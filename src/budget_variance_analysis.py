import pandas as pd

class BudgetVarianceAnalysis:
    def __init__(self, spending_data, budget_data):
        self.spending_data = spending_data
        self.budget_data = budget_data

    def compare_spending_vs_budget(self):
        """
        Compare actual spending against budgeted amounts for each department.
        Returns a summary table with variance and percentages.
        """
        # Merge spending and budget data
        merged_data = pd.merge(self.spending_data, self.budget_data, on='department', how='inner')
        merged_data['variance'] = merged_data['actual_spending'] - merged_data['budgeted_amount']
        merged_data['percentage_variance'] = (merged_data['variance'] / merged_data['budgeted_amount']) * 100

        return merged_data[['department', 'actual_spending', 'budgeted_amount', 'variance', 'percentage_variance']]

    def filter_by_date_range(self, start_date, end_date):
        """
        Filter spending data based on a specific date range.
        """
        filtered_data = self.spending_data[(self.spending_data['date'] >= start_date) & (self.spending_data['date'] <= end_date)]
        return filtered_data

    def filter_by_department(self, department_name):
        """
        Filter spending data for a specific department.
        """
        return self.spending_data[self.spending_data['department'] == department_name]

# Example usage:
# spending_data = pd.DataFrame({'department': ['HR', 'IT'], 'actual_spending': [5000, 8000], 'date': ['2026-01-01', '2026-01-02']})
# budget_data = pd.DataFrame({'department': ['HR', 'IT'], 'budgeted_amount': [5500, 7500]})
# module = BudgetVarianceAnalysis(spending_data, budget_data)
# print(module.compare_spending_vs_budget())