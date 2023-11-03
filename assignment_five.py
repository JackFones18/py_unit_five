import random


# Function to get a random number between 1 and 100
def get_number():
    return random.randint(1, 100)


# Function to get a valid guess from the user
def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number between 1 and 100.")


# Main game logic
def play_game():
    target_number = get_number()
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    guesses = 0
    while True:
        user_guess = get_guess()
        guesses += 1

        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", guesses,"tries.")
            return guesses


# Main function to play the game three times and calculate the average
def main():
    total_guesses = 0
    num_games = 3
    get_number()
    get_guess()
    for x in range(num_games):
        total_guesses += play_game()

    average_guesses = total_guesses / num_games
    print("Average number of guesses for", num_games,"games:", average_guesses)


if __name__ == "__main":
    main()
