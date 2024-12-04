

import random
# List of cards and their corresponding values
CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]  # card values (10-King are worth 0)
OUTCOME = ['Player wins', 'Banker wins', 'Tie']  # Possible game outcomes


def compute_score(hand):
    total_value = 0
    for card in hand:  # Add up the values of the cards
        total_value += VALUES[CARDS.index(card)]
    return total_value % 10  # The score is the last digit of the total value


def play_game():  # main play def
    # Game introduction
    print("Welcome to Baccarat!")
    print('''
To Play baccarat the first step is the pick your bet amount for the round. After that you choose 
if you are the Player or the Banker. From there the "Dealer" then deals the cards and your job
is to get the closet to 9, like blackjack. If you get a 8 or a 9 total score that is considered a 
"natural win." When you hit, it hits both the player and banker. cards 10-King are worth 0. 
''')

    # Initialize player's total money
    total_money = 1000  # Starting amount for the player

    while True:  # Loop to allow multiple games
        print(f"\nYour total money: ${total_money}")
        if total_money <= 0:
            print("You have no more money left. Game over!")
            break

        bet_amount = int(input("Enter your bet amount: "))
        while bet_amount > total_money or bet_amount <= 0:
            bet_amount = int(input("Invalid bet amount. Please enter a valid bet: "))

        print("Do you want to play as the Player or the Banker?")
        # Ask the user to choose their role
        role = input("Type 'player' to be the Player or 'banker' to be the Banker: ")
        while role not in ['player', 'banker']:  # Check the input
            role = input("Invalid choice. Please type 'player' or 'banker': ")

        user_is_player = role == 'player'  # Boolean to track if the user is the Player
        print(f"\nYou are the {'Player' if user_is_player else 'Banker'}. Let's begin!")

        # Generate initial hands for the Player and the Banker
        player_hand = [random.choice(CARDS), random.choice(CARDS)]  # Draw two random cards for the Player
        banker_hand = [random.choice(CARDS), random.choice(CARDS)]  # Draw two random cards for the Banker

        # Compute the initial scores
        player_score = compute_score(player_hand)
        banker_score = compute_score(banker_hand)

        # Display the initial hands and scores
        print("\nPlayer's cards:", player_hand)
        print("Player's score:", player_score)
        print("\nBanker's cards:", banker_hand)
        print("Banker's score:", banker_score)

        # Check for natural win (score of 8 or 9)
        if player_score in [8, 9] or banker_score in [8, 9]:
            print("Natural win detected!")  # If either Player or Banker has a natural win
            if player_score == banker_score:  # If scores are tied
                result = "It's a Tie!"
            else:
                result = OUTCOME[banker_score > player_score]  # Determine winner based on higher score
        else:
            # Allow to decide whether to draw another card
            if user_is_player:  # If the user is the Player
                if player_score in range(0, 7):  # Player can draw a card only if their score is 0-5
                    draw_third_card = input("\nDo you want to draw a third card? (yes/no): ")
                    if draw_third_card == "yes":  # If the user decides to draw a card
                        player_hand.append(random.choice(CARDS))  # Add a new card to the Player's hand
                        print("You drew a third card:", player_hand[-1])  # Show the card
            else:
                if banker_score in range(0, 7):  # Banker can draw a card only if their score is 0-5
                    draw_third_card = input("\nDo you want to draw a third card? (yes/no): ")
                    if draw_third_card == "yes":  # If the user decides to draw a card
                        banker_hand.append(random.choice(CARDS))  # Add a new card to the Banker's hand
                        print("Banker drew a third card:", banker_hand[-1])  # Show the card

            # Add total score
            player_score = compute_score(player_hand)
            banker_score = compute_score(banker_hand)

            # Display the final hands and scores
            print("\nFinal Player's hand:", player_hand)
            print("Final Player's score:", player_score)
            print("\nFinal Banker's hand:", banker_hand)
            print("Final Banker's score:", banker_score)

            # Determine and return the final outcome
            if player_score > banker_score:
                result = "Player wins!"
            elif player_score < banker_score:
                result = "Banker wins!"
            else:
                result = "It's a Tie!"

        print("\nGame Over! " + result)  # Print the result of the game

        # Adjust total money based on result
        if result == "Player wins!":
            total_money += bet_amount if user_is_player else -bet_amount
        elif result == "Banker wins!":
            total_money += bet_amount if not user_is_player else -bet_amount
        else:
            print("It's a Tie! No money won or lost.")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

# Run the game
play_game()  # Call the function to play the game
