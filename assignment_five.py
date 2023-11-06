#
#
#


import random


# Function to get a random number between 1 and 100
def get_number():
    """
    generates a random number that the user tries to guess
    :return: random integer between 1 and 100
    """
    return random.randint(1, 100)


# Function to get a valid guess from the user
def get_guess():
    """
    gets the user's guess. if they put in a valid integer, it will be returned. If not they will get an error message.
    :return: integer with the user's guess
    """
    while True:
        try:
            guess = float(input("Enter a valid integer between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a valid integer between 1 and 100.")
        except ValueError:
            print("Invalid number. Please enter a valid integer between 1 and 100.")


# Main game logic
def play_game():
    """

    :return:
    """
    final_number = get_number()
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    guesses = 0
    while True:
        user_guess = get_guess()
        guesses += 1

        if user_guess < final_number:
            print("Too low! Try again.")
        elif user_guess > final_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", guesses, "tries.")
            return guesses


# Main function to play the game three times and calculate the average
def main():
    total_guesses = 0
    print("this is a guessing game in which you have to guess which number I chose between 1 and 100.")
    print("I will count the amount of tries it takes you per game and tell you the average amount of guesses when "
          "you're done!")
    num_games = int(input("How many times would you like to play?: "))
    get_number()
    get_guess()
    for x in range(num_games):
        total_guesses += play_game()

    average_guesses = total_guesses / num_games
    print("Average number of guesses for", num_games, "games:", average_guesses)


main()
