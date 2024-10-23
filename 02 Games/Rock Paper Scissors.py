import random

def introduction():
    print("Welcome to Rock, Paper, Scissors!")
    print("Try to beat the computer by choosing rock, paper, or scissors.\n")

def get_player_choice():
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter 1, 2, or 3: ")
    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    return choices.get(choice, None)

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    player_choice = get_player_choice()
    if player_choice is None:
        print("Invalid choice. Game over.")
        return

    computer_choice = get_computer_choice()
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

def main():
    play_again = "yes"
    while play_again.lower() == "yes":
        introduction()
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ")

if __name__ == "__main__":
    main()