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
players = []
while True:
    player_name = input("Enter player name (or \"done\")")
    if player_name.lower() == "done":
        break
    score = int(input(f"Enter score for {player_name}: "))
    try: 
        if score >= 0:
            players.append((player_name, score))
        else:
            print("Invalid score. Skipping this entry.")
    except ValueError:
        print("Invalid score. Skipping this entry.")
print(players)
# setup variables to store summary values
num_players = len(players)
highest_score_player = max(players, key=lambda x: x[1]) # get_highest_score_player()
lowest_score_player = min(players, key=lambda x: x[1])
average_score = calculate_avg_score(players)

# Output player summary
output_player_summary(num_players, highest_score_player[1], lowest_score_player[1], average_score)
