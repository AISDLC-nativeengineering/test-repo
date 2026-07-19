import schedule
import time
from datetime import datetime
from src.financial_report import FinancialReport

# Constants for scheduling
DATA_PATH = "data/financial_data.csv"
DEFAULT_FORMAT = "pdf"
OUTPUT_PATH = "output/financial_report.{}"
EMAIL_RECIPIENTS = ["stakeholder1@example.com", "stakeholder2@example.com"]

# Function to send emails with reports
def send_email(recipients, report_path):
    # Dummy email integration - replace with actual implementation
    print(f"Sending email to {recipients} with attachment: {report_path}")

# Job to generate and email financial report
def generate_and_email_report():
    try:
        print("Starting scheduled financial report generation.")
        # Initialize financial report
        report = FinancialReport(dataset_path=DATA_PATH)
        report.load_data()
        report.compute_variance()
        # Export report
        output_path = OUTPUT_PATH.format(DEFAULT_FORMAT)
        report.export_report(format=DEFAULT_FORMAT, output_path=output_path)
        # Send email
        send_email(recipients=EMAIL_RECIPIENTS, report_path=output_path)
        print("Email dispatched successfully.")
    except Exception as e:
        print(f"Error during report generation or emailing: {str(e)}")

# Utility to find first business day of the month
def first_business_day():
    today = datetime.now()
    first_day = datetime(today.year, today.month, 1)
    while first_day.weekday() >= 5:  # Skip weekends
        first_day = first_day + timedelta(days=1)
    return first_day

# Schedule the job for first business day of next month
schedule.every().month.at("00:00").do(generate_and_email_report)

print("Scheduled task initialized.")

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)