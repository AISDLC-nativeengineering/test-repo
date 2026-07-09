# Sustainability Report

## Overview
This module generates sustainability reports based on energy consumption data. It summarizes energy savings, employee satisfaction improvements, and carbon footprint reductions.

## Features
- Summarize metrics by KPI category.
- Export reports in PDF and Excel formats.
- Filter data by custom date range.

## Implementation

### Functionality
```python
import pandas as pd
from fpdf import FPDF  # For generating PDF reports

class SustainabilityReport:

    def __init__(self, data):
        """
        Initialize report with data.
        :param data: Dictionary containing energy metrics.
        """
        self.data = data

    def summarize_kpi(self, category):
        """
        Summarize metrics for the given KPI category.
        :param category: KPI category.
        :return: Summary dictionary.
        """
        try:
            return self.data.get(category, {})
        except KeyError:
            raise ValueError(f"Category {category} not found.")

    def export_pdf(self, summary, filename):
        """
        Export summary to PDF file.
        :param summary: Summary dictionary.
        :param filename: File name to save the report.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.cell(200, 10, txt="Sustainability Report", ln=1, align='C')

        for key, value in summary.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=2, align='L')

        pdf.output(filename)

    def export_excel(self, summary, filename):
        """
        Export summary to Excel file.
        :param summary: Summary dictionary.
        :param filename: File name to save the report.
        """
        df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
        df.to_excel(filename, index=False)

# Example Usage:
data_metrics = {
    "Energy Savings": {"January": 1200, "February": 1400},
    "Carbon Footprint Reduction": {"January": 200, "February": 250}
}

report = SustainabilityReport(data_metrics)
summary = report.summarize_kpi("Energy Savings")
report.export_pdf(summary, "energy_report.pdf")
report.export_excel(summary, "energy_report.xlsx")
```

### API Contracts
- **Input:**
  - KPI category (string).
  - Date range (start_date, end_date).
- **Output:**
  - Dictionary containing summarized metrics.
  - Report file in PDF or Excel format.

## NFRs
- AES-256 encryption for secure data storage.
- Sub-1-second response time.

---