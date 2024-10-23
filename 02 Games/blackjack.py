import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the score of the current cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, dealer_score):
    """Compares the scores of the dealer and the player."""
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Lose"
    elif player_score == 0:
        return "Win"
    elif player_score > 21:
        return "Lose"
    elif dealer_score > 21:
        return "Win"
    elif player_score > dealer_score:
        return "Win"
    else:
        return "Lose"


def play_blackjack():
    print("Welcome to Blackjack!")
    player_balance = 1000  # Initial player balance

    while True:
        player_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card(), deal_card()]
        print(f"\nYour balance is: ${player_balance}")
        try:
            bid = int(input("How much would you like to bid? $"))
            if bid > player_balance:
                print("Sorry, you can't bid more than your current balance.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        game_over = False

        while not game_over:
            player_score = calculate_score(player_cards)
            dealer_score = calculate_score(dealer_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Dealer's first card: {dealer_cards[0]}")

            if player_score == 0 or dealer_score == 0 or player_score > 21:
                game_over = True
            else:
                should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
                if should_continue.lower() == "y":
                    player_cards.append(deal_card())
                else:
                    game_over = True

        while dealer_score != 0 and dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        result = compare(player_score, dealer_score)
        if result == "Win":
            player_balance += bid
            print(f"You win! New balance: ${player_balance}")
        elif result == "Lose":
            player_balance -= bid
            print(f"You lost! New balance: ${player_balance}")
        else:
            print("It's a draw!")

        if player_balance <= 0:
            print("You've run out of money! Game over.")
            break

        if input("Do you want to play another round? (y/n): ").lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_blackjack()
