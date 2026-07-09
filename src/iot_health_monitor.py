# AINA-257: IoT Health Monitor
"""
This module monitors the health and uptime of the smart lighting system.
Provides:
- Real-time component statuses (Active/Inactive)
- Downtime alerts and notifications
- GDPR compliance logs with timestamped sensor operations
"""

# Required imports
import json
import time

class IoTHealthMonitor:
    def __init__(self):
        self.component_statuses = {}
        self.alerts = []
        self.gdpr_logs = []

    def update_component_status(self, component_id, status):
        """
        Update the status of a component.
        Args:
            component_id (str): ID of the component
            status (str): Status (e.g., 'Active', 'Inactive')
        """
        self.component_statuses[component_id] = status

    def flag_downtime_alert(self, component_id):
        """
        Flag downtime for a given component.
        Args:
            component_id (str): ID of the component
        Returns:
            dict: Alert details
        """
        alert = {
            "component_id": component_id,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Downtime flagged",
        }
        self.alerts.append(alert)
        print(f"ALERT: Component {component_id} downtime flagged!")
        return alert

    def log_gdpr_compliance(self, component_id, data):
        """
        Log GDPR compliance data for a component.
        Args:
            component_id (str): ID of the component
            data (dict): GDPR data
        """
        log_entry = {
            "component_id": component_id,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "data": data,
        }
        self.gdpr_logs.append(log_entry)

    def view_gdpr_logs(self):
        """
        View GDPR compliance logs.
        Returns:
            list: GDPR logs
        """
        return json.dumps(self.gdpr_logs, indent=4)

# Example usage
if __name__ == "__main__":
    monitor = IoTHealthMonitor()

    # Update component status
    monitor.update_component_status("sensor_001", "Active")
    monitor.update_component_status("sensor_002", "Inactive")

    # Flag downtime alert
    monitor.flag_downtime_alert("sensor_002")

    # Log GDPR compliance data
    monitor.log_gdpr_compliance("sensor_001", {"data_point": "Temperature Reading", "value": "22°C"})

    # View GDPR compliance logs
    print(monitor.view_gdpr_logs())