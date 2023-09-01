# A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.

# Example
# b=60
# keyboards = [40, 50, 60]
# drivers=[5,8,12]
# The person can buy a 40 keyboard + 12 usb drives = 52, or a 50 keyboard+8 usb drivers=58. Choose the latter as the more expensive option and return 58.

# Function Description

# Complete the getMoneySpent function in the editor below.

# getMoneySpent has the following parameter(s):

# int keyboards[n]: the keyboard prices
# int drives[m]: the drive prices
# int b: the budget
# Returns

# int: the maximum that can be spent, or -1 if it is not possible to buy both items
# Input Format

# The first line contains three space-separated integers b,n , and m, the budget, the number of keyboard models and the number of USB drive models.
# The second line contains n space-separated integers keyboard[i], the prices of each keyboard model.
# The third line contains m space-separated integers drivers, the prices of the USB drives.

# Constraints
# 1<=n, m<=100
# 1<=b<=10^6
# The price of each item is in the inclusive range [1,10^6].

#Time complexity is O(n^2)
def getMoneySpent(keyboards, drives, b):
    max_spent = -1  # Initialize the maximum spent variable to -1
    
    for keyboard_price in keyboards:
        for drive_price in drives:
            total_price = keyboard_price + drive_price
            if total_price <= b and total_price > max_spent:
                max_spent = total_price
    
    return max_spent

# Read input
b, n, m = map(int, input().split())
keyboards = list(map(int, input().split()))
drives = list(map(int, input().split()))

result = getMoneySpent(keyboards, drives, b)
print(result)


#Time complexity is O(n * log(n) + m * log(m))
def getMoneySpent(keyboards, drives, budget):
    keyboards.sort()  # Sort keyboards in ascending order
    drives.sort(reverse=True)  # Sort drives in descending order
    
    max_spent = -1  # Initialize max_spent to -1
    
    i = 0
    j = 0
    
    while i < len(keyboards) and j < len(drives):
        total_cost = keyboards[i] + drives[j]
        
        if total_cost <= budget and total_cost > max_spent:
            max_spent = total_cost
        
        if total_cost < budget:
            i += 1  # Move to the next keyboard (higher price)
        else:
            j += 1  # Move to the next drive (lower price)
    
    return max_spent

# Example usage:
budget = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]

result = getMoneySpent(keyboards, drives, budget)
print(result)  # Output: 58
# This modified program has a time complexity of O(n * log(n) + m * log(m)), where n is the number of keyboard models, and m is the number of USB drive models. The sorting steps have a time complexity of O(n * log(n)) and O(m * log(m)), and the subsequent traversal is linear. This approach is more efficient than the previous O(n * m) approach for large input sizes.