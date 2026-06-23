import pandas as pd
from fpdf import FPDF

class ReportGenerator:
    def __init__(self, api_client):
        self.api_client = api_client

    def fetch_data(self, financial_year):
        """Fetch financial data from the accounting API for the given fiscal year."""
        response = self.api_client.get_data(financial_year)
        if not response['success']:
            raise Exception("Incomplete accounting data detected.")
        return response['data']

    def generate_report(self, data):
        """Generate profit and loss statement."""
        df = pd.DataFrame(data)
        revenue = df['revenue'].sum()
        cost_of_goods_sold = df['cost_of_goods_sold'].sum()
        operating_expenses = df['operating_expenses'].sum()
        net_profit = revenue - cost_of_goods_sold - operating_expenses

        return {
            "Revenue": revenue,
            "Cost of Goods Sold": cost_of_goods_sold,
            "Operating Expenses": operating_expenses,
            "Net Profit": net_profit
        }

    def export_to_pdf(self, report_data, file_name):
        """Export report to a PDF file."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Annual Profit and Loss Statement", ln=True, align='C')
        pdf.ln(10)

        for key, value in report_data.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

        pdf.output(file_name)

    def export_to_excel(self, report_data, file_name):
        """Export report to an Excel file."""
        df = pd.DataFrame([report_data])
        df.to_excel(file_name, index=False)
