# Way to roll the die
import random  # allow to generate random numbers

# Rolling the die
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

#value = roll()
#print(value)

# Set up the number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4")
    else:
            print("Inavlid, Try Again !")

# Defining the maximum score  
max_score = 50 

# List of all the individual scores of the players
player_scores = [0 for _ in range(players)]


# Player turn
while max(player_scores) < max_score:
    # One player's turn
    for player_idx in range(players):
    # Player turn
        print("\nPlayer", player_idx+1, "turn just started !\n")
        print(" Your total score is : ", player_scores[player_idx], "\n")
    # Track the scores
        current_score = 0 
        while True:
        # rolling turn
            should_roll = input("Would you like to roll (Y): ")
            if should_roll.lower() != 'y' :
                break
            value = roll()
            if value == 1:
                print(" Your solled is 1, Turn Done !")
                current_score = 0
                break
            else:
                current_score += value
                print(" You rolled a : ", value)
                
            print(" Your current score is: ", current_score)
            
            # Current score after the turn of the player
        player_scores[player_idx] +=  current_score
        print("The total score is : ", player_scores[player_idx])

         
max_score = max(player_scores)    
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx+1, "has won the game with the score of", max_score,"! :)")


