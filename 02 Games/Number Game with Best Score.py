print("""Welcome to the number guessing game!
You will imput a number between 1-100.
Try to use as few tries as possible.""")

import random

def new_round():
    random_number = random.randint(1, 100)
    number_of_guesses = 0

    while True:
        guess = int(input("Input guess: "))
        if guess > 100 or guess < 1:
            print("Your guess was out of bounds, try again.")
        else:
            number_of_guesses += 1
            if guess == random_number:
                print("Congrats! You guessed the number! You took", number_of_guesses, "guesses!")
                return number_of_guesses
            elif guess < random_number:
                print("Your guess was too low, try again.")
            elif guess > random_number:
                print("Your guess was too high, try again.")

best_score = float('inf')

while True:
    current_score = new_round()
    if current_score < best_score:
        best_score = current_score
        print(f"New best score is: {best_score} guesses!")
    else:
        print(f"Your score: {current_score} guesses. Best score is: {best_score} guesses.")
    play_again = input("Would you like to play again? (y/n):").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break