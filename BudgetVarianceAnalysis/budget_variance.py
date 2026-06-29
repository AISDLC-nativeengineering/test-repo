import datetime

class BudgetVariance:
    def __init__(self, threshold_percentage, threshold_absolute):
        """
        Initialize thresholds for flagging significant budget variances.
        :param threshold_percentage: Allowed percentage deviation from budget
        :param threshold_absolute: Allowed absolute deviation from budget
        """
        self.threshold_percentage = threshold_percentage
        self.threshold_absolute = threshold_absolute

    def flag_variance(self, department, budget, actual_spending):
        """
        Flags significant variances based on thresholds.
        :param department: Name of the department
        :param budget: Budgeted amount
        :param actual_spending: Actual amount spent
        :return: Dictionary containing flag details
        """
        absolute_variance = actual_spending - budget
        percentage_variance = ((actual_spending - budget) / budget) * 100 if budget else 0

        severity = None
        if percentage_variance > self.threshold_percentage:
            severity = "high"
        elif absolute_variance > self.threshold_absolute:
            severity = "moderate"
        
        if severity:
            return {
                "department": department,
                "flagged_at": datetime.datetime.now().isoformat(),
                "budgeted": budget,
                "actual": actual_spending,
                "absolute_variance": absolute_variance,
                "percentage_variance": percentage_variance,
                "severity": severity,
            }

        return None

# Example Usage
if __name__ == "__main__":
    variance_checker = BudgetVariance(threshold_percentage=10, threshold_absolute=5000)
    result = variance_checker.flag_variance(
        department="Marketing", budget=50000, actual_spending=60000
    )
    
    if result:
        print("Flagged Variance:", result)
    else:
        print("No significant variance detected.")