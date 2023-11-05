# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 23:37:17 2023

@author: Palacy
"""

# FINDING MEDIAN OF NUMBERS

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    smaller = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(greater)

def find_median(arr):
    if not arr:
        raise ValueError("List is empty, cannot find mean")
    sorted_numbers = quick_sort(arr)
    num_elements = len(sorted_numbers)
    if num_elements % 2 == 1:
        median = sorted_numbers[num_elements // 2]
    else:
        middle1 = sorted_numbers[num_elements // 2 - 1]
        middle2 = sorted_numbers[num_elements // 2]
        median = (middle1 + middle2) / 2
    return median

# Example:
my_array = [7, 8, 4, 6, 9]
result = find_median(my_array)
print("The Median of this array is:", result)



# FINDING MODE OF NUMBERS

def find_modes(arr):
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

# Example usage:
numbers = [1, 1, 2, 2, 3, 3, 4]
result = find_modes(numbers)
print("Modes:", result)



