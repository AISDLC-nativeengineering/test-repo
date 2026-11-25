from __future__ import annotations

import logging
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from threading import Condition, Thread, current_thread
from typing import NoReturn


logger = logging.getLogger(__name__)

ReportGenerator = Callable[[str, Mapping[str, object]], None]
ErrorNotifier = Callable[[str], None]


@dataclass
class _ScheduledReport:
    scheduled_at: datetime
    parameters: dict[str, object]


class ReportScheduler:
    def __init__(
        self,
        report_generator: ReportGenerator,
        error_notifier: ErrorNotifier,
        poll_interval_seconds: float = 1.0,
    ) -> None:
        if poll_interval_seconds <= 0:
            raise ValueError("poll_interval_seconds must be greater than zero")

        self._report_generator = report_generator
        self._error_notifier = error_notifier
        self._poll_interval_seconds = poll_interval_seconds
        self._condition = Condition()
        self._schedules: dict[str, _ScheduledReport] = {}
        self._worker: Thread | None = None
        self._stopping = False

    def schedule_report(
        self,
        report_id: str,
        schedule: str,
        parameters: Mapping[str, object],
    ) -> None:
        if not isinstance(report_id, str) or not report_id.strip():
            self._configuration_error("report_id must be a non-empty string")
        scheduled_at = self._parse_schedule(schedule)
        parameter_values = self._copy_parameters(parameters)

        with self._condition:
            if report_id in self._schedules:
                self._configuration_error(
                    f"Report '{report_id}' already has a pending schedule"
                )
            self._schedules[report_id] = _ScheduledReport(
                scheduled_at=scheduled_at,
                parameters=parameter_values,
            )
            self._condition.notify()

    def update_parameters(
        self, report_id: str, parameters: Mapping[str, object]
    ) -> None:
        parameter_values = self._copy_parameters(parameters)
        with self._condition:
            scheduled_report = self._schedules.get(report_id)
            if scheduled_report is None:
                self._configuration_error(
                    f"No pending schedule exists for report '{report_id}'"
                )
            scheduled_report.parameters = parameter_values

    def start(self) -> None:
        with self._condition:
            if self._worker is not None and self._worker.is_alive():
                return
            self._stopping = False
            self._worker = Thread(
                target=self._run, name="report-scheduler", daemon=True
            )
            self._worker.start()

    def shutdown(self) -> None:
        with self._condition:
            self._stopping = True
            worker = self._worker
            self._condition.notify_all()
        if worker is not None and worker is not current_thread():
            worker.join()

    def _run(self) -> None:
        while True:
            with self._condition:
                if self._stopping:
                    return
                if not self._schedules:
                    self._condition.wait()
                    continue

                next_report_id = min(
                    self._schedules,
                    key=lambda report_id: self._schedules[report_id].scheduled_at,
                )
                next_report = self._schedules[next_report_id]
                now = datetime.now(timezone.utc)
                wait_seconds = (next_report.scheduled_at - now).total_seconds()
                if wait_seconds > 0:
                    self._condition.wait(
                        min(wait_seconds, self._poll_interval_seconds)
                    )
                    continue

                due_reports = sorted(
                    (
                        (report_id, report)
                        for report_id, report in self._schedules.items()
                        if report.scheduled_at <= now
                    ),
                    key=lambda item: item[1].scheduled_at,
                )
                for report_id, _ in due_reports:
                    del self._schedules[report_id]
                due_reports = [
                    (report_id, dict(report.parameters))
                    for report_id, report in due_reports
                ]

            for report_id, parameters in due_reports:
                try:
                    self._report_generator(report_id, parameters)
                except Exception as error:
                    message = f"Report '{report_id}' generation failed: {error}"
                    logger.exception(message)
                    self._notify_error(message)

    def _parse_schedule(self, schedule: str) -> datetime:
        if not isinstance(schedule, str):
            self._configuration_error("schedule must be an ISO 8601 string")
        try:
            scheduled_at = datetime.fromisoformat(
                schedule.replace("Z", "+00:00")
            )
        except ValueError:
            self._configuration_error(
                "schedule must be a valid ISO 8601 datetime"
            )
        if scheduled_at.tzinfo is None or scheduled_at.utcoffset() is None:
            self._configuration_error("schedule must include a timezone")
        return scheduled_at.astimezone(timezone.utc)

    def _copy_parameters(
        self, parameters: Mapping[str, object]
    ) -> dict[str, object]:
        if not isinstance(parameters, Mapping) or any(
            not isinstance(key, str) for key in parameters
        ):
            self._configuration_error(
                "parameters must be a mapping with string keys"
            )
        return dict(parameters)

    def _configuration_error(self, message: str) -> NoReturn:
        logger.error(message)
        self._notify_error(message)
        raise ValueError(message)

    def _notify_error(self, message: str) -> None:
        try:
            self._error_notifier(message)
        except Exception:
            logger.exception("Could not send report automation error notification")
