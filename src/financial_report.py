import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from calendar import monthrange
import logging

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
                plt.title('Financial Variance Analysis')
                pdf.savefig()  # Save plot to PDF
                plt.close()
        elif format == 'excel':
            self.data.to_excel(output_path, index=False)
        else:
            raise ValueError("Unsupported format. Use 'pdf' or 'excel'.")

    def send_email(self, recipients, attachment_path):
        """Send email with the financial report attachment."""
        try:
            sender = "no-reply@example.com"
            subject = "Monthly Financial Report"
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = ", ".join(recipients)
            msg['Subject'] = subject

            body = "Please find the monthly financial report attached."
            msg.attach(MIMEText(body, 'plain'))

            attachment = open(attachment_path, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={attachment_path}")
            msg.attach(part)

            # Example SMTP setup (adjust as needed)
            server = smtplib.SMTP('smtp.example.com', 587)
            server.starttls()
            server.login(sender, "password")
            server.sendmail(sender, recipients, msg.as_string())
            server.quit()
            attachment.close()
            logging.info("Email sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

    def schedule_report(self, recipients):
        """Schedule monthly financial report generation and delivery."""
        try:
            today = datetime.today()
            first_day, last_day = monthrange(today.year, today.month)
            first_business_day = datetime(today.year, today.month, first_day)

            # Adjust for weekends (example logic)
            if first_business_day.weekday() in [5, 6]:
                first_business_day += timedelta(days=7 - first_business_day.weekday())

            if today.date() == first_business_day.date():
                self.load_data()
                self.compute_variance()
                output_path = 'financial_report.pdf'
                self.export_report(output_path=output_path)
                self.send_email(recipients=recipients, attachment_path=output_path)
                logging.info("Financial report generated and emailed successfully.")
        except Exception as e:
            logging.error(f"Error in scheduling monthly financial report: {e}")

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    report = FinancialReport(dataset_path='financial_data.csv')
    recipients = ["stakeholder1@example.com", "stakeholder2@example.com"]
    report.schedule_report(recipients=recipients)