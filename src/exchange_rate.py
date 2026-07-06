import requests
import logging

class ExchangeRateFetcher:
    """Fetches real-time currency exchange rates from configured API."""

    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def fetch_rates(self):
        """Fetches exchange rates from API."""
        try:
            response = requests.get(f"{self.api_url}/latest", params={"access_key": self.api_key})
            response.raise_for_status()
            data = response.json()
            if "rates" in data:
                return data["rates"]
            else:
                logging.error("Exchange rates not found in response.")
                raise ValueError("Invalid API response format.")
        except requests.RequestException as e:
            logging.error(f"Failed to fetch exchange rates: {e}")
            raise ValueError("Exchange rate API call failed.")

# Example usage
# fetcher = ExchangeRateFetcher(api_url="https://api.openexchangerates.org", api_key="your_api_key")
# rates = fetcher.fetch_rates()
# print(rates)