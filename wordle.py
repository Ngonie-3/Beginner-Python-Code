import random
from rich import print


class Wordle:
    def __init__(self):
        file = open('words.txt', 'r')
        read = file.readlines()
        self.word = random.choice(read)
        self.num_of_guesses = 0
        self.guess_dictionary = {
            0: [" "] * 5,
            1: [" "] * 5,
            2: [" "] * 5,
            3: [" "] * 5,
            4: [" "] * 5,
            5: [" "] * 5,
        }

    def draw_board(self):
        for guess in self.guess_dictionary.values():
            print(" | ".join(guess))
            print("================")

    def get_user_input(self):
        user_guess = input("Enter a 5 letter word: ")
        while len(user_guess) != 5:
            user_guess = input("Invalid, enter a 5 letter word")

        user_guess = user_guess.lower()
        for index, char in enumerate(user_guess):
            if char in self.word:
                if char == self.word[index]:
                    char = f"[green]{char}[/]"
                else:
                    char = f"[yellow]{char}[/]"
            self.guess_dictionary[self.num_of_guesses][index] = char

        self.num_of_guesses += 1
        return user_guess

    def play(self):
        while True:
            self.draw_board()
            user_guess = self.get_user_input()

            if user_guess == self.word:
                self.draw_board()
                print(f"You won! The correct word is {self.word}")
                break

            if self.num_of_guesses > 5:
                print(f"You lost! The correct word was {self.word}")
                break
