import random

def guess_the_number_game():
    print("\n--- Welcome to 'Guess the Number'! ---")
    player_name = input("What's your name? ")
    print(f"Hello, {player_name}! I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    secret_number = random.randint(1, 100)
    guesses_taken = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            guesses_taken += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
            elif guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"\nGood job, {player_name}! You guessed my number in {guesses_taken} guesses!")
                break
        except ValueError:
            print("That's not a valid number. Please enter an integer.")

# Main game loop to allow playing multiple times
while True:
    guess_the_number_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
