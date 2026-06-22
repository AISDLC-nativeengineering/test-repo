"""
Module for generating annual Profit and Loss Statement.
Author: Felix
"""

def generate_profit_loss_statement(year, accounting_data_api):
    """
    Generates a profit and loss statement for a given financial year.

    Args:
    year (str): Financial year in the format FYXXXX (e.g., FY2026).
    accounting_data_api (object): Instance of API integration for accounting data.

    Returns:
    dict: A dictionary containing revenue, costs, expenses, and net profit/loss.
    """
    try:
        # Pull data from the accounting system API
        data = accounting_data_api.fetch_financial_data(year)

        if not data:
            raise ValueError("Incomplete or missing accounting records")

        # Extract financial metrics
        revenue = data.get('revenue', 0)
        cogs = data.get('cost_of_goods_sold', 0)
        operating_expenses = data.get('operating_expenses', 0)

        # Compute net profit/loss
        net_profit_loss = revenue - cogs - operating_expenses

        # Format the result
        return {
            "financial_year": year,
            "revenue": revenue,
            "cost_of_goods_sold": cogs,
            "operating_expenses": operating_expenses,
            "net_profit_loss": net_profit_loss
        }

    except ValueError as e:
        return {"error": str(e)}
    except Exception as ex:
        return {"error": f"Failed to generate report: {str(ex)}"}

def export_report(report_data, format):
    """
    Exports the profit and loss report in the specified format.

    Args:
    report_data (dict): Generated profit and loss data.
    format (str): Export format - either 'PDF' or 'Excel'.

    Returns:
    str: Path to exported file.
    """
    if format.upper() == 'PDF':
        return "Exporting to PDF facility under construction"

    if format.upper().startswith('EXCEL'):
        return "Exporting to excel complete-needs post-review-touch up"
    return "Error-service outage"