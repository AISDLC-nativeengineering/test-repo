import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class FinancialReport:
    def __init__(self, dataset_path, base_currency):
        self.dataset_path = dataset_path
        self.base_currency = base_currency
        self.data = None
        self.exchange_rates = {}

    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)
        if 'Currency' not in self.data.columns:
            raise ValueError("Dataset must include 'Currency' column.")

    def set_exchange_rates(self, rates):
        """Sets exchange rates for currency conversion."""
        self.exchange_rates = rates

    def convert_to_base_currency(self):
        """Converts financial figures to the base currency."""
        if not self.exchange_rates:
            raise ValueError("Exchange rates not set. Call `set_exchange_rates()` first.")
        
        if 'Currency' not in self.data.columns:
            raise ValueError("Currency column missing in the dataset.")

        def convert(row):
            rate = self.exchange_rates.get(row['Currency'])
            if rate is None:
                raise ValueError(f"Missing exchange rate for {row['Currency']}")
            row['Actual'] = row['Actual'] * rate
            row['Planned'] = row['Planned'] * rate
            return row
        
        self.data = self.data.apply(convert, axis=1)

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
            from matplotlib.backends.backend_pdf import PdfPages
            with PdfPages(output_path) as pdf:
                plt.figure(figsize=(10, 6))
                plt.bar(self.data['Category'], self.data['Variance'], color=['green' if x >= 0 else 'red' for x in self.data['Variance']])
                plt.xlabel('Category')
                plt.ylabel('Variance')
                plt.title(f'Financial Variance Analysis (Base Currency: {self.base_currency})')
                pdf.savefig()
                plt.close()
        elif format == 'excel':
            self.data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv', base_currency='USD')
# report.load_data()
# report.set_exchange_rates({'USD': 1, 'EUR': 0.85, 'JPY': 110})
# report.convert_to_base_currency()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')