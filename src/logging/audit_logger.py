import json
from datetime import datetime

def log_change(report_id, user_id, change_description):
    """
    Logs a change to the change_logs table.

    :param report_id: ID of the financial report being modified.
    :param user_id: ID of the user making the change.
    :param change_description: Description of the change.
    """
    # Example log entry format
    log_entry = {
        "report_id": report_id,
        "user_id": user_id,
        "timestamp": datetime.now().isoformat(),
        "description": change_description
    }

    with open("change_log.json", "a") as log_file:
        log_file.write(json.dumps(log_entry))
        log_file.write("\n")


def export_logs_to_csv():
    """
    Exports all logs to a CSV file.
    """
    import csv

    with open("change_log.json", "r") as log_file, open("change_logs.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write CSV header
        csv_writer.writerow(["Report ID", "User ID", "Timestamp", "Description"])

        # Write each log entry
        for line in log_file:
            entry = json.loads(line.strip())
            csv_writer.writerow([entry["report_id"], entry["user_id"], entry["timestamp"], entry["description"]])

__all__ = ["log_change", "export_logs_to_csv"]