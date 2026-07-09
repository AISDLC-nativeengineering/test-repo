# threat_service.py

from datetime import datetime

def filter_threats(severity=None, category=None, timeline=None):
    """
    Filters threats based on severity, category, and timeline.

    Parameters:
        severity (str): Severity level (Critical, High, Medium, Low).
        category (str): Category of threats (e.g., Malware, Phishing).
        timeline (tuple): Start and end dates as strings ('YYYY-MM-DD').

    Returns:
        list: Filtered list of threats.
    """
    threats = [
        {
            "id": "123",
            "severity": "Critical",
            "category": "Phishing",
            "timestamp": "2023-10-01",
            "status": "Pending",
            "suggested_actions": ["Disable email account", "Notify affected users"]
        },
        # Add more dummy threats for testing
    ]

    # Filter based on severity
    if severity:
        threats = [threat for threat in threats if threat["severity"] == severity]

    # Filter based on category
    if category:
        threats = [threat for threat in threats if threat["category"] == category]

    # Filter based on timeline
    if timeline:
        start_date, end_date = map(datetime.fromisoformat, timeline)
        threats = [
            threat for threat in threats
            if start_date <= datetime.fromisoformat(threat["timestamp"]) <= end_date
        ]

    return threats

def mitigate_threat(threat_id):
    """
    Retrieves suggested actions for mitigating a threat.

    Parameters:
        threat_id (str): Threat ID.

    Returns:
        dict: Suggested mitigation actions.
    """
    threats = {
        "123": ["Disable email account", "Notify affected users"],
        # Add more dummy threat actions for testing
    }

    actions = threats.get(threat_id, [])
    return {
        "message": "Suggested actions retrieved successfully",
        "actions": actions
    }