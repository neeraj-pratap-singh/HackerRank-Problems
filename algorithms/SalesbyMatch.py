# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
def count_pairs(socks):
    color_count = {}  # Dictionary to store the count of each color
    pairs = 0  # Variable to store the total number of pairs
    
    # Count the occurrences of each color
    for sock in socks:
        if sock in color_count:
            color_count[sock] += 1
        else:
            color_count[sock] = 1
    
    # Count the pairs for each color
    for count in color_count.values():
        pairs += count // 2  # Integer division to find pairs
    
    return pairs

# Taking the number of socks from the user
num_socks = int(input("Enter the number of socks: "))

# Taking the colors of socks from the user
socks_array = []
for _ in range(num_socks):
    sock_color = int(input(f"Enter the color of sock {_+1}: "))
    socks_array.append(sock_color)

# Calculating and displaying the total number of pairs
result = count_pairs(socks_array)
print("Total number of pairs:", result)
