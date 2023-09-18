# There is a string, s, of lowercase English letters that is repeated infinitely many times. Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.

# Example
# s = 'abcac'
# n = 10

# The substring we consider is abcacabcac, the first 10 characters of the infinite string. There are 4 occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Returns

# int: the frequency of a in the substring
# Input Format

# The first line contains a single string, s.
# The second line contains an integer, n.
def repeatedString(s, n):
    # Calculate the number of times 'a' appears in the original string
    count_a_in_s = s.count('a')
    
    # Calculate how many times the entire string 's' will be repeated
    complete_repeats = n // len(s)
    
    # Calculate the number of letters remaining after fitting the complete repetitions of 's'
    remaining_letters = n % len(s)
    
    # Count the occurrences of 'a' in the remaining part of the string
    count_a_in_remaining = s[:remaining_letters].count('a')
    
    # Calculate the total number of 'a' in the first n letters of the infinite string
    total_count_a = (count_a_in_s * complete_repeats) + count_a_in_remaining
    
    return total_count_a

# Test the function
s = 'abcac'
n = 10
result = repeatedString(s, n)
print(f"The number of occurrences of 'a' in the first {n} characters is {result}.")
