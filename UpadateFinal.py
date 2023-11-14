import tkinter as tk
import statistics
import random
from tkinter import Entry, Label
from tkinter import messagebox

class DataStatistics:
    def __init__(self, data):
        self.data = data


    
    def calculate_mean(self):
        a=self.data
        n=len(a)
        ms=0
        for i in range(n):
            ms=ms+a[i]
        mavg=ms/n
        return mavg
    
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return DataStatistics.quick_sort(smaller) + [pivot] + DataStatistics.quick_sort(greater)
    
    
    def find_modes(self):
        arr=self.data
        if not arr:
            raise ValueError("List is empty, cannot find mode")
        counts = {}
        max_count = 0
        modes = []
        for item in arr:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
            if counts[item] > max_count:
                max_count = counts[item]
                modes = [item]
            elif counts[item] == max_count and item not in modes:
                modes.append(item)
        return modes
    
    
    def find_median(self):
        arr=self.data
        if not arr:
            raise ValueError("List is empty, cannot find mean")
        sorted_numbers = DataStatistics.quick_sort(arr)
        num_elements = len(sorted_numbers)
        if num_elements % 2 == 1:
            median = sorted_numbers[num_elements // 2]
        else:
            middle1 = sorted_numbers[num_elements // 2 - 1]
            middle2 = sorted_numbers[num_elements // 2]
            median = (middle1 + middle2) / 2
        return median
    
    def find_min(self):
        arr=self.data
        if not arr:
            raise ValueError("List is empty, cannot find minimum")
        def divide_conquer_min(start, end):
            if start == end:
                return arr[start]
            elif end - start == 1:
                return arr[start] if arr[start] < arr[end] else arr[end]
            else:
                mid = (start + end) // 2
                min1 = divide_conquer_min(start, mid)
                min2 = divide_conquer_min(mid + 1, end)
                return min1 if min1 < min2 else min2
        return divide_conquer_min(0, len(arr) - 1)
    
    def find_max(self):
        arr=self.data
        if not arr:
            raise ValueError("List is empty, cannot find maximum")
        def divide_conquer_max(start, end):
            if start == end:
                return arr[start]
            elif end - start == 1:
                return arr[start] if arr[start] > arr[end] else arr[end]
            else:
                mid = (start + end) // 2
                max1 = divide_conquer_max(start, mid)
                max2 = divide_conquer_max(mid + 1, end)
                return max1 if max1 > max2 else max2
        return divide_conquer_max(0, len(arr) - 1)
    
    def absolute(k):
        if k>=0:
            return k
        else:
            return k*-1
    
    def mad(self):
        a=self.data
        n=len(a)
        ms=0
        for i in range(n):
            ms=ms+a[i]
        mavg=ms/n
        mads=0
        for i in range(n):
            mads=mads+(DataStatistics.absolute(a[i]-mavg))        
        madavg=mads/n
        return madavg
    
    def custom_sqrt(number, epsilon=1e-7):
        guess = number / 2  # Initial guess (can be any reasonable value)
        
        while DataStatistics.absolute(guess * guess - number) > epsilon:
            guess = 0.5 * (guess + number / guess)

        return guess
    
    def sd(self):
        a=self.data
        n=len(a)
        ms=0
        for i in range(n):
            ms=ms+a[i]
        mavg=ms/n
        sds=0
        for i in range(n):
            tv=(a[i]-mavg)*(a[i]-mavg)  
            sds=sds+tv
        
        sdavg=sds/n
        return (DataStatistics.custom_sqrt(sdavg))

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
        self.r_label = Label(root, text="Please enter the maximum range of the number you want to generate:")
        self.r_label.grid(row=2, column=0, padx=5, columnspan=8, pady=(0, 10))

         # Entry widgets for n and r
        self.n_entry = Entry(root)
        self.n_entry.insert(0, "1000")
        self.n_entry.grid(row=1, column=4, padx=5, columnspan=8, pady=(0, 10))
        self.r_entry = Entry(root)
        self.r_entry.insert(0, "1000")
        self.r_entry.grid(row=2, column=4, padx=5, columnspan=8, pady=(0, 10))

        
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
            r = int(self.r_entry.get())
            if r < n:
                raise ValueError("Maximum range must be greater than or equal to the total number")


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
