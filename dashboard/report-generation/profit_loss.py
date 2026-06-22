# Profit and Loss Statement Generation Module

# Module to integrate accounting API, generate P&L statement and export it

import accounting_api
import pdf_exporter
import excel_exporter

class ProfitLossStatementGenerator:
    def __init__(self):
        self.data_sources = {}  # Initialize accounting data sources

    def retrieve_accounting_data(self, financial_year):
        """
        Retrieves accounting data for the given financial year.
        Args:
            financial_year (str): Financial year (e.g., FY2026)

        Returns:
            dict: Accounting data including revenue, expenses, and net profit
        """
        try:
            self.data_sources = accounting_api.get_financial_data(financial_year)
        except Exception as e:
            raise ValueError(f"Failed to retrieve accounting data: {str(e)}")
        return self.data_sources

    def generate_report(self):
        """
        Processes accounting data and generates profit and loss report

        Returns:
            dict: Profit and loss summary including revenue breakdown, expenses, and net profit
        """
        if not self.data_sources:
            raise ValueError("Accounting data is incomplete.")

        revenue = sum(self.data_sources.get("revenue", {}).values())
        expenses = sum(self.data_sources.get("expenses", {}).values())
        net_profit_loss = revenue - expenses

        return {
            "revenue": revenue,
            "expenses": expenses,
            "net_profit_loss": net_profit_loss
        }

    def export(self, report, format):
        """
        Exports report in the requested format
        Args:
            report (dict): Generated report data
            format (str): 'PDF' or 'Excel'

        Returns:
            None
        """
        if format == "PDF":
            pdf_exporter.export_to_pdf(report)
        elif format == "Excel":
            excel_exporter.export_to_excel(report)
        else:
            raise ValueError("Invalid format. Supported formats are PDF and Excel.")

# Example usage
if __name__ == "__main__":
    financial_year = "FY2026"
    generator = ProfitLossStatementGenerator()

    try:
        data = generator.retrieve_accounting_data(financial_year)
        report = generator.generate_report()
        generator.export(report, "PDF")
        generator.export(report, "Excel")
        print("Reports exported successfully!")
    except Exception as e:
        print(f"Error: {e}")