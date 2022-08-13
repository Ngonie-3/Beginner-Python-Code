from guess_number import guess_the_number
from rock_paper_scissors import r_p_s
from wordle import Wordle

while True:
    txt = """Welcome to Mini Games!!!
    -Guess The number(1)
    -Rock, Paper, Scissors(2)
    -Wordle(3)
    -Connect Four(4)
    -Tic Tac Toe(5)
To play a game press a number, or 'q' to quit: """
    value = input(txt)
    if value == "1":
        upper_limit = int(input("Choose a number to represent the upper limit: "))
        guess_the_number(upper_limit)
    elif value == "2":
        r_p_s()
    elif value == "3":
        game = Wordle()
        game.play()
    elif value == "4":
        pass
    elif value == "5":
        pass
    elif value == "q":
        print("Thank you for playing")
        break
