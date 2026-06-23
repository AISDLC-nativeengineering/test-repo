import tkinter as tk
from tkinter import ttk
from report_generation import ReportGenerator

class DashboardUI:
    def __init__(self, api_client):
        self.report_generator = ReportGenerator(api_client)
        self.root = tk.Tk()
        self.root.title("Financial Dashboard")

    def create_ui(self):
        """Generate the dashboard UI for user interaction."""
        tk.Label(self.root, text="Select Financial Year:").grid(row=0, column=0, padx=10, pady=10)
        year_selection = ttk.Combobox(self.root, values=["2025", "2026", "2027"])
        year_selection.grid(row=0, column=1, padx=10, pady=10)

        def generate_report():
            year = year_selection.get()
            if not year:
                tk.messagebox.showerror("Error", "Please select a financial year")
                return
            try:
                data = self.report_generator.fetch_data(year)
                report = self.report_generator.generate_report(data)
                print("Report Generated Successfully:", report)
                tk.messagebox.showinfo("Success", "Report has been generated.")
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Generate Report", command=generate_report).grid(row=1, column=0, columnspan=2, pady=10)

    def run(self):
        self.create_ui()
        self.root.mainloop()

if __name__ == "__main__":
    api_client = None  # Replace with actual API client
    ui = DashboardUI(api_client)
    ui.run()
