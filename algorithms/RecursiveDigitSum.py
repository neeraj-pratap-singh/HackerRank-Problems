# We define super digit of an integer x using the following rules:

# Given an integer, we need to find the super digit of the integer.

# If x has only 1 digit, then its super digit is x.
# Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
# For example, the super digit of 9875 will be calculated as:

# 	super_digit(9875)   	9+8+7+5 = 29 
# 	super_digit(29) 	2 + 9 = 11
# 	super_digit(11)		1 + 1 = 2
# 	super_digit(2)		= 2  

# take 2 parameters from user n and k
# where n is strint "9875" and k is int 4
# pass these data in function, create a super digit by concatinating the n k times then perform the above operation
def calculate_super_digit(n, k):
    super_digit = (n * k) % 9
    return super_digit if super_digit != 0 else 9

# Input the values
n = input("Enter an integer n: ")
k = int(input("Enter an integer k: "))

# Calculate super digit
super_digit = calculate_super_digit(int(n), k)
print("Super digit of concatenated string:", super_digit)

# This optimized code avoids the recursive calculation and directly calculates the super digit using the formula (n * k) % 9. This reduces both time and memory complexity.
# This optimized code calculates the super digit of a concatenated string of a given integer n repeated k times. Let's break down the code step by step:

# The function calculate_super_digit(n, k) calculates the super digit using a mathematical property. The formula (n * k) % 9 is used to directly calculate the super digit. If the result is not 0, it's returned as the super digit. If the result is 0, then the super digit is 9.

# The main part of the code takes user input for the integer n as a string and integer k.

# The function calculate_super_digit is called with the integer version of n and k as arguments.

# The calculated super digit is printed to the console.

# This approach eliminates the need for recursive calculations and directly computes the super digit using a mathematical property, making it more efficient and faster compared to the earlier approach.