import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class FinancialReport:
    def __init__(self, dataset_path, api_url):
        self.dataset_path = dataset_path
        self.api_url = api_url
        self.data = None

    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)

    def fetch_exchange_rate(self, from_currency, to_currency, date=None):
        """Fetch exchange rates from external API."""
        try:
            params = {"base": from_currency, "symbols": to_currency}
            if date:
                api_endpoint = f"{self.api_url}/{date}"
            else:
                api_endpoint = self.api_url

            response = requests.get(api_endpoint, params=params)
            response.raise_for_status()
            return response.json()['rates'][to_currency]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
            return None

    def compute_variance_with_conversion(self, from_currency, to_currency, date=None):
        """Computes variance with currency conversion."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        exchange_rate = self.fetch_exchange_rate(from_currency, to_currency, date=date)
        if exchange_rate is None:
            print("Using fallback conversion rate: 1")
            exchange_rate = 1  # Fallback mechanism

        self.data['Converted_Planned'] = self.data['Planned'] * exchange_rate
        self.data['Converted_Actual'] = self.data['Actual'] * exchange_rate
        self.data['Variance'] = self.data['Converted_Actual'] - self.data['Converted_Planned']

    def generate_visualization(self, output_path):
        """Generate graphs or charts to visualize the variance."""
        if self.data is None or 'Variance' not in self.data.columns:
            raise ValueError("Variance not computed. Call `compute_variance_with_conversion()` first.")
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
# report = FinancialReport(dataset_path='financial_data.csv', api_url='https://example.com/api/exchange_rates')
# report.load_data()
# report.compute_variance_with_conversion(from_currency='USD', to_currency='EUR', date='2023-01-01')
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')
