# You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

# Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left.

# Example
# arr = [1,2,3]
# The shortest stick length is 1, so cut that length from the longer two and discard the pieces of length 1. Now the lengths are arr = [1,2]. Again, the shortest stick is of length 1, so cut that amount from the longer stick and discard those pieces. There is only one stick left,arr=[1] , so discard that stick. The number of sticks at each iteration are answer=[3,2,1].

# Function Description

# Complete the cutTheSticks function in the editor below. It should return an array of integers representing the number of sticks before each cut operation is performed.

# cutTheSticks has the following parameter(s):

# int arr[n]: the lengths of each stick
# Returns

# int[]: the number of sticks after each iteration
# Input Format

# The first line contains a single integer n, the size of arr.
# The next line contains n space-separated integers, each an arr[i], where each value represents the length of the i stick.

# Constraints
# 1<=n<=1000
# 1<=arr[i]<=1000
def cutTheSticks(arr):
    result = []
    
    while len(arr) > 0:
        # Append the current number of sticks to the result list
        result.append(len(arr))
        
        # Find the shortest stick
        shortest = min(arr)
        
        # Cut the sticks
        arr = [x - shortest for x in arr]
        
        # Remove sticks that have been completely cut
        arr = [x for x in arr if x > 0]
        
    return result

# Test the function
print(cutTheSticks([1, 2, 3]))  # Output should be [3, 2, 1]
