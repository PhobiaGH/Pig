#########################################
#########################################
##                                     ##
##         mmmmm    "                  ##
##         #   "# mmm     mmmm         ##
##         #mmm#"   #    #" "#         ##
##         #        #    #   #         ##
##         #      mm#mm  "#m"#         ##
##                        m  #         ##
##                         ""          ##
##                                     ##
#########################################
#########################################

import random
import time

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2 - 8): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 8:
            break
        else:
            print("Must be between 2 - 8 players.")
    else:
        print("Invalid entry, enter a number between 2 - 8.")

max_score = 100
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_index in range(players):
        print("\nPlayer", player_index + 1, "Your turn has begun!\n")
        print("Your overall score is:", player_scores[player_index], "\n")
        current_score = 0

        while True:
            want_roll = input("Would you like to roll (y/n)? ")
            if want_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("\nYou rolled a 1!")
                current_score = 0
                break
            else:
                current_score += value
                print("\nYou rolled a:", value)

            print("Your score is:", current_score, "\n")
            time.sleep(1)

        player_scores[player_index] += current_score
        print("Your overall score is:", player_scores[player_index])
        print("Your turn is over.\n")
        time.sleep(3)

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player", winning_index + 1, "is the winner with a score of:", max_score)









#########################################
#########################################
##                                     ##
##  By: PhobiaGH                       ##
##⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠙⠻⢶⣄⡀⠀⠀⠀⢀⣤⠶⠛⠛⡇⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⣙⣿⣦⣤⣴⣿⣁⠀⠀⣸⠇⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣡⣾⣿⣿⣿⣿⣿⣿⣿⣷⣌⠋⠀⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⣄⡈⢻⣿⡟⢁⣠⣾⣿⣦⠀⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠘⣿⠃⣿⣿⣿⣿⡏⠀⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⠛⣰⠿⣆⠛⠁⠀⡀⠀⠀⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣦⠀⠘⠛⠋⠀⣴⣿⠁⠀⠀⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣏⠀⠀⠀⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠀⠀⠀⠾⢿⣿⠀⠀⠀⠀⠀⠀##
##⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⡿⠟⠋⣁⣠⣤⣤⡶⠶⠶⣤⣄⠈⠀⠀⠀⠀⠀⠀##
##⠀⠀⠀⢰⣿⣿⣮⣉⣉⣉⣤⣴⣶⣿⣿⣋⡥⠄⠀⠀⠀⠀⠉⢻⣄⠀⠀⠀⠀⠀##
##⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣋⣁⣤⣀⣀⣤⣤⣤⣤⣄⣿⡄⠀⠀⠀⠀##
##⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀##
##⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉                      ##
##                                     ##
#########################################
#########################################