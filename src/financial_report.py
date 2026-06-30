import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests

class FinancialReport:
    def __init__(self, dataset_path, api_key, base_currency):
        self.dataset_path = dataset_path
        self.api_key = api_key
        self.base_currency = base_currency
        self.data = None
        self.exchange_rates = {}

    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)

    def fetch_exchange_rates(self):
        """Fetch real-time exchange rates."""
        try:
            url = f"https://openexchangerates.org/api/latest.json?app_id={self.api_key}"
            response = requests.get(url)
            response.raise_for_status()
            self.exchange_rates = response.json()['rates']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")

    def apply_currency_conversion(self):
        """Apply currency conversion to financial data."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        if not self.exchange_rates:
            raise ValueError("Exchange rates not fetched. Call `fetch_exchange_rates()` first.")

        self.data['Converted'] = self.data['Amount'] * self.data['Currency'].map(self.exchange_rates).div(self.exchange_rates[self.base_currency])

    def compute_variance(self):
        """Computes variance between planned and actual figures after conversion."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")
        
        if 'Converted' not in self.data.columns:
            raise ValueError("Currency conversion not applied. Call `apply_currency_conversion()` first.")

        self.data['Variance'] = self.data['Actual'] - self.data['Converted']

    def generate_visualization(self, output_path):
        """Generate graphs to visualize variance."""
        if self.data is None or 'Variance' not in self.data.columns:
            raise ValueError("Variance not computed. Call `compute_variance()` first.")
        
        plt.figure(figsize=(10, 6))
        plt.bar(self.data['Category'], self.data['Variance'], color=['green' if x >= 0 else 'red' for x in self.data['Variance']])
        plt.xlabel('Category')
        plt.ylabel('Variance')
        plt.title('Financial Variance Analysis')
        plt.savefig(output_path)
        plt.close()

    def export_report(self, format='pdf', output_path='financial_report.pdf'):
        """Export the report including converted amounts in PDF or Excel."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        if format == 'pdf':
            from matplotlib.backends.backend_pdf import PdfPages
            with PdfPages(output_path) as pdf:
                plt.figure(figsize=(10, 6))
                plt.bar(self.data['Category'], self.data['Variance'], color=['green' if x >= 0 else 'red' for x in self.data['Variance']])
                plt.xlabel('Category')
                plt.ylabel('Variance')
                plt.title('Financial Variance Analysis')
                pdf.savefig()
                plt.close()
        elif format == 'excel':
            self.data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv', api_key='YOUR_API_KEY', base_currency='USD')
# report.load_data()
# report.fetch_exchange_rates()
# report.apply_currency_conversion()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')