# src/export_reports.py

import os
from fpdf import FPDF
import xlsxwriter

class ReportExporter:
    def __init__(self, company_logo=None, headers=None):
        self.company_logo = company_logo
        self.headers = headers or {}

    def export_to_pdf(self, report_data, output_file):
        pdf = FPDF()
        pdf.add_page()

        # Add company logo
        if self.company_logo and os.path.exists(self.company_logo):
            pdf.image(self.company_logo, x=10, y=8, w=30)

        # Add customizable headers
        pdf.set_font('Arial', 'B', 16)
        for header, value in self.headers.items():
            pdf.cell(0, 10, f'{header}: {value}', ln=True)

        # Add report data
        pdf.set_font('Arial', '', 12)
        for line in report_data:
            pdf.cell(0, 10, line, ln=True)

        pdf.output(output_file)

    def export_to_excel(self, report_data, output_file):
        workbook = xlsxwriter.Workbook(output_file)
        worksheet = workbook.add_worksheet()

        # Add customizable headers
        row = 0
        col = 0
        for header, value in self.headers.items():
            worksheet.write(row, col, f'{header}: {value}')
            row += 1

        # Add report data
        for line in report_data:
            worksheet.write(row, col, line)
            row += 1

        workbook.close()

# Usage Example
if __name__ == '__main__':
    exporter = ReportExporter(
        company_logo='path/to/logo.png',
        headers={'Title': 'Year-End Report', 'Date': '2023-12-31'}
    )
    sample_data = ['Revenue: $1,000,000', 'Expenses: $500,000']

    # Export PDF
    exporter.export_to_pdf(sample_data, 'financial_report.pdf')

    # Export Excel
    exporter.export_to_excel(sample_data, 'financial_report.xlsx')