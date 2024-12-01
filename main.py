'''
PLAN:
1. take user input (A, B -- both inclusive)
    ensure range is valid (A < B)
2. generate random number
3. user guesses number
    using while loop (do u wanna play again)
        using while loop (checking guess)
            counter variable for number of tries
4. game over message
5. want to play again?
'''

# NUMBER GUESSING GAME 

import random

def main():
    lower, upper = get_range()

    correct_num = generate_random(lower, upper)

    while True:
        num_of_guesses = 1
        got_it = False

        print(f"I have selected a number between {lower} and {upper} (both inclusive). Can you guess it?")
        user_guess = int(input("Your guess: "))
        while got_it == False:
            if user_guess > correct_num:
                print("Your guess is too high. Try again.")
                num_of_guesses += 1
            if user_guess < correct_num:
                print("Your guess is too low. Try again.")
                num_of_guesses += 1

            user_guess = int(input("Your guess: "))
            if user_guess == correct_num:
                got_it = True
        print("\nCongratulations! You've guessed the correct number.")
        print(f"Number of guesses: {num_of_guesses}\n")

        user_play_again = input("Do you want to play again (yes/no)? ").lower()

        if user_play_again == "no":
            print("Thank you for playing!")
            return

        lower, upper = get_range()
        correct_num = generate_random(lower, upper)

def get_range() -> tuple:
    lower = int(input("Lower limit: "))
    upper = int(input("Upper limit: "))

    while lower >= upper:
        print("Lower limit must be smaller than upper limit.")
        lower = int(input("Lower limit: "))
        upper = int(input("Upper limit: "))

    return lower, upper

def generate_random(lower, upper):
    return random.randint(lower, upper)

if __name__ == "__main__":
    main()
