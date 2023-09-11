# Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

# You are given q queries in the form of x, y, and z representing the respective positions for cats A and B, and for mouse C. Complete the function catsAndMouse to return the appropriate answer to each query, which will be printed on a new line.

# If cat A catches the mouse first, print Cat A.
# If cat B catches the mouse first, print Cat B.
# If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.
def cats_and_mouse(x, y, z):
    distance_from_A = abs(z - x)
    distance_from_B = abs(z - y)
    
    if distance_from_A < distance_from_B:
        return "Cat A"
    elif distance_from_B < distance_from_A:
        return "Cat B"
    else:
        return "Mouse C"

# Number of queries
q = int(input("Enter the number of queries: "))

# Loop for each query
for _ in range(q):
    x, y, z = map(int, input("Enter the positions of Cat A, Cat B, and Mouse C separated by spaces: ").split())
    print(cats_and_mouse(x, y, z))
