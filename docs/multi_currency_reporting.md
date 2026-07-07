# Multi-Currency Reporting

## Description
This module implements functionality for generating financial reports in multiple currencies with automatic exchange rate conversion. It integrates with third-party exchange rate APIs, handles fallback scenarios, and complies with international rounding standards.

## Features
- Select desired reporting currency
- Fetch up-to-date exchange rates from a third-party API
- Use cached rates when the API is unavailable
- Generate reports in selected currency with accurate rounding

## Technical Notes
- Integration with OpenExchangeRates or XE API
- Caching mechanism for exchange rates
- Compliance with IFRS rounding standards

## Future Enhancements
- Additional fallback APIs
- Real-time currency conversion dashboard