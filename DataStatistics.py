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
    
import random
if __name__ == '__main__':
    
    n=int(input("Please enter the number you want to generate"))
    r=int(input("Please enter the maximum range of numbers"))
    data=[]
    for i in range(n):
        data.append(random.randrange(1,r))
        
    print("Below displayed is the random generated data ")
    print(data)
    statistics_calculator = DataStatistics(data)
    maximum= statistics_calculator.find_max()
    minimum= statistics_calculator.find_min()
    mean_value = statistics_calculator.calculate_mean()
    median_value = statistics_calculator.find_median()
    mode_value = statistics_calculator.find_modes()
    mean_absolute_deviation_value = statistics_calculator.mad()
    standard_deviation_value = statistics_calculator.sd()
    
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Mode: {mode_value}")
    print(f"Mean Absolute Deviation: {mean_absolute_deviation_value}")
    print(f"Standard Deviation: {standard_deviation_value}")

