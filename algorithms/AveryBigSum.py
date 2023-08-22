# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

# Function Description

# Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

# aVeryBigSum has the following parameter(s):

# int ar[n]: an array of integers .
# Return

# long: the sum of all array elements
# Input Format

# The first line of the input consists of an integer .
# The next line contains  space-separated integers contained in the array.

# Output Format

# Return the integer sum of the elements in the array.
def aVeryBigSum(ar):
    total_sum = sum(ar)
    return total_sum

# Example usage
n = int(input("Enter the number of elements: "))
ar = list(map(int, input("Enter the array elements separated by space: ").split()))
result = aVeryBigSum(ar)
print("Sum of array elements:", result)
