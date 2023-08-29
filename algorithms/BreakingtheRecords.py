# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

# Example
# scores = [12,24,10,24]
# Scores are in the same order as the games played. She tabulates her results as follows:

#                                      Count
#     Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1
# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.
def breaking_records(scores):
    min_score = max_score = scores[0]
    min_breaks = max_breaks = 0
    
    for score in scores:
        if score < min_score:
            min_score = score
            min_breaks += 1
        elif score > max_score:
            max_score = score
            max_breaks += 1
    
    return max_breaks, min_breaks

# Example usage
scores = [12, 24, 10, 24]
max_breaks, min_breaks = breaking_records(scores)
print("Number of times Maria breaks her record for most points:", max_breaks)
print("Number of times Maria breaks her record for least points:", min_breaks)
