def calculate_avg_score(players):
    ## pull the scores into a separate list
    # declare a new variable to hold a list of scores
    player_scores = []
    score_total = 0

    # iterate over the players list
    # add each score to the new list
    for player in players:
        player_scores.append(player[1])
        # add all the scores together
        score_total += player[1]

    # print(score_total)
    # print(player_scores)
    # find the average
    # divide by the number of scores
    # set the value of average_score
    return score_total / len(player_scores)

    # 2025 10 20