import requests
from datetime import datetime

def fetch_exchange_rates(api_url, reporting_date=None):
    """
    Fetches exchange rates from the provided external API for a specific reporting date.

    Args:
        api_url (str): The URL of the external API.
        reporting_date (str): The reporting date in YYYY-MM-DD format.

    Returns:
        dict: A dictionary containing currency codes as keys and their rates as values.
    """
    try:
        params = {'date': reporting_date} if reporting_date else {}
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return {}

def convert_currency(amount, from_rate, to_rate):
    """
    Converts an amount from one currency to another using given rates.

    Args:
        amount (float): The amount to convert.
        from_rate (float): The exchange rate of the source currency.
        to_rate (float): The exchange rate of the target currency.

    Returns:
        float: The converted amount.
    """
    try:
        return round(amount * (to_rate / from_rate), 2)
    except ZeroDivisionError:
        print("Error: Division by zero in rate conversion")
        return 0.0

def generate_report(base_currency, transactions, api_url, reporting_date):
    """
    Generates a financial report with multi-currency conversion.

    Args:
        base_currency (str): The base currency for the report.
        transactions (list of dict): List of transactions with 'amount' and 'currency'.
        api_url (str): The external API URL for exchange rates.
        reporting_date (str): The reporting date (YYYY-MM-DD).

    Returns:
        dict: Report containing converted amounts and exchange rates.
    """
    rates = fetch_exchange_rates(api_url, reporting_date)
    if not rates:
        return {"error": "Failed to fetch exchange rates"}

    report = {
        "base_currency": base_currency,
        "reporting_date": reporting_date,
        "transactions": []
    }

    for transaction in transactions:
        amount = transaction['amount']
        currency = transaction['currency']
        from_rate = rates.get('rates', {}).get(currency, 0)
        to_rate = rates.get('rates', {}).get(base_currency, 0)
        converted_amount = convert_currency(amount, from_rate, to_rate)

        report["transactions"].append({
            "original_amount": amount,
            "original_currency": currency,
            "converted_amount": converted_amount,
            "base_currency": base_currency
        })

    report["exchange_rates"] = rates
    return report

# Example Usage
if __name__ == "__main__":
    exchange_api = "https://api.exchangerate-api.com/v4/latest/USD"
    transactions = [
        {"amount": 100, "currency": "EUR"},
        {"amount": 200, "currency": "GBP"}
    ]
    report_date = "2023-10-01"
    financial_report = generate_report("USD", transactions, exchange_api, report_date)
    print(financial_report)