import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime

class FinancialReport:
    def __init__(self, dataset_path, primary_currency='USD', exchange_rate_api_key=None):
        self.dataset_path = dataset_path
        self.primary_currency = primary_currency
        self.exchange_rate_api_key = exchange_rate_api_key
        self.data = None
    
    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)
        if 'Currency' in self.data.columns:
            self.data['Converted_Amount'] = self.data.apply(
                lambda row: self.convert_currency(row['Amount'], row['Currency']), axis=1
            )
    
    def convert_currency(self, amount, source_currency):
        """Convert an amount from source_currency to primary_currency."""
        if source_currency == self.primary_currency:
            return amount

        url = f"https://openexchangerates.org/api/latest.json?app_id={self.exchange_rate_api_key}"
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Failed to fetch exchange rates.")

        rates = response.json()['rates']
        if source_currency not in rates or self.primary_currency not in rates:
            raise ValueError("Currency not supported.")

        rate = rates[self.primary_currency] / rates[source_currency]
        return amount * rate

    def compute_variance(self):
        """Computes variance between planned and actual financial figures."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")
        self.data['Variance'] = self.data['Converted_Actual'] - self.data['Converted_Planned']

    def generate_visualization(self, output_path):
        """Generate graphs or charts to visualize the variance."""
        if self.data is None or 'Variance' not in self.data.columns:
            raise ValueError("Variance not computed. Call `compute_variance()` first.")
        plt.figure(figsize=(10, 6))
        plt.bar(
            self.data['Category'], 
            self.data['Variance'], 
            color=['green' if x >= 0 else 'red' for x in self.data['Variance']]
        )
        plt.xlabel('Category')
        plt.ylabel('Variance')
        plt.title('Financial Variance Analysis (Converted)')
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
                plt.bar(
                    self.data['Category'], 
                    self.data['Variance'], 
                    color=['green' if x >= 0 else 'red' for x in self.data['Variance']]
                )
                plt.xlabel('Category')
                plt.ylabel('Variance')
                plt.title('Financial Variance Analysis (Converted)')
                pdf.savefig()  # Save plot to PDF
                plt.close()
        elif format == 'excel':
            self.data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv', primary_currency='USD', exchange_rate_api_key='YOUR_API_KEY')
# report.load_data()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')