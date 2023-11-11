import tkinter as tk
import statistics
import random

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

        self.generate_button = tk.Button(root, text="Generate Data", command=self.generate_data)
        self.generate_button.pack()

        self.data_text = tk.Text(root, height=20, width=160)
        self.data_text.pack()

        self.mean_button = tk.Button(root, text="Mean", command=self.calculate_mean)
        self.mean_button.pack()
        self.mean_label = tk.Label(root, text="Mean: ")
        self.mean_label.pack()

        self.median_button = tk.Button(root, text="Median", command=self.calculate_median)
        self.median_button.pack()
        self.median_label = tk.Label(root, text="Median: ")
        self.median_label.pack()

        self.mode_button = tk.Button(root, text="Mode", command=self.calculate_mode)
        self.mode_button.pack()
        self.mode_label = tk.Label(root, text="Mode: ")
        self.mode_label.pack()

        self.maximum_button = tk.Button(root, text="Maximum", command=self.calculate_maximum)
        self.maximum_button.pack()
        self.maximum_label = tk.Label(root, text="Maximum: ")
        self.maximum_label.pack()

        self.minimum_button = tk.Button(root, text="Minimum", command=self.calculate_minimum)
        self.minimum_button.pack()
        self.minimum_label = tk.Label(root, text="Minimum: ")
        self.minimum_label.pack()

        self.mad_button = tk.Button(root, text="Mean Absolute Deviation", command=self.calculate_mad)
        self.mad_button.pack()
        self.mad_label = tk.Label(root, text="Mean Absolute Deviation: ")
        self.mad_label.pack()

        self.sd_button = tk.Button(root, text="Standard Deviation", command=self.calculate_sd)
        self.sd_button.pack()
        self.sd_label = tk.Label(root, text="Standard Deviation: ")
        self.sd_label.pack()

    def generate_data(self):
        n = 1000
        r = 1000
        self.data = [random.randrange(0, r) for _ in range(n)]
        self.data_text.delete(1.0, tk.END)  # Clear previous data
        self.data_text.insert(tk.END, str(self.data))

    def calculate_mean(self):
        if self.data:
            statistics_calculator = DataStatistics(self.data)
            mean_value = statistics_calculator.calculate_mean()
            self.mean_label.config(text=f"Mean: {mean_value}")

    def calculate_median(self):
        if self.data:
            statistics_calculator = DataStatistics(self.data)
            median_value = statistics_calculator.find_median()
            self.median_label.config(text=f"Median: {median_value}")

    def calculate_mode(self):
        if self.data:
            statistics_calculator = DataStatistics(self.data)
            mode_value = statistics_calculator.find_modes()
            self.mode_label.config(text=f"Mode: {mode_value}")

    def calculate_maximum(self):
        if self.data:
            statistics_calculator = DataStatistics(self.data)
            maximum_value = statistics_calculator.find_max()
            self.maximum_label.config(text=f"Maximum: {maximum_value}")

    def calculate_minimum(self):
        if self.data:
            statistics_calculator = DataStatistics(self.data)
            minimum_value = statistics_calculator.find_min()
            self.minimum_label.config(text=f"Minimum: {minimum_value}")

    def calculate_mad(self):
        if self.data:
            statistics_calculator = DataStatistics(self.data)
            mad_value = statistics_calculator.mad()
            self.mad_label.config(text=f"Mean Absolute Deviation: {mad_value}")

    def calculate_sd(self):
        if self.data:
            statistics_calculator = DataStatistics(self.data)
            sd_value = statistics_calculator.sd()
            self.sd_label.config(text=f"Standard Deviation: {sd_value}")

if __name__ == '__main__':
    root = tk.Tk()
    app = DataStatisticsGUI(root)
    root.mainloop()
