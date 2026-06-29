# Multi-Currency Reporting

## Overview
This module supports multi-currency reporting with automatic exchange rate conversion for financial dashboards.

### Features
- Fetch real-time exchange rates automatically from a reliable API.
- Apply exchange rates to financial entries from international subsidiaries.
- Support report generation with date-specific exchange rate values.
- Generate and export consolidated financial reports formatted with accurate currency conversion.

## Implementation

### Integration
We use [Exchangerate-API](https://exchangerate-api.com) to fetch real-time exchange rates:

**Steps:**
1. Retrieve exchange rates via the API for selected dates.
2. Apply rates during financial data processing.
3. Cache rates locally for enhanced performance.

### Code Example
#### Fetching Rates:
```python
import requests
import datetime

class ExchangeRateService:
    API_URL = "https://open.er-api.com/v6/latest/"

    def __init__(self, base_currency):
        self.base_currency = base_currency

    def fetch_exchange_rates(self):
        url = f"{self.API_URL}{self.base_currency}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Failed to fetch exchange rates: {response.status_code}")

# Example Usage
service = ExchangeRateService(base_currency="USD")
exchange_rates = service.fetch_exchange_rates()
print(exchange_rates)
```

### Report Conversion
#### Apply Exchange Rates:
```python
def convert_currency(amount, rate):
    return round(amount * rate, 2)

def process_financial_data(data_entries, rates):
    for entry in data_entries:
        entry['converted_amount'] = convert_currency(entry['amount'], rates[entry['currency']])
```

## Export
Reports will include:
1. Converted values.
2. Base currency.
3. Exchange rate details.

### Error Handling
- Handle API failures gracefully.
- Log errors for audit.

---