import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from audit_logger import AuditLogger

class FinancialReport:
    def __init__(self, dataset_path, audit_log_path):
        self.dataset_path = dataset_path
        self.audit_logger = AuditLogger(log_file=audit_log_path)
        self.data = None

    def load_data(self):
        """Loads financial data from the dataset."""
        self.data = pd.read_csv(self.dataset_path)

    def compute_variance(self):
        """Computes variance between planned and actual financial figures."""
        if self.data is None:
            raise ValueError("Data not loaded. Call `load_data()` first.")
        self.data['Variance'] = self.data['Actual'] - self.data['Planned']

    def generate_visualization(self, output_path, report_name, user):
        """Generate graphs or charts to visualize the variance and log the action."""
        if self.data is None or 'Variance' not in self.data.columns:
            raise ValueError("Variance not computed. Call `compute_variance()` first.")
        plt.figure(figsize=(10, 6))
        plt.bar(self.data['Category'], self.data['Variance'], color=['green' if x >= 0 else 'red' for x in self.data['Variance']])
        plt.xlabel('Category')
        plt.ylabel('Variance')
        plt.title('Financial Variance Analysis')
        plt.savefig(output_path)
        plt.close()

        # Log report generation
        self.audit_logger.log_report_generation(report_name=report_name, user=user)

    def export_report(self, format='pdf', output_path='financial_report.pdf', user='unknown'):        
        """Export the report in specified format (PDF or Excel) and log the action."""
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

        # Log data export
        self.audit_logger.log_data_export(file_type=format, destination=output_path, user=user)

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv', audit_log_path='audit.log')
# report.load_data()
# report.compute_variance()
# report.generate_visualization(output_path='variance_graph.png', report_name='Monthly Financial Report', user='admin')
# report.export_report(format='pdf', output_path='financial_report.pdf', user='admin')