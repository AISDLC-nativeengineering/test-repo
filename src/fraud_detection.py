# fraud_detection.py

import json

class TransactionMonitor:

    def __init__(self):
        """
        Initializes the transaction monitor for fraud detection.
        """
        self.flagged_transactions = []

    def process_transaction(self, transaction):
        """
        Processes a transaction and checks for fraudulent patterns.
        
        Args:
            transaction (dict): A dictionary representing the transaction data.
        
        Returns:
            dict: A result dictionary indicating if fraud was detected.
        """
        result = {"transaction_id": transaction.get("transaction_id"), "is_fraud": False, "reason": ""}

        if self._is_suspicious(transaction):
            result["is_fraud"] = True
            result["reason"] = "Pattern indicating potential fraud detected."
            self.flagged_transactions.append(transaction)

        return result

    def _is_suspicious(self, transaction):
        """
        Determines if a transaction is suspicious.
        
        Args:
            transaction (dict): A dictionary representing the transaction data.
        
        Returns:
            bool: True if the transaction is suspicious, False otherwise.
        """
        # Example suspicious pattern: Sudden large transaction
        if transaction.get("amount") > 10000:
            return True

        return False

    def get_flagged_details(self):
        """
        Retrieves details of flagged transactions.

        Returns:
            list: A list of flagged transactions.
        """
        return self.flagged_transactions

def main():
    transaction_monitor = TransactionMonitor()

    # Example transaction stream
    transactions = [
        {"transaction_id": "txn1", "amount": 500, "description": "Normal Transaction"},
        {"transaction_id": "txn2", "amount": 15000, "description": "Large Transaction"}
    ]

    for transaction in transactions:
        result = transaction_monitor.process_transaction(transaction)
        print(json.dumps(result, indent=2))

    # Simulate compliance officer clicking on alerts
    flagged_transactions = transaction_monitor.get_flagged_details()
    if flagged_transactions:
        print("Flagged Transactions:")
        print(json.dumps(flagged_transactions, indent=2))

if __name__ == "__main__":
    main()