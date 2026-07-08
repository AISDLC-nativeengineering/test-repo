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

    def verify_data_integrity(self):
        """Checks data integrity for actual and budgeted amounts."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        required_columns = ['Department', 'Actual', 'Budgeted', 'Date']
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}.")

    def filter_data(self, department=None, start_date=None, end_date=None):
        """Filters data by department and date range."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")

        filtered_data = self.data

        if department:
            filtered_data = filtered_data[filtered_data['Department'] == department]

        if start_date and end_date:
            filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])
            filtered_data = filtered_data[(filtered_data['Date'] >= pd.to_datetime(start_date)) & (filtered_data['Date'] <= pd.to_datetime(end_date))]

        self.filtered_data = filtered_data

    def compute_variance(self):
        """Computes variance between budgeted and actual financial figures."""
        if self.filtered_data is None:
            raise ValueError("Filtered data not set. Call `filter_data()` first.")

        self.filtered_data['Variance'] = self.filtered_data['Actual'] - self.filtered_data['Budgeted']

    def generate_visualization(self, output_path):
        """Generate graphs or charts to visualize the variance."""
        if self.filtered_data is None or 'Variance' not in self.filtered_data.columns:
            raise ValueError("Variance not computed. Call `compute_variance()` first.")
        
        plt.figure(figsize=(10, 6))
        plt.bar(self.filtered_data['Department'], 
                self.filtered_data['Variance'], 
                color=['green' if x >= 0 else 'red' for x in self.filtered_data['Variance']])
        
        plt.xlabel('Department')
        plt.ylabel('Variance')
        plt.title('Budget Variance Analysis')
        plt.savefig(output_path)
        plt.close()

    def export_report(self, format='pdf', output_path='financial_report.pdf'):
        """Export the report in specified format (PDF or Excel)."""
        if self.filtered_data is None:
            raise ValueError("Filtered data not set. Call `filter_data()` first.")

        if format == 'pdf':
            from matplotlib.backends.backend_pdf import PdfPages
            with PdfPages(output_path) as pdf:
                plt.figure(figsize=(10, 6))
                plt.bar(self.filtered_data['Department'], 
                        self.filtered_data['Variance'], 
                        color=['green' if x >= 0 else 'red' for x in self.filtered_data['Variance']])
                plt.xlabel('Department')
                plt.ylabel('Variance')
                plt.title('Budget Variance Analysis')
                pdf.savefig()  # Save plot to PDF
                plt.close()
        elif format == 'excel':
            self.filtered_data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")