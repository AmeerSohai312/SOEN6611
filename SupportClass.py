class Support:
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return Support.quick_sort(smaller) + [pivot] + Support.quick_sort(greater)
    
    def absolute(k):
        if k>=0:
            return k
        else:
            return k*-1
        
    def custom_sqrt(number, epsilon=1e-7):
        guess = number / 2  # Initial guess (can be any reasonable value)
        
        while Support.absolute(guess * guess - number) > epsilon:
            guess = 0.5 * (guess + number / guess)

        return guess
    