import requests
from datetime import datetime

def fetch_exchange_rates(date_range=None):
    """
    Fetch exchange rates with a fallback and historical rate handling.

    :param date_range: tuple of (start_date, end_date) for historical rates.
    :return: Dictionary of exchange rates or fallback values.
    """
    try:
        if date_range:
            # Fetch historical rates for the specified date range
            start_date, end_date = date_range
            response = requests.get(f"https://api.exchangeratesapi.com/history?start_at={start_date}&end_at={end_date}")
        else:
            # Fetch latest rates
            response = requests.get("https://api.exchangeratesapi.com/latest")

        response.raise_for_status()
        return response.json().get("rates", {})

    except requests.RequestException:
        # Fallback mechanism: Use hardcoded rates
        return {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.75
        }