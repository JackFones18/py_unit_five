# Jack Fones 11-7-2023 this code generates a random number between 1 and 100 and has the user guess the number.
# after each guess, the computer tells the user whether their guess is too low or too high, and keeps track of the
# number of guesses. After the user plays three times the computer will average the amount of guesses that the user
# took per game.


import random


def get_number():
    """
    generates a random number that the user will try to guess
    :return: random integer between 1 and 100
    """
    return random.randint(1, 100)


def get_guess():
    """
    gets the user's guess. if they put in a valid integer, it will be returned. If not they will get an error message.
    :return: float with the user's guess
    """
    while True:
        try:                                                                                                            # This line and lines 30-31 ensure that if the user enters a string the code will not completely break.
            guess = float(input("Enter a valid integer between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a valid integer between 1 and 100.")
        except ValueError:
            print(":( That's not right! Please enter a valid integer between 1 and 100.")


# Main game logic
def play_game():
    """
    this is the function that actually runs the game. It takes the computer's number and compares it to the user's
    number, which is entered with an input. It will compare the user's number with the computer's and tell the user
    whether their number is higher or lower than the computer's.
    :return: returns the amount of guesses as an int so the computer can later average the amount of guesses per game.
    """
    final_number = get_number()
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    guesses = 0
    while True:
        user_guess = get_guess()
        guesses += 1                                                                                                    # Adds one guess to the tally every time the user enters a number
        if user_guess < final_number:
            print("Nope! That's too low! Try again, please.")
        elif user_guess > final_number:
            print("Not quite, that's too high! Please try again.")
        else:                                                                                                           # If the user's guess isn't higher or lower they got it right, which is why I used the else statement.
            print("Congratulations! You guessed the number in", guesses, "tries. I didn't think you'd ever get that "
                "one!")
            return guesses


# Main function to play the game three times and calculate the average
def main():
    total_guesses = 0                                                                                                   # Sets the amount of guesses to zero.
    print("This is a guessing game in which you have to guess which number I chose between 1 and 100.")                 # Just a print statement to explain the code to the user.
    print("I will count the amount of tries it takes you per game and tell you the average amount of guesses per game "
        "when you're done!")
    num_games = int(input("How many times would you like to play? Choose wisely!: "))
    get_number()
    get_guess()
    for x in range(num_games):
        total_guesses += play_game()                                                                                    # This is where the play_game is called, and it's called however many times the user enters in num_games

    average_guesses = total_guesses / num_games                                                                         # Takes the total amount of guesses, which was the return from play_game, and divides it by the number of games played to find the average.
    print(" Your average number of guesses for", num_games, "games:", average_guesses)
    print("Wow! That's a lot! I bet you get a lower average!")
    while True:                                                                                                         # Creating a while loop specifically for when the user decides whether they want to play again
        choice = input("Would you like to play again? (y/n): ")
        if choice == "n":
            print("Ok! See you later!")
            break                                                                                                       # Breaks the while loop if the user selects no.
        if choice == "y":
            main()                                                                                                      # If the user wants to keep playing it just reruns main.


main()
