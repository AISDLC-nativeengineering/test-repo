import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime

class FinancialReport:
    def __init__(self, dataset_path, base_currency='USD', exchange_api_key=None):
        self.dataset_path = dataset_path
        self.base_currency = base_currency
        self.exchange_api_key = exchange_api_key
        self.data = None

    def fetch_exchange_rates(self):
        """Fetches real-time exchange rates."""
        if not self.exchange_api_key:
            raise ValueError("Exchange API key is required.")

        try:
            response = requests.get(
                f"https://openexchangerates.org/api/latest.json",
                params={"app_id": self.exchange_api_key}
            )
            response.raise_for_status()
            return response.json()["rates"]
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch exchange rates: {e}")
            return {}

    def load_data(self):
        """Loads financial data and converts currency based on real-time rates."""
        self.data = pd.read_csv(self.dataset_path)

        # Ensure 'Currency' and 'Amount' columns exist
        if 'Currency' not in self.data.columns or 'Amount' not in self.data.columns:
            raise ValueError("Dataset must contain 'Currency' and 'Amount' columns.")

        # Fetch exchange rates and convert to base currency
        rates = self.fetch_exchange_rates()
        if rates:
            self.data['Amount_Base_Currency'] = self.data.apply(
                lambda row: row['Amount'] / rates.get(row['Currency'], 1)
                if row['Currency'] != self.base_currency else row['Amount'], axis=1
            )
        else:
            self.data['Amount_Base_Currency'] = self.data['Amount']

    def compute_variance(self):
        """Computes variance between planned and actual financial figures in base currency."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        if 'Planned_Base_Currency' not in self.data.columns or 'Actual_Base_Currency' not in self.data.columns:
            raise ValueError("Dataset must contain 'Planned_Base_Currency' and 'Actual_Base_Currency' columns.")

        self.data['Variance'] = self.data['Actual_Base_Currency'] - self.data['Planned_Base_Currency']

    def generate_visualization(self, output_path):
        """Generate graphs or charts to visualize the variance."""
        if self.data is None or 'Variance' not in self.data.columns:
            raise ValueError("Variance not computed. Call `compute_variance()` first.")

        plt.figure(figsize=(10, 6))
        plt.bar(
            self.data['Category'], self.data['Variance'],
            color=['green' if x >= 0 else 'red' for x in self.data['Variance']]
        )
        plt.xlabel('Category')
        plt.ylabel('Variance (Base Currency)')
        plt.title('Financial Variance Analysis')
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
                plt.bar(
                    self.data['Category'], self.data['Variance'],
                    color=['green' if x >= 0 else 'red' for x in self.data['Variance']]
                )
                plt.xlabel('Category')
                plt.ylabel('Variance (Base Currency)')
                plt.title('Financial Variance Analysis')
                pdf.savefig()
                plt.close()
        elif format == 'excel':
            self.data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv', base_currency='USD', exchange_api_key='your_api_key')
# report.load_data()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')