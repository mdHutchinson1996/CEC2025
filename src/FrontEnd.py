import tkinter as tk
from tkinter import ttk
import os
import csv

class AverageConfidenceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Average Confidence Values")
        self.root.geometry("600x200")  # Set the window size to 600x200 to accommodate the labels

        # Labels
        self.yes_label = tk.Label(root, text="Yes")
        self.yes_label.grid(row=0, column=0, padx=10, pady=10)

        self.no_label = tk.Label(root, text="No")
        self.no_label.grid(row=1, column=0, padx=10, pady=10)

        # Progress bars
        self.yes_var = tk.DoubleVar()
        self.yes_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", variable=self.yes_var)
        self.yes_bar.grid(row=0, column=1, padx=10, pady=10)

        self.no_var = tk.DoubleVar()
        self.no_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", variable=self.no_var)
        self.no_bar.grid(row=1, column=1, padx=10, pady=10)

        # Average value labels
        self.yes_avg_label = tk.Label(root, text="0.0")
        self.yes_avg_label.grid(row=0, column=2, padx=10, pady=10)

        self.no_avg_label = tk.Label(root, text="0.0")
        self.no_avg_label.grid(row=1, column=2, padx=10, pady=10)

        # Count labels
        self.yes_count_label = tk.Label(root, text="Count: 0")
        self.yes_count_label.grid(row=0, column=3, padx=10, pady=10)

        self.no_count_label = tk.Label(root, text="Count: 0")
        self.no_count_label.grid(row=1, column=3, padx=10, pady=10)

        # Calculate and update average values
        self.update_averages()

    def update_averages(self):
        yes_values = []
        no_values = []

        # Read the CSV files
        parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        yes_csv_file_path = os.path.join(parent_directory, 'predictedResults_Yes.csv')
        no_csv_file_path = os.path.join(parent_directory, 'predictedResults_No.csv')

        with open(yes_csv_file_path, mode='r') as yes_file:
            reader = csv.reader(yes_file)
            next(reader)  # Skip the header row
            for row in reader:
                yes_values.append(float(row[0]))

        with open(no_csv_file_path, mode='r') as no_file:
            reader = csv.reader(no_file)
            next(reader)  # Skip the header row
            for row in reader:
                no_values.append(float(row[0]))

        # Calculate averages
        yes_average = sum(yes_values) / len(yes_values) if yes_values else 0
        no_average = sum(no_values) / len(no_values) if no_values else 0

        # Update progress bars
        self.yes_var.set(yes_average * 100)  # Assuming confidence is a value between 0 and 1
        self.no_var.set(no_average * 100)  # Assuming confidence is a value between 0 and 1

        # Update average value labels
        self.yes_avg_label.config(text=f"{yes_average:.2f}")
        self.no_avg_label.config(text=f"{no_average:.2f}")

        # Update count labels
        if(len(yes_values) > 0):
            yes_count = len(yes_values)+1
        else:  
            yes_count = 0
        if(len(no_values) > 0):
            no_count = len(no_values)+1
        else:  
            no_count = 0
        self.yes_count_label.config(text=f"Count: {yes_count}")
        self.no_count_label.config(text=f"Count: {no_count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AverageConfidenceApp(root)
    root.mainloop()