import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests

class FinancialReport:
    def __init__(self, dataset_path, target_currency='USD'):
        self.dataset_path = dataset_path
        self.data = None
        self.target_currency = target_currency
        self.exchange_rates = {}

    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)

    def fetch_exchange_rates(self, base_currency='USD'):
        """Fetch the latest exchange rates using an external API."""
        try:
            response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{base_currency}')
            response.raise_for_status()
            data = response.json()
            self.exchange_rates = data['rates']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")

    def convert_currency(self):
        """Convert financial figures to the target currency."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")
        if not self.exchange_rates:
            raise ValueError("Exchange rates not loaded. Call `fetch_exchange_rates()` first.")

        conversion_rate = self.exchange_rates.get(self.target_currency, 1)
        self.data['Actual'] = self.data['Actual'] * conversion_rate
        self.data['Planned'] = self.data['Planned'] * conversion_rate

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
        plt.bar(self.data['Category'], self.data['Variance'],
                color=['green' if x >= 0 else 'red' for x in self.data['Variance']])
        plt.xlabel('Category')
        plt.ylabel('Variance')
        plt.title(f'Financial Variance Analysis ({self.target_currency})')
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
                plt.bar(self.data['Category'], self.data['Variance'],
                        color=['green' if x >= 0 else 'red' for x in self.data['Variance']])
                plt.xlabel('Category')
                plt.ylabel('Variance')
                plt.title(f'Financial Variance Analysis ({self.target_currency})')
                pdf.savefig()
                plt.close()
        elif format == 'excel':
            self.data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv', target_currency='EUR')
# report.load_data()
# report.fetch_exchange_rates()
# report.convert_currency()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')