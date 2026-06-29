# Variance Threshold Module

"""
This module allows administrators to set variance thresholds either globally or per department. 
Thresholds can be defined as a percentage or an absolute value.

Global thresholds apply to all departments.
Specific thresholds can be customized per department.

"""

def set_thresholds(global_percentage_threshold=None, global_absolute_threshold=None, department_thresholds=None):
    """
    Function to configure variance thresholds.

    Parameters:
        global_percentage_threshold (float): The percentage threshold for global variances.
        global_absolute_threshold (float): The absolute value threshold for global variances.
        department_thresholds (dict): A dictionary mapping departments to their thresholds.
                                      Each value can be a dict with keys 'percentage' and 'absolute'.

    Returns:
        dict: The applied threshold configuration.

    """
    thresholds = {}

    # Handle global thresholds
    if global_percentage_threshold is not None:
        thresholds['global_percentage'] = global_percentage_threshold
    if global_absolute_threshold is not None:
        thresholds['global_absolute'] = global_absolute_threshold

    # Handle department-specific thresholds
    if department_thresholds:
        thresholds['departments'] = {}
        for department, department_values in department_thresholds.items():
            thresholds['departments'][department] = {
                'percentage': department_values.get('percentage'),
                'absolute': department_values.get('absolute')
            }

    return thresholds

# Example usage
if __name__ == "__main__":
    config = set_thresholds(
        global_percentage_threshold=10.0,
        global_absolute_threshold=10000.0,
        department_thresholds={
            'HR': {'percentage': 5.0, 'absolute': 5000.0},
            'IT': {'percentage': 15.0, 'absolute': 20000.0}
        }
    )
    print("Threshold configuration:", config)
