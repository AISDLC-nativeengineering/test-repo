import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class FinancialReport:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = None

    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)

    def compute_variance(self):
        """Computes variance between planned and actual financial figures."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")
        self.data['Variance'] = self.data['Actual'] - self.data['Planned']

    def filter_data(self, department=None, start_date=None, end_date=None):
        """Filter data based on department and date range."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        filtered_data = self.data

        if department:
            filtered_data = filtered_data[filtered_data['Department'] == department]

        if start_date:
            filtered_data = filtered_data[filtered_data['Date'] >= start_date]

        if end_date:
            filtered_data = filtered_data[filtered_data['Date'] <= end_date]

        return filtered_data

    def generate_visualization(self, filtered_data, output_path):
        """Generate graphs or charts to visualize the variance based on filtered data."""
        if filtered_data is None or 'Variance' not in filtered_data.columns:
            raise ValueError("Variance not computed or invalid filtered data.")

        plt.figure(figsize=(10, 6))
        plt.bar(filtered_data['Category'], filtered_data['Variance'], color=['green' if x >= 0 else 'red' for x in filtered_data['Variance']])
        plt.xlabel('Category')
        plt.ylabel('Variance')
        plt.title('Filtered Financial Variance Analysis')
        plt.savefig(output_path)
        plt.close()

    def export_report(self, filtered_data, format='pdf', output_path='filtered_financial_report.pdf'):
        """Export the filtered report in specified format (PDF or Excel)."""
        if filtered_data is None:
            raise ValueError("No filtered data available to export.")

        if format == 'pdf':
            from matplotlib.backends.backend_pdf import PdfPages
            with PdfPages(output_path) as pdf:
                plt.figure(figsize=(10, 6))
                plt.bar(filtered_data['Category'], filtered_data['Variance'], color=['green' if x >= 0 else 'red' for x in filtered_data['Variance']])
                plt.xlabel('Category')
                plt.ylabel('Variance')
                plt.title('Filtered Financial Variance Analysis')
                pdf.savefig()
                plt.close()
        elif format == 'excel':
            filtered_data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv')
# report.load_data()
# report.compute_variance()
# filtered = report.filter_data(department='Sales', start_date='2026-01-01', end_date='2026-02-01')
# report.generate_visualization(filtered, output_path='filtered_variance_graph.png')
# report.export_report(filtered, format='excel', output_path='filtered_financial_report.xlsx')
