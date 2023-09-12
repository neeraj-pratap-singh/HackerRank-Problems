# An integer d is a divisor of an integer n if the remainder of n/d = 0.

# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.
def find_divisors(n):
    count = 0
    for digit_str in str(n):  # Convert the integer to a string to iterate through its digits
        digit = int(digit_str)  # Convert the digit back to an integer
        if digit == 0:  # Skip zero, as dividing by zero is undefined
            continue
        if n % digit == 0:  # Check if digit divides n without leaving a remainder
            count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    result = find_divisors(n)
    print(f"The number of divisors of {n} among its own digits is: {result}")
