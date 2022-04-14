

import random
magic_number = random.randint(1,100)
print(magic_number)
print("Hello! Welcome to the Number Guessing Game! ^_^")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
# easy/hard counter will decrease as user makes an incorrect guess.
easy_counter = 10
hard_counter = 5

def remaining(level):
    print(f"You have {level} attempt(s) remaining to guess the number.")


def user_guess(level):
    guess = int(input("Make a guess: "))
    if guess == magic_number:
        print(f"You got it! The magic number is {magic_number}.")
        exit()
    elif guess > magic_number:
        print("Too high.")
        return level - 1
    elif guess < magic_number:
        print("Too low.")
        return level -1


def game(level):
    while level != 0:
        remaining(level)
        level = user_guess(level)
        if level != 0:
            print("\nGuess again.")
    print("You ran out of all attempts! You lose.")

if difficulty == "easy":
    game(level = easy_counter)
elif difficulty == "hard":
    game(level = hard_counter)