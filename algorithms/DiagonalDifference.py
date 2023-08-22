# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(matrix):
    n = len(matrix)
    primary_sum = 0
    secondary_sum = 0
    
    for i in range(n):
        primary_sum += matrix[i][i]
        secondary_sum += matrix[i][n - i - 1]
    
    absolute_difference = abs(primary_sum - secondary_sum)
    return absolute_difference

# Example usage
n = int(input("Enter the size of the square matrix: "))
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = diagonalDifference(matrix)
print("Absolute difference between sums of diagonals:", result)
