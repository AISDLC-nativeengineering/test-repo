import requests

def fetch_exchange_rate(api_url, base_currency, target_currency):
    """ Fetch live exchange rate from the given API. Returns exchange rate."""
    response = requests.get(f"{api_url}/latest", params={"base": base_currency})
    if response.status_code == 200:
        rates = response.json().get("rates", {})
        return rates.get(target_currency)
    else:
        raise Exception(f"Failed to fetch exchange rates: {response.text}")

def generate_report(data, base_currency, target_currency, api_url):
    """ Generate financial report with converted values."""
    exchange_rate = fetch_exchange_rate(api_url, base_currency, target_currency)
    report = []
    for record in data:
        converted_value = record['amount'] * exchange_rate
        report.append({
            "name": record['name'],
            "amount": record['amount'],
            "converted_amount": converted_value,
            "currency": target_currency
        })
    return report

def export_report(report, filename):
    """ Export the multi-currency report as a JSON file."""
    with open(filename, 'w') as file:
        import json
        json.dump(report, file, indent=4)

def main():
    # Example data
    data = [
        {"name": "Revenue", "amount": 10000},
        {"name": "Cost", "amount": 5000}
    ]

    # User configuration
    base_currency = "USD"
    target_currency = "EUR"
    api_url = "https://api.exchangerate-api.com/v4"

    # Generate and export report
    report = generate_report(data, base_currency, target_currency, api_url)
    export_report(report, "multi_currency_report.json")

if __name__ == "__main__":
    main()