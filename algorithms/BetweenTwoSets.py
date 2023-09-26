# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Example
# a = [2,6]
# b = [24,36]

# There are two numbers between the arrays: 6 and 12.
# 6%2 = 0, 6%6 = 0 , 24%6 = 0 and 36%6 = 0 for the first value.
# 12%2 = 0, 12%6 = 0 , 24%12 = 0 and 36%12 = 0  for the second value. Return 2.

# Function Description

# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

# getTotalX has the following parameter(s):

# int a[n]: an array of integers
# int b[m]: an array of integers
# Returns

# int: the number of integers that are between the sets
# Input Format

# The first line contains two space-separated integers, n and m, the number of elements in arrays a and b.
# The second line contains n distinct space-separated integers a[i] where 0<=i<n.
# The third line contains m distinct space-separated integers b[j] where 0<=j<m
from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def getTotalX(a, b):
    count = 0
    
    # Calculate LCM of all elements in a
    lcm_a = reduce(lcm, a)
    
    # Calculate GCD of all elements in b
    gcd_b = reduce(gcd, b)
    
    # Check multiples of LCM up to GCD
    multiple = lcm_a
    while multiple <= gcd_b:
        if all(multiple % x == 0 for x in a) and all(x % multiple == 0 for x in b):
            count += 1
        multiple += lcm_a
    
    return count

# Example usage
a = [2, 6]
b = [24, 36]
print(getTotalX(a, b))  # Output should be 2
