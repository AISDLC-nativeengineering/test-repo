import requests

class ExchangeRateProvider:
    """Fetch exchange rates from a third-party API."""
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_rates(self):
        """Fetch the latest exchange rates."""
        try:
            response = requests.get(f"{self.base_url}?app_id={self.api_key}")
            response.raise_for_status()
            return response.json()['rates']
        except requests.RequestException as e:
            print(f"Error fetching rates: {e}")
            return None

class MultiCurrencyReport:
    """Generate financial reports with multi-currency support."""
    def __init__(self, exchange_rate_provider):
        self.exchange_rate_provider = exchange_rate_provider

    def convert_currency(self, amount, from_currency, to_currency, rates):
        """Convert amount from one currency to another."""
        if from_currency == to_currency:
            return amount
        try:
            converted_amount = amount / rates[from_currency] * rates[to_currency]
            return round(converted_amount, 2)
        except KeyError:
            print(f"Invalid currency: {from_currency} or {to_currency}")
            return None

    def generate_report(self, data, to_currency):
        """Generate report in the selected currency."""
        rates = self.exchange_rate_provider.fetch_rates()
        if not rates:
            print("Using cached rates for report generation.")
            rates = self.exchange_rate_provider.cached_rates

        report = []
        for entry in data:
            converted_value = self.convert_currency(entry['value'], entry['currency'], to_currency, rates)
            report.append({"name": entry['name'], "converted_value": converted_value})

        return report

# Example usage
if __name__ == "__main__":
    api_key = "your_api_key_here"
    base_url = "https://openexchangerates.org/api/latest.json"
    provider = ExchangeRateProvider(api_key, base_url)
    report_generator = MultiCurrencyReport(provider)

    # Sample accounting data
    data = [
        {"name": "Revenue", "value": 1000, "currency": "USD"},
        {"name": "Expense", "value": 500, "currency": "EUR"}
    ]

    # Generate report
    report = report_generator.generate_report(data, "GBP")
    for item in report:
        print(f"{item['name']}: {item['converted_value']} GBP")