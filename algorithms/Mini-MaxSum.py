# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
def min_max_sum(arr):
    min_sum = sum(arr) - max(arr)
    max_sum = sum(arr) - min(arr)
    return min_sum, max_sum

# Input five integers
arr = list(map(int, input().split()))

min_sum, max_sum = min_max_sum(arr)
print(min_sum, max_sum)
