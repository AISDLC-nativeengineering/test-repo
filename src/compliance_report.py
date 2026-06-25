# compliance_report.py
# Module to generate compliance reports for auditors

import csv
from fpdf import FPDF

class ComplianceReport:
    """Generates compliance reports including logs, histories, and user permissions."""

    def __init__(self, data):
        self.data = data  # Data should be a dictionary containing report content

    def generate_csv(self, file_path):
        """Generate the report in CSV format."""
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.data.keys())  # Write header
                writer.writerow(self.data.values())  # Write data
            print(f"CSV report created at: {file_path}")
        except Exception as e:
            print(f"Error generating CSV: {e}")

    def generate_pdf(self, file_path):
        """Generate the report in PDF format."""
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Compliance Report", ln=True, align='C')
            for key, value in self.data.items():
                pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
            pdf.output(file_path)
            print(f"PDF report created at: {file_path}")
        except Exception as e:
            print(f"Error generating PDF: {e}")

# Example usage:
if __name__ == "__main__":
    sample_data = {
        "Access Logs": "Details about access logs...",
        "Change History": "Details about change history...",
        "User Permissions": "Details about user permissions..."
    }
    report = ComplianceReport(data=sample_data)
    report.generate_csv("compliance_report.csv")
    report.generate_pdf("compliance_report.pdf")