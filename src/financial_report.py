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

    def filter_data(self, department=None, start_date=None, end_date=None):
        """Filters data by department and date range."""
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

    def compute_variance(self):
        """Computes variance between planned and actual financial figures."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")
        self.data['Variance'] = self.data['Actual'] - self.data['Planned']

    def generate_visualization(self, output_path, department=None, start_date=None, end_date=None):
        """Generate graphs or charts to visualize the variance."""
        if self.data is None or 'Variance' not in self.data.columns:
            raise ValueError("Variance not computed. Call `compute_variance()` first.")

        filtered_data = self.filter_data(department, start_date, end_date)

        plt.figure(figsize=(10, 6))
        plt.bar(filtered_data['Category'], filtered_data['Variance'], 
                color=['green' if x >= 0 else 'red' for x in filtered_data['Variance']])
        plt.xlabel('Category')
        plt.ylabel('Variance')
        plt.title('Financial Variance Analysis')
        plt.savefig(output_path)
        plt.close()

    def export_report(self, format='pdf', output_path='financial_report.pdf', department=None, start_date=None, end_date=None):
        """Export the report in specified format (PDF or Excel)."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        filtered_data = self.filter_data(department, start_date, end_date)

        if format == 'pdf':
            # Export visualization as part of PDF report
            from matplotlib.backends.backend_pdf import PdfPages
            with PdfPages(output_path) as pdf:
                plt.figure(figsize=(10, 6))
                plt.bar(filtered_data['Category'], filtered_data['Variance'], 
                        color=['green' if x >= 0 else 'red' for x in filtered_data['Variance']])
                plt.xlabel('Category')
                plt.ylabel('Variance')
                plt.title('Financial Variance Analysis')
                pdf.savefig()  # Save plot to PDF
                plt.close()
        elif format == 'excel':
            filtered_data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv')
# report.load_data()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')