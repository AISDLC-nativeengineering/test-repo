import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from src.exchange_rate import ExchangeRateFetcher

class FinancialReport:
    def __init__(self, dataset_path, base_currency='USD', api_url='', api_key=''):
        self.dataset_path = dataset_path
        self.base_currency = base_currency
        self.api_url = api_url
        self.api_key = api_key
        self.data = None
        self.exchange_rates = {}

    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)

    def fetch_exchange_rates(self):
        """Fetches real-time exchange rates using ExchangeRateFetcher."""
        fetcher = ExchangeRateFetcher(api_url=self.api_url, api_key=self.api_key)
        self.exchange_rates = fetcher.fetch_rates()

    def convert_currencies(self):
        """Converts financial data to the base currency using exchange rates."""
        if not self.exchange_rates:
            raise ValueError("Exchange rates not available. Call `fetch_exchange_rates()` first.")

        def convert(row):
            rate = self.exchange_rates.get(row['Currency'], 1)
            return row['Amount'] * rate / self.exchange_rates.get(self.base_currency, 1)

        self.data['ConvertedAmount'] = self.data.apply(convert, axis=1)

    def compute_variance(self):
        """Computes variance between planned and actual financial figures."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")
        self.data['Variance'] = self.data['Actual'] - self.data['Planned']

    def generate_visualization(self, output_path):
        """Generate graphs or charts to visualize the variance."""
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
        """Export the report in specified format (PDF or Excel)."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        if format == 'pdf':
            # Export visualization as part of PDF report
            from matplotlib.backends.backend_pdf import PdfPages
            with PdfPages(output_path) as pdf:
                plt.figure(figsize=(10, 6))
                plt.bar(self.data['Category'], self.data['Variance'], color=['green' if x >= 0 else 'red' for x in self.data['Variance']])
                plt.xlabel('Category')
                plt.ylabel('Variance')
                plt.title('Financial Variance Analysis')
                pdf.savefig()  # Save plot to PDF
                plt.close()
        elif format == 'excel':
            self.data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv', base_currency='USD', api_url='https://api.openexchangerates.org', api_key='your_api_key')
# report.load_data()
# report.fetch_exchange_rates()
# report.convert_currencies()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')