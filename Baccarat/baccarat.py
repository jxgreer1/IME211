

import random

# Constants
CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
OUTCOME = ['Player wins', 'Banker wins', 'Tie']

def display_intro():
    """Display the game introduction."""
    print("Welcome to Baccarat!")
    print('''
To play Baccarat, first pick your bet amount for the round. Then choose 
if you want to be the Player or the Banker. The "Dealer" deals the cards, 
and your goal is to get the closest score to 9. A total score of 8 or 9 
is a "natural win." When you hit, both Player and Banker draw cards.
Cards 10-King are worth 0.
''')

def compute_score(hand):
    """Compute the score of a hand."""
    total_value = sum(VALUES[CARDS.index(card)] for card in hand)
    return total_value % 10

def get_bet_amount(total_money):
    """Get a valid bet amount from the user."""
    while True:
        try:
            bet_amount = int(input("Enter your bet amount: "))
            if 0 < bet_amount <= total_money:
                return bet_amount
            else:
                print("Invalid bet amount. Please enter a valid bet.")
        except ValueError:
            print("Please enter a number.")

def get_user_role():
    """Ask the user to choose their role."""
    while True:
        role = input("Type 'player' to be the Player or 'banker' to be the Banker: ").lower()
        if role in ['player', 'banker']:
            return role == 'player'
        print("Invalid choice. Please type 'player' or 'banker'.")

def draw_card():
    """Draw a random card."""
    return random.choice(CARDS)

def display_hand_and_score(hand, role):
    """Display the hand and score for a role."""
    score = compute_score(hand)
    print(f"\n{role.capitalize()}'s cards: {hand}")
    print(f"{role.capitalize()}'s score: {score}")
    return score

def check_natural_win(player_score, banker_score):
    """Check for a natural win."""
    if player_score in [8, 9] or banker_score in [8, 9]:
        print("Natural win detected!")
        if player_score == banker_score:
            return "It's a Tie!"
        return OUTCOME[banker_score > player_score]
    return None

def ask_to_draw_card(role):
    """Ask if the user wants to draw a card."""
    while True:
        choice = input(f"\nDo you want {role} to draw a third card? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        print("Invalid choice. Please type 'yes' or 'no'.")

def update_total_money(total_money, bet_amount, result, user_is_player):
    """Update the total money based on the result."""
    if result == "Player wins!":
        return total_money + bet_amount if user_is_player else total_money - bet_amount
    elif result == "Banker wins!":
        return total_money - bet_amount if user_is_player else total_money + bet_amount
    return total_money  # No change for a tie

def play_round(total_money):
    """Play a single round of Baccarat."""
    print(f"\nYour total money: ${total_money}")
    bet_amount = get_bet_amount(total_money)
    user_is_player = get_user_role()
    role = 'Player' if user_is_player else 'Banker'

    # Initial hands
    player_hand = [draw_card(), draw_card()]
    banker_hand = [draw_card(), draw_card()]
    
    # Display initial hands and scores
    player_score = display_hand_and_score(player_hand, "Player")
    banker_score = display_hand_and_score(banker_hand, "Banker")
    
    # Check for natural win
    result = check_natural_win(player_score, banker_score)
    if not result:
        # Player draws a third card
        if user_is_player and player_score in range(0, 6) and ask_to_draw_card("Player"):
            player_hand.append(draw_card())
            player_score = display_hand_and_score(player_hand, "Player")
        
        # Banker draws a third card
        if not user_is_player and banker_score in range(0, 6) and ask_to_draw_card("Banker"):
            banker_hand.append(draw_card())
            banker_score = display_hand_and_score(banker_hand, "Banker")

        # Determine result
        if player_score > banker_score:
            result = "Player wins!"
        elif player_score < banker_score:
            result = "Banker wins!"
        else:
            result = "It's a Tie!"

    print("\nGame Over! " + result)
    return update_total_money(total_money, bet_amount, result, user_is_player)

def play_game():
    """Main game loop."""
    display_intro()
    total_money = 1000

    while total_money > 0:
        total_money = play_round(total_money)
        if total_money <= 0:
            print("You have no more money left. Game over!")
            break
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")

# Run the game
play_game()
