def find_min(arr):
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

def find_max(arr):
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
# Example usage
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_value = find_min(my_list)
max_value = find_max(my_list)
print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")
