# Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.

# Example
# ar = [1,2,3,4,5,6]
# k = 5

# Three pairs meet the criteria: [1,4] , [2,3]  and [4,6].

# Function Description

# Complete the divisibleSumPairs function in the editor below.

# divisibleSumPairs has the following parameter(s):

# int n: the length of array ar
# int ar[n]: an array of integers
# int k: the integer divisor
# Returns
# - int: the number of pairs

# Input Format

# The first line contains 2 space-separated integers, n and k.
# The second line contains n space-separated integers, each a value of ar[i].
def divisibleSumPairs(n, ar, k):
    count = 0  # Initialize the count of pairs that meet the criteria to zero
    
    # Loop through each pair (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            # Check if the sum of ar[i] and ar[j] is divisible by k
            if (ar[i] + ar[j]) % k == 0:
                count += 1  # Increment the count
                
    return count  # Return the final count

# Example usage:
n, k = 6, 5
ar = [1, 2, 3, 4, 5, 6]
result = divisibleSumPairs(n, ar, k)
print(result)  # Output should be 3
