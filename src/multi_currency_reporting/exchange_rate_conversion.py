import requests

def fetch_exchange_rates(api_url):
    """
    Fetches exchange rates from the provided external API.

    Args:
        api_url (str): The URL of the external API.

    Returns:
        dict: A dictionary containing currency codes as keys and their rates as values.
    """
    try:
        response = requests.get(api_url)
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
    return amount * (to_rate / from_rate)

# Example API integration
if __name__ == "__main__":
    exchange_api = "https://api.exchangerate-api.com/v4/latest/USD"
    rates = fetch_exchange_rates(exchange_api)
    if rates:
        print("Exchange rates fetched successfully!")
    else:
        print("Failed to fetch exchange rates.")