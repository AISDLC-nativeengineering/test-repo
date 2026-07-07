import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import logging  # Added for session logging

# Configure logging
logging.basicConfig(
    filename="session.log",
    level=logging.INFO,
    format="%(asctime)s - USER_ID: %(message)s"
)

class FinancialReport:
    def __init__(self, dataset_path, user_id):  # Added user_id parameter
        self.dataset_path = dataset_path
        self.user_id = user_id  # Store user_id
        self.data = None
        self.log_session_initiation()  # Log session initiation

    def log_session_initiation(self):
        """Logs the initiation of a user session accessing the reporting module."""
        logging.info(f"Reporting module accessed by user {self.user_id}")

    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)

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
        plt.bar(
            self.data['Category'],
            self.data['Variance'],
            color=['green' if x >= 0 else 'red' for x in self.data['Variance']]
        )
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
                plt.bar(
                    self.data['Category'],
                    self.data['Variance'],
                    color=['green' if x >= 0 else 'red' for x in self.data['Variance']]
                )
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
# report = FinancialReport(dataset_path='financial_data.csv', user_id='USER123')
# report.load_data()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png')
# report.export_report(format='pdf', output_path='financial_report.pdf')