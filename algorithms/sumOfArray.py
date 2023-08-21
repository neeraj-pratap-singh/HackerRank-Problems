# Given an array of integers, find the sum of its elements.

# For example, if the array ar = [1,2,3] , 1+2+3=6 , so return 6
def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Example usage
arr = [1, 2, 3]
result = array_sum(arr)
print("Sum of array elements:", result)
