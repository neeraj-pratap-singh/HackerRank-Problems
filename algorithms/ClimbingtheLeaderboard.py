# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

# The player with the highest score is ranked number 1 on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
# Example
# ranked = [100,90,90,80]
# player = [70,80,105]

# The ranked players will have ranks 1,2 ,2 , and 3, respectively. If the player's scores are 70, 80 and 105, their rankings after each game are 4, 3 and 1. Return [4,3,1].

# Function Description

# Complete the climbingLeaderboard function in the editor below.

# climbingLeaderboard has the following parameter(s):

# int ranked[n]: the leaderboard scores
# int player[m]: the player's scores
# Returns

# int[m]: the player's rank after each new score
# Input Format

# The first line contains an integer n, the number of players on the leaderboard.
# The next line contains n space-separated integers ranked[i], the leaderboard scores in decreasing order.
# The next line contains an integer, m, the number games the player plays.
# The last line contains m space-separated integers player[j], the game scores.
def climbingLeaderboard(ranked, player):
    # Remove duplicate scores and sort the leaderboard in descending order
    unique_ranked = list(sorted(set(ranked), reverse=True))
    
    # Initialize a list to store the player's ranks
    player_ranks = []
    
    # Initialize pointers for the ranked and player lists
    i = len(unique_ranked) - 1
    j = 0
    
    while j < len(player):
        if i < 0:
            # Player's score is higher than anyone on the leaderboard
            player_ranks.append(1)
            j += 1
        elif player[j] < unique_ranked[i]:
            # Player's rank is one more than the rank of the current leaderboard score
            player_ranks.append(i + 2)
            j += 1
        elif player[j] >= unique_ranked[i]:
            # Player's score is greater or equal to the current leaderboard score
            # Move to the next lower leaderboard score
            i -= 1
            
    return player_ranks

# Test the function
print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))  # Output should be [4, 3, 1]
