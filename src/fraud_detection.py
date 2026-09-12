import json
import time

class FraudDetection:
    def __init__(self, model, notification_service, dashboard_service):
        self.model = model
        self.notification_service = notification_service
        self.dashboard_service = dashboard_service

    def analyze_transaction(self, transaction):
        """
        Analyze the transaction to detect fraud.

        Args:
        transaction (dict): Transaction details containing transaction_id, 
                            amount, currency, timestamp, and other metadata.

        Returns:
        dict: Fraud analysis result containing status, alert_id, and message.
        """
        fraud_score = self.model.predict(transaction)

        if fraud_score > 0.9:
            alert_id = self._generate_alert(transaction, fraud_score)
            return {
                "status": "flagged",
                "alert_id": alert_id,
                "message": "Suspicious transaction flagged for review"
            }
        else:
            return {
                "status": "pending",
                "alert_id": None,
                "message": "Transaction does not meet fraud threshold"
            }

    def _generate_alert(self, transaction, fraud_score):
        """
        Generate a fraud alert for a transaction.

        Args:
        transaction (dict): Transaction details.
        fraud_score (float): Fraud score provided by the model.

        Returns:
        str: Alert ID for the created alert.
        """
        alert = {
            "alert_id": f"alert-{int(time.time())}",
            "time_created": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            "transaction_id": transaction["transaction_id"],
            "fraud_score": fraud_score,
            "status": "flagged"
        }
        self.notification_service.send_notification(alert)
        self.dashboard_service.update_dashboard(alert)

        return alert["alert_id"]

# Example usage:
if __name__ == "__main__":
    class MockModel:
        def predict(self, transaction):
            return 0.95  # Mock fraud score

    class MockNotificationService:
        def send_notification(self, alert):
            print(f"Notification sent for alert: {json.dumps(alert)}")

    class MockDashboardService:
        def update_dashboard(self, alert):
            print(f"Dashboard updated with alert: {json.dumps(alert)}")

    transaction_example = {
        "transaction_id": "TX12345",
        "amount": 1500.50,
        "currency": "USD",
        "timestamp": "2026-09-12T18:05:55Z",
        "source_account": "ACC123",
        "target_account": "ACC321"
    }

    fraud_detection = FraudDetection(MockModel(), MockNotificationService(), MockDashboardService())
    result = fraud_detection.analyze_transaction(transaction_example)
    print(result)
