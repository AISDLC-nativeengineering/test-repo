import tkinter as tk
from tkinter import filedialog
import csv

from src.logging.audit_logger import export_logs_to_csv

def show_audit_trail_ui():
    """
    Displays a simple UI for exporting audit logs.
    """
    def export_logs():
        # Export logs and save CSV file
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filepath:
            export_logs_to_csv()
            with open("change_logs.csv", "r") as log, open(filepath, "w") as dest:
                dest.write(log.read())
            tk.messagebox.showinfo("Export Successful", f"Logs exported to {filepath}.")

    root = tk.Tk()
    root.title("Financial Report Audit Logs")

    export_button = tk.Button(root, text="Export Logs to CSV", command=export_logs)
    export_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    show_audit_trail_ui()