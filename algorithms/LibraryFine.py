# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

# 1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
# 2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos x (the number of days late)
# 3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos x (the number of months late).
# 4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10000 Hackos.

# Example
# d1, m1, y1 = 14, 7, 2018
# d2, m2, y2 = 5, 7, 2018

# The first values are the return date and the second are the due date. The years are the same and the months are the same. The book is 14-5 = 9 days late. Return 9*15=135.

# Function Description

# Complete the libraryFine function in the editor below.

# libraryFine has the following parameter(s):

# d1, m1, y1: returned date day, month and year, each an integer
# d2, m2, y2: due date day, month and year, each an integer
# Returns

# int: the amount of the fine or 0 if there is none
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Initialize fine to 0
    fine = 0
    
    # Case 1: Returned on or before due date
    if (y1, m1, d1) <= (y2, m2, d2):
        fine = 0
    
    # Case 2: Returned after the expected day but within the same month and year
    elif y1 == y2 and m1 == m2 and d1 > d2:
        fine = 15 * (d1 - d2)
    
    # Case 3: Returned after the expected month but within the same year
    elif y1 == y2 and m1 > m2:
        fine = 500 * (m1 - m2)
        
    # Case 4: Returned after the expected year
    elif y1 > y2:
        fine = 10000
    
    return fine

# Test the function
d1, m1, y1 = 14, 7, 2018
d2, m2, y2 = 5, 7, 2018
print(libraryFine(d1, m1, y1, d2, m2, y2))  # Output should be 135
