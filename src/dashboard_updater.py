import time
import requests
from threading import Timer

class DashboardUpdater:
    REFRESH_INTERVAL = 60  # Refresh every 60 seconds

    def __init__(self):
        self.is_active = True  # To control automatic refresh

    def fetch_recent_transactions(self):
        """
        Fetch recent transactions from the backend API.
        """
        try:
            response = requests.get("/api/v1/transactions/recent")
            response.raise_for_status()
            transactions = response.json()
            self.update_dashboard(transactions)
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)

    def manual_refresh(self):
        """
        Triggered by a manual Refresh button click.
        """
        try:
            response = requests.post("/api/v1/user/refresh-data")
            response.raise_for_status()
            print("Manual refresh successful.")
            self.fetch_recent_transactions()
        except requests.exceptions.RequestException as e:
            print("Manual refresh failed:", e)

    def schedule_refresh(self):
        """
        Automatically refresh the dashboard at regular intervals.
        """
        if self.is_active:
            self.fetch_recent_transactions()
            Timer(self.REFRESH_INTERVAL, self.schedule_refresh).start()

    def update_dashboard(self, transactions):
        """
        Update the dashboard with the fetched transaction data.
        """
        print("Dashboard updated with transactions:", transactions)

    def stop_refresh(self):
        """
        Stop automatic refreshing when the dashboard is inactive.
        """
        self.is_active = False

# Example usage
if __name__ == "__main__":
    updater = DashboardUpdater()

    # Start automatic refresh
    updater.schedule_refresh()

    # Simulate stopping after some time
    Timer(300, updater.stop_refresh).start()  # Stop after 5 minutes
