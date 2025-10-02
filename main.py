from score_stats import calculate_avg_score
from output import output_player_summary
"""
input example:

Enter player name (or "done"): Alice
Enter score for Alice: 95
Enter player name (or "done"): Bob
Enter score for Bob: notanumber
Invalid score. Skipping this entry.
Enter player name (or "done"): Cara
Enter score for Cara: 88
Enter player name (or "done"): done
"""
# store players as a list of tuples
players = [("Sally", 95), ("Toby", 90), ("Sandeep", 10), ("Zainab", 5)]

# setup variables to store summary values
num_players = len(players)
highest_score_player = (None, 0) # get_highest_score_player()
lowest_score_player = (None, 0)
average_score = calculate_avg_score(players)

# Output player summary
output_player_summary(num_players, highest_score_player[1], lowest_score_player[1], average_score)
