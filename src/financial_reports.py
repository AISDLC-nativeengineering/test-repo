# financial_reports.py

import datetime

# In-memory storage for demonstration purposes
report_versions = {}
audit_logs = []


def save_version(report_id, content):
    """
    Save a new version of the financial report.

    Parameters:
        report_id (str): The unique ID of the report.
        content (str): The report content.

    Returns:
        dict: Information about the saved version.
    """
    timestamp = datetime.datetime.now().isoformat()
    version_id = len(report_versions.get(report_id, [])) + 1
    version_info = {
        'version_id': version_id,
        'timestamp': timestamp,
        'content': content,
    }

    if report_id not in report_versions:
        report_versions[report_id] = []

    report_versions[report_id].append(version_info)
    return version_info


def get_versions(report_id):
    """
    Retrieve all versions of a financial report.

    Parameters:
        report_id (str): The unique ID of the report.

    Returns:
        list: List of all versions with timestamps and IDs.
    """
    return report_versions.get(report_id, [])


def revert_to_version(report_id, version_id):
    """
    Revert the financial report to a specific version.

    Parameters:
        report_id (str): The unique ID of the report.
        version_id (int): The ID of the version to revert to.

    Returns:
        dict: Details of the reverted version.
    """
    versions = report_versions.get(report_id, [])

    if not versions:
        raise ValueError("No versions found for the specified report.")

    if version_id < 1 or version_id > len(versions):
        raise ValueError("Invalid version ID.")

    # Get the target version
    target_version = versions[version_id - 1]

    # Save the current version as a new version before reverting
    current_content = versions[-1]['content']
    save_version(report_id, current_content)

    # Log the revert event
    log_reversion(report_id, version_id)

    return {
        'reverted_to': target_version,
        'current_content_preserved': current_content
    }


def log_reversion(report_id, version_id):
    """
    Log the details of a report reversion.

    Parameters:
        report_id (str): The unique ID of the report.
        version_id (int): The ID of the version reverted to.
    """
    log_entry = {
        'report_id': report_id,
        'version_id': version_id,
        'timestamp': datetime.datetime.now().isoformat(),
        'user': 'system',  # Placeholder for user identification
    }
    audit_logs.append(log_entry)

# Example usage
def main():
    report_id = "report_1"
    save_version(report_id, "Initial content of report.")
    save_version(report_id, "Updated content of report.")

    print("Report Versions:", get_versions(report_id))

    print("Reverting to version 1...")
    print(revert_to_version(report_id, 1))

    print("Audit Logs:", audit_logs)

if __name__ == "__main__":
    main()