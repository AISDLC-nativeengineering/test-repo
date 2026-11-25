import unittest
from datetime import datetime, timedelta, timezone
from threading import Event

from src.report_automation import ReportScheduler


class ReportSchedulerTests(unittest.TestCase):
    def test_runs_due_report_with_latest_parameters(self):
        generated = Event()
        reports = []

        def generate(report_id, parameters):
            reports.append((report_id, parameters))
            generated.set()

        scheduler = ReportScheduler(
            generate,
            lambda message: self.fail(f"Unexpected notification: {message}"),
            poll_interval_seconds=0.01,
        )
        schedule = (
            datetime.now(timezone.utc) + timedelta(seconds=0.1)
        ).isoformat()

        scheduler.schedule_report("governance", schedule, {"period": "monthly"})
        scheduler.start()
        try:
            scheduler.update_parameters("governance", {"period": "quarterly"})
            self.assertTrue(generated.wait(timeout=2))
        finally:
            scheduler.shutdown()

        self.assertEqual(reports, [("governance", {"period": "quarterly"})])

    def test_rejects_timezone_naive_schedule_and_notifies(self):
        notifications = []
        scheduler = ReportScheduler(
            lambda report_id, parameters: None, notifications.append
        )

        with self.assertRaisesRegex(ValueError, "must include a timezone"):
            scheduler.schedule_report(
                "governance", "2026-11-25T10:00:00", {}
            )

        self.assertEqual(len(notifications), 1)
        self.assertIn("must include a timezone", notifications[0])

    def test_generation_failure_is_notified_and_scheduler_continues(self):
        notified = Event()
        generated = Event()
        reports = []

        def generate(report_id, parameters):
            if report_id == "broken":
                raise RuntimeError("template unavailable")
            reports.append(report_id)
            generated.set()

        def notify(message):
            if "template unavailable" in message:
                notified.set()

        scheduler = ReportScheduler(generate, notify, poll_interval_seconds=0.01)
        schedule = (
            datetime.now(timezone.utc) - timedelta(seconds=1)
        ).isoformat()
        scheduler.schedule_report("broken", schedule, {})
        scheduler.schedule_report("healthy", schedule, {})
        scheduler.start()
        try:
            self.assertTrue(notified.wait(timeout=2))
            self.assertTrue(generated.wait(timeout=2))
        finally:
            scheduler.shutdown()

        self.assertEqual(reports, ["healthy"])


if __name__ == "__main__":
    unittest.main()
