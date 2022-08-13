import random


def guess_the_number(x):
    print("Let's play Guess The Number")
    random_number = random.randint(0, x)
    num_of_guesses = 0
    while True:
        guess = int(input(f"Pick a number between 0 and {x}: "))
        num_of_guesses += 1
        if guess == random_number:
            print(f"Congratulations you guessed the correct number which is {random_number}")
            print(f"The number of guesses you took were {num_of_guesses}")
            break
        elif guess < random_number:
            print("The number you guessed is lower than the actual number")
        else:
            print("The number you guessed is higher than the actual number")
