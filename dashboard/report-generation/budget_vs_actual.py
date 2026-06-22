# Budget vs Actual Comparison Report Module

# Required modules for data integration and exporting reports
import accounting_api
import pdf_exporter
import excel_exporter

class BudgetVsActualReport:
    def __init__(self):
        self.budget_data = {}
        self.actual_data = {}

    def retrieve_data(self, fiscal_period, department=None):
        """
        Retrieves budget and actual data for the given fiscal period and department.

        Args:
            fiscal_period (str): Fiscal period (e.g., 'Q1 2026')
            department (str, optional): Department name

        Returns:
            dict: Budget and actual data
        """
        try:
            self.budget_data = accounting_api.get_budget_data(fiscal_period, department)
            self.actual_data = accounting_api.get_actual_data(fiscal_period, department)
        except Exception as e:
            raise ValueError(f"Failed to retrieve data: {str(e)}")

        return {
            "budget": self.budget_data,
            "actual": self.actual_data
        }

    def generate_comparison_report(self):
        """
        Generates comparison report showing budget, actual, and variance.

        Returns:
            dict: Comparison data including variances
        """
        if not self.budget_data or not self.actual_data:
            raise ValueError("Incomplete data for report generation.")

        comparison = {}
        for item, budget_value in self.budget_data.items():
            actual_value = self.actual_data.get(item, 0)
            variance = actual_value - budget_value
            comparison[item] = {
                "budget": budget_value,
                "actual": actual_value,
                "variance": variance
            }

        return comparison

    def export(self, report, format):
        """
        Exports the generated report in the requested format.

        Args:
            report (dict): Generated comparison report data
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
    fiscal_period = "Q1 2026"
    department = "Sales"
    report_generator = BudgetVsActualReport()

    try:
        data = report_generator.retrieve_data(fiscal_period, department)
        comparison_report = report_generator.generate_comparison_report()
        report_generator.export(comparison_report, "PDF")
        report_generator.export(comparison_report, "Excel")
        print("Reports exported successfully!")
    except Exception as e:
        print(f"Error: {e}")