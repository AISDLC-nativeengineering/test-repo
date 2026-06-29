import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests

class FinancialReport:
    def __init__(self, dataset_path, currency_api_url, base_currency):
        self.dataset_path = dataset_path
        self.currency_api_url = currency_api_url
        self.base_currency = base_currency
        self.data = None
        self.exchange_rates = {}

    def fetch_exchange_rates(self):
        """Fetch real-time exchange rates from the API."""
        response = requests.get(self.currency_api_url)
        if response.status_code == 200:
            self.exchange_rates = response.json().get('rates', {})
        else:
            raise Exception("Failed to fetch exchange rates")

    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)

    def apply_currency_conversion(self):
        """Convert all financial values to the base currency."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")
        if not self.exchange_rates:
            raise ValueError("Exchange rates not loaded. Call `fetch_exchange_rates()` first.")

        # Assuming 'Currency' column exists and indicates currency for each data row
        # 'Amount' column holds financial values needing conversion
        def convert(row):
            rate = self.exchange_rates.get(row['Currency'], 1)
            return row['Amount'] * rate

        self.data['ConvertedAmount'] = self.data.apply(convert, axis=1)

    def compute_variance(self):
        """Computes variance between planned and actual financial figures."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")
        self.data['Variance'] = self.data['ConvertedAmount'] - self.data['Planned']
        self.data['ExchangeRateUsed'] = self.data['Currency'].map(self.exchange_rates)

    def generate_visualization(self, output_path):
        """Generate graphs or charts to visualize the variance."""
        if self.data is None or 'Variance' not in self.data.columns:
            raise ValueError("Variance not computed. Call `compute_variance()` first.")
        plt.figure(figsize=(10, 6))
        plt.bar(self.data['Category'], self.data['Variance'], color=['green' if x >= 0 else 'red' for x in self.data['Variance']])
        plt.xlabel('Category')
        plt.ylabel('Variance')
        plt.title(f'Financial Variance Analysis ({self.base_currency})')
        plt.savefig(output_path)
        plt.close()

    def export_report(self, format='pdf', output_path='financial_report.pdf'):
        """Export the report in specified format (PDF or Excel)."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        if format == 'pdf':
            from matplotlib.backends.backend_pdf import PdfPages
            with PdfPages(output_path) as pdf:
                plt.figure(figsize=(10, 6))
                plt.bar(self.data['Category'], self.data['Variance'], color=['green' if x >= 0 else 'red' for x in self.data['Variance']])
                plt.xlabel('Category')
                plt.ylabel('Variance')
                plt.title(f'Financial Variance Analysis ({self.base_currency})')
                pdf.savefig()
                plt.close()
        elif format == 'excel':
            self.data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv', currency_api_url='https://api.exchangerate-api.com/v4/latest/USD', base_currency='USD')
# report.fetch_exchange_rates()
# report.load_data()
# report.apply_currency_conversion()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')