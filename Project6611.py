import tkinter as tk
import statistics
import random
from tkinter import Entry, Label
from tkinter import messagebox
from DataStatistics import DataStatistics


    
    

class DataStatisticsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Statistics Calculator")
        self.data = None

        # Add project name label
        project_name_label = tk.Label(root, text="METRICSTICS", font=("Helvetica", 16, "bold"), pady=10)
        project_name_label.grid(row=0, column=0, columnspan=8)

        # Labels for n and r
        self.n_label = Label(root, text="Please enter the total number you want to generate:")
        self.n_label.grid(row=1, column=0, padx=5, columnspan=8, pady=(0, 10))
        # self.r_label = Label(root, text="Please enter the maximum range of the number you want to generate:")
        # self.r_label.grid(row=2, column=0, padx=5, columnspan=8, pady=(0, 10))

         # Entry widgets for n and r
        self.n_entry = Entry(root)
        self.n_entry.insert(0, "1000")
        self.n_entry.grid(row=1, column=4, padx=5, columnspan=8, pady=(0, 10))
        # self.r_entry = Entry(root)
        # self.r_entry.insert(0, "1000")
        # self.r_entry.grid(row=2, column=4, padx=5, columnspan=8, pady=(0, 10))

        
        self.generate_button = tk.Button(root, text="Generate Data", command=self.generate_data)
        self.generate_button.grid(row=3, column=0, columnspan=8, pady=(0, 10))

        self.data_text = tk.Text(root, height=20, width=50)
        self.data_text.grid(row=4, column=0, columnspan=8, pady=0)

        self.mean_button = tk.Button(root, text="Mean", command=self.calculate_mean)
        self.mean_button.grid(row=5, column=0, padx=45, pady=10)
        self.mean_label = tk.Label(root, text="")
        self.mean_label.grid(row=6, column=0)

        self.median_button = tk.Button(root, text="Median", command=self.calculate_median)
        self.median_button.grid(row=5, column=1, padx=45, pady=10)
        self.median_label = tk.Label(root, text="")
        self.median_label.grid(row=6, column=1)

        self.mode_button = tk.Button(root, text="Mode", command=self.calculate_mode)
        self.mode_button.grid(row=5, column=2, padx=45, pady=10)
        self.mode_label = tk.Label(root, text="")
        self.mode_label.grid(row=6, column=2)

        self.maximum_button = tk.Button(root, text="Maximum", command=self.calculate_maximum)
        self.maximum_button.grid(row=5, column=3, padx=45, pady=10)
        self.maximum_label = tk.Label(root, text="")
        self.maximum_label.grid(row=6, column=3)

        self.minimum_button = tk.Button(root, text="Minimum", command=self.calculate_minimum)
        self.minimum_button.grid(row=5, column=4, padx=45, pady=10)
        self.minimum_label = tk.Label(root, text="")
        self.minimum_label.grid(row=6, column=4)

        self.mad_button = tk.Button(root, text="Mean Absolute Deviation", command=self.calculate_mad)
        self.mad_button.grid(row=5, column=5, padx=45, pady=10)
        self.mad_label = tk.Label(root, text="")
        self.mad_label.grid(row=6, column=5)

        self.sd_button = tk.Button(root, text="Standard Deviation", command=self.calculate_sd)
        self.sd_button.grid(row=5, column=6, padx=45, pady=10)
        self.sd_label = tk.Label(root, text="")
        self.sd_label.grid(row=6, column=6)

    def reset_labels(self):
        self.mean_label.config(text="")
        self.median_label.config(text="")
        self.mode_label.config(text="")
        self.maximum_label.config(text="")
        self.minimum_label.config(text="")
        self.mad_label.config(text="")
        self.sd_label.config(text="")

    def generate_data(self):
        try:
            # Get n and r from Entry widgets
            n = int(self.n_entry.get())
            r = 1000
            if n<=0:
                raise ValueError("Enter the numbers greater than 0 to start operations")
            
            if n>=100000:
                raise ValueError("Enter the number less than the 100000 range to start operations as for better performing runtime")

                       
            self.data = [random.randrange(0, r) for _ in range(n)]
            self.data_text.delete(1.0, tk.END)  # Clear previous data
            self.data_text.insert(tk.END, str(self.data))
            self.reset_labels()  # Reset all labels
        except ValueError as e:
            # Display an error message if there's an issue with the input values
            tk.messagebox.showerror("Input Error", str(e))

    def calculate_mean(self):
        try:
            if self.data:
                statistics_calculator = DataStatistics(self.data)
                mean_value = round(statistics_calculator.calculate_mean(), 2)
                self.mean_label.config(text=f" {mean_value}")
            else:
                raise ValueError("No data available. Please generate data first.")
        except ValueError as e:
            tk.messagebox.showerror("Calculation Error", str(e))

    def calculate_median(self):
        try:
            if self.data:
                statistics_calculator = DataStatistics(self.data)
                median_value = round(statistics_calculator.find_median(), 2)
                self.median_label.config(text=f"{median_value}")
            else:
                raise ValueError("No data available. Please generate data first.")
        except ValueError as e:
            tk.messagebox.showerror("Calculation Error", str(e))

    def calculate_mode(self):
        try:
            if self.data:
                statistics_calculator = DataStatistics(self.data)
                mode_value = statistics_calculator.find_modes()
                self.mode_label.config(text=f"{mode_value}")
            else:
                raise ValueError("No data available. Please generate data first.")
        except ValueError as e:
            tk.messagebox.showerror("Calculation Error", str(e))

    def calculate_maximum(self):
        try:
            if self.data:
                statistics_calculator = DataStatistics(self.data)
                maximum_value = round(statistics_calculator.find_max(), 2)
                self.maximum_label.config(text=f"{maximum_value}")
            else:
                raise ValueError("No data available. Please generate data first.")
        except ValueError as e:
            tk.messagebox.showerror("Calculation Error", str(e))

    def calculate_minimum(self):
        try:
            if self.data:
                statistics_calculator = DataStatistics(self.data)
                minimum_value = round(statistics_calculator.find_min(), 2)
                self.minimum_label.config(text=f"{minimum_value}")
            else:
                raise ValueError("No data available. Please generate data first.")
        except ValueError as e:
            tk.messagebox.showerror("Calculation Error", str(e))

    def calculate_mad(self):
        try:
            if self.data:
                statistics_calculator = DataStatistics(self.data)
                mad_value = round(statistics_calculator.mad(), 2)
                self.mad_label.config(text=f"{mad_value}")
            else:
                raise ValueError("No data available. Please generate data first.")
        except ValueError as e:
            tk.messagebox.showerror("Calculation Error", str(e))

    def calculate_sd(self):
        try:
            if self.data:
                statistics_calculator = DataStatistics(self.data)
                sd_value = round(statistics_calculator.sd(), 2)
                self.sd_label.config(text=f"{sd_value}")
            else:
                raise ValueError("No data available. Please generate data first.")
        except ValueError as e:
            tk.messagebox.showerror("Calculation Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = DataStatisticsGUI(root)
    root.mainloop()
