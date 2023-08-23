# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example
# candles = [4,4, 2, 3]

# The maximum height candles are 4 units high. There are 2 of them, so return 2.
def count_tallest_candles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count

# Input the list of candle heights
candles = list(map(int, input().split()))

tallest_count = count_tallest_candles(candles)
print(tallest_count)
