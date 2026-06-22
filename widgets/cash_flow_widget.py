"""
Real-Time Cash Flow Widget Implementation
Author: Felix
"""

class CashFlowWidget:
    def __init__(self, api_client):
        """
        Initialize the CashFlowWidget with an API client.

        Args:
        api_client (object): API client for retrieving cash flow data.
        """
        self.api_client = api_client

    def fetch_cash_flow_data(self):
        """
        Fetch the latest cash flow data from the accounting system API.

        Returns:
        dict: Contains current cash flow and trend details.
        """
        try:
            data = self.api_client.get_cash_flow()
            if 'cash_flow' not in data or 'trend' not in data:
                raise ValueError("Incomplete data received from API")
            return data
        except Exception as e:
            return {"error": f"Failed to fetch cash flow data: {str(e)}"}

    def render_widget(self, cash_flow_data):
        """
        Render the widget based on cash flow data.

        Args:
        cash_flow_data (dict): Cash flow data to display.

        Returns:
        str: Rendered widget as a string.
        """
        try:
            cash_flow = cash_flow_data['cash_flow']
            trend = cash_flow_data['trend']

            indicator_color = "green" if trend > 0 else "red"
            trend_icon = "↑" if trend > 0 else "↓"

            return (
                f"Cash Flow: {cash_flow} ({indicator_color})\n"
                f"Trend: {trend}% {trend_icon}"
            )
        except KeyError:
            return "Error: Missing data fields for rendering widget"
        except Exception as e:
            return f"Error: Failed to render widget: {str(e)}"