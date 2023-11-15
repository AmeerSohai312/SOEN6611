from SupportClass import Support as sp

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
        if len(modes)>=20:
            return modes[0:20]
        else:
            return modes
    
    
    def find_median(self):
        arr=self.data
        if not arr:
            raise ValueError("List is empty, cannot find mean")
        sorted_numbers = sp.quick_sort(arr)
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
    

    
    def mad(self):
        a=self.data
        n=len(a)
        ms=0
        for i in range(n):
            ms=ms+a[i]
        mavg=ms/n
        mads=0
        for i in range(n):
            mads=mads+(sp.absolute(a[i]-mavg))        
        madavg=mads/n
        return madavg
    

    
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
        return (sp.custom_sqrt(sdavg))
