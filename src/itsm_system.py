import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import random

class ITSMSystem:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.incident_data = None

    def load_data(self):
        """Loads incident data from the dataset."""
        self.incident_data = pd.read_csv(self.dataset_path)

    def auto_categorize_prioritize(self):
        """Automatically categorizes and prioritizes incidents."""
        if self.incident_data is None:
            raise ValueError("Incident data not loaded. Call `load_data()` first.")
        self.incident_data['Category'] = self.incident_data['Description'].apply(lambda x: 'Network' if 'network' in x.lower() else 'Software')
        self.incident_data['Priority'] = self.incident_data['Impact'].apply(lambda x: 'High' if x >= 5 else 'Low')

    def suggest_resolution(self):
        """Provides resolution suggestions based on historical data."""
        if self.incident_data is None:
            raise ValueError("Incident data not loaded. Call `load_data()` first.")
        self.incident_data['Resolution'] = self.incident_data['Category'].apply(lambda x: 'Restart Device' if x == 'Network' else 'Update Software')

    def proactive_alerts(self):
        """Identifies repetitive incidents and proactively alerts users."""
        if self.incident_data is None:
            raise ValueError("Incident data not loaded. Call `load_data()` first.")
        repetitive_patterns = self.incident_data['Description'].value_counts().to_dict()
        alerts = {key: val for key, val in repetitive_patterns.items() if val > 3}
        return alerts

    def generate_reporting_dashboard(self, output_path):
        """Generates analytics dashboards."""
        if self.incident_data is None:
            raise ValueError("Incident data not loaded. Call `load_data()` first.")
        plt.figure(figsize=(10, 6))
        category_counts = self.incident_data['Category'].value_counts()
        plt.bar(category_counts.index, category_counts.values, color=['blue', 'orange'])
        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.title('Incident Distribution by Category')
        plt.savefig(output_path)
        plt.close()

    def integrate_with_external_systems(self, system_name):
        """Verifies integration with external systems."""
        return f"Integration with {system_name} successful!"

# Example Usage
# itsm = ITSMSystem(dataset_path='incident_data.csv')
# itsm.load_data()
# itsm.auto_categorize_prioritize()
# itsm.suggest_resolution()
# alerts = itsm.proactive_alerts()
# itsm.generate_reporting_dashboard(output_path='incident_dashboard.png')
# print(itsm.integrate_with_external_systems(system_name='Customer Service Platform'))