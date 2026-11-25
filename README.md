# test-repo
A public test repository created via API

## Scheduled report generation

`src.report_automation.ReportScheduler` runs a report callback at a timezone-aware
ISO 8601 datetime. Parameters can be updated until the scheduled report starts.
The error notifier is called for invalid configuration and report-generation
failures. Schedules are held in process memory, so register them when the service
starts.

```python
from src.report_automation import ReportScheduler

scheduler = ReportScheduler(
    report_generator=generate_report,
    error_notifier=send_notification,
)
scheduler.schedule_report(
    "governance", "2026-12-01T09:00:00+01:00", {"period": "monthly"}
)
scheduler.update_parameters("governance", {"period": "quarterly"})
scheduler.start()

try:
    run_service()
finally:
    scheduler.shutdown()
```
