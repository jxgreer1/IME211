import random  # Importing random module to draw random cards

# List of cards and their corresponding values
CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]  # Card values in Baccarat (10, J, Q, K are worth 0)
OUTCOME = ['Player wins', 'Banker wins', 'Tie']  # Possible game outcomes


# Function to compute the score of a hand
def compute_score(hand):

    total_value = 0
    for card in hand:  # Add up the values of the cards
        total_value += VALUES[CARDS.index(card)]  # Use the index of the card in CARDS to find its value in VALUES
    return total_value % 10  # The score is the last digit of the total value


# Function to simulate the Baccarat game
def play_game(): #main play def

    # Game introduction
    print("Welcome to Baccarat!")
    print("Do you want to play as the Player or the Banker?")

    # Ask the user to choose their role
    role = input("Type 'player' to be the Player or 'banker' to be the Banker: ").strip().lower()
    while role not in ['player', 'banker']:  # Validate the input
        role = input("Invalid choice. Please type 'player' or 'banker': ").strip().lower()

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
        print("\nNatural win detected!")  # If either Player or Banker has a natural win
        if player_score == banker_score:  # If scores are tied
            return "It's a Tie!"
        return OUTCOME[banker_score > player_score]  # Determine winner based on higher score

    # Allow the user to decide whether to draw a third card
    if user_is_player:  # If the user is the Player
        if player_score in range(0, 6):  # Player can draw a card only if their score is 0-5
            draw_third_card = input("\nDo you want to draw a third card? (yes/no): ").strip().lower()
            if draw_third_card == "yes":  # If the user decides to draw a card
                player_hand.append(random.choice(CARDS))  # Add a new card to the Player's hand
                print("You drew a third card:", player_hand[-1])  # Show the card
    else:  # If the user is the Banker
        if banker_score in range(0, 6):  # Banker can draw a card only if their score is 0-5
            draw_third_card = input("\nDo you want to draw a third card? (yes/no): ").strip().lower()
            if draw_third_card == "yes":  # If the user decides to draw a card
                banker_hand.append(random.choice(CARDS))  # Add a new card to the Banker's hand
                print("You drew a third card:", banker_hand[-1])  # Show the card

    # Range to decide if other player draws a card
    if not user_is_player and player_score in range(0, 6):
        player_hand.append(random.choice(CARDS))
        print("\nPlayer drew a third card:", player_hand[-1])
    elif user_is_player and banker_score in range(0, 6): #if banker
        banker_hand.append(random.choice(CARDS))
        print("\nBanker drew a third card:", banker_hand[-1])

    # add total score
    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)

    # Display the final hands and scores
    print("\nFinal Player's hand:", player_hand)
    print("Final Player's score:", player_score)
    print("\nFinal Banker's hand:", banker_hand)
    print("Final Banker's score:", banker_score)

    # Determine and return the final outcome
    if player_score > banker_score:
        return "Player wins!"
    elif player_score < banker_score:
        return "Banker wins!"
    else:
        return "It's a Tie!"


# Run the game
result = play_game()  # Call the function to play the game
print("\nGame Over! " + result)  # Print the result of the game
