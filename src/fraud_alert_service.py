import datetime

def fraud_alert_notification(transaction_id, fraud_type, account_id, amount, location, timestamp):
    return {
        "transactionId": transaction_id,
        "fraudType": fraud_type,
        "accountId": account_id,
        "amount": amount,
        "location": location,
        "timestamp": timestamp,
    }

class FraudAlertService:
    def __init__(self, message_broker):
        self.message_broker = message_broker

    def send_alert(self, transaction_metadata):
        alert = fraud_alert_notification(
            transaction_metadata.get("transactionId"),
            transaction_metadata.get("fraudType"),
            transaction_metadata.get("accountId"),
            transaction_metadata.get("amount"),
            transaction_metadata.get("location"),
            transaction_metadata.get("timestamp")
        )
        self.message_broker.publish(alert)

    def mark_alert_resolved(self, alert_id):
        resolution_log = {
            "alertId": alert_id,
            "status": "resolved",
            "resolvedAt": datetime.datetime.now().isoformat()
        }
        print("Resolution logged: ", resolution_log)
