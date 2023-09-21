# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

# Example
# a = [1,1,2,2,4,4,5,5,5]

# There are two subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.

# Function Description

# Complete the pickingNumbers function in the editor below.

# pickingNumbers has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the length of the longest subarray that meets the criterion
# Input Format

# The first line contains a single integer n, the size of the array a.
# The second line contains  space-separated integers, each an a[i].

# Constraints
# 2<=n<=100
# 0<a[i]<100

# The answer will be >= 2.
def pickingNumbers(a):
    # Initialize a dictionary to store the frequency of each integer
    freq = {}
    
    # Count the frequency of each integer in the array
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_length = 0
    
    # Iterate through the unique integers to find the longest subarray
    for num in freq.keys():
        max_length = max(max_length, freq[num] + freq.get(num + 1, 0))
        max_length = max(max_length, freq[num] + freq.get(num - 1, 0))
    
    return max_length

# Input read and function call
n = int(input())
a = list(map(int, input().split()))
result = pickingNumbers(a)
print(result)
