import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

class FinancialReport:
    def __init__(self, dataset_path, stakeholders):
        self.dataset_path = dataset_path
        self.data = None
        self.stakeholders = stakeholders

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

    def send_email(self):
        """
        Send financial report email to stakeholders.
        """
        try:
            report_path = "financial_report.pdf"
            self.export_report(output_path=report_path)

            sender_email = "your_email@example.com"
            sender_password = "your_password"

            for recipient_email in self.stakeholders:
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = recipient_email
                message['Subject'] = "Monthly Financial Report"

                body = "Please find attached the monthly financial report."
                message.attach(MIMEText(body, 'plain'))

                attachment = open(report_path, 'rb')
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(report_path)}")
                message.attach(part)
                attachment.close()

                # Connect to server and send email
                server = smtplib.SMTP('smtp.example.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                text = message.as_string()
                server.sendmail(sender_email, recipient_email, text)
                server.quit()

        except Exception as e:
            print(f"Error sending email: {e}")
            raise

    @staticmethod
    def is_first_business_day():
        """Checks if today is the first business day of the month."""
        today = datetime.today()
        first_day = today.replace(day=1)
        return today.weekday() < 5 and today.day == first_day.day


# Scheduler setup
scheduler = BackgroundScheduler()
def scheduled_job():
    try:
        if FinancialReport.is_first_business_day():
            report = FinancialReport(dataset_path='financial_data.csv', stakeholders=['stakeholder1@example.com', 'stakeholder2@example.com'])
            report.load_data()
            report.compute_variance()
            report.send_email()

    except Exception as err:
        print(f"Scheduled job error: {err}")

scheduler.add_job(scheduled_job, 'cron', day='1')  # Adjust cron for first business day
scheduler.start()

# Example usage
# report = FinancialReport(dataset_path='financial_data.csv', stakeholders=['example@example.com'])
# report.load_data()
# report.compute_variance()
# report.send_email()