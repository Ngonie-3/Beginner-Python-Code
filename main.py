from guess_number import guess_the_number
from rock_paper_scissors import r_p_s
from wordle import Wordle
from connect_four import ConnectFour
while True:
    txt = """Welcome to Mini Games!!!
    1. Guess The number
    2. Rock, Paper, Scissors
    3. Wordle
    4. Connect Four
    5. Tic Tac Toe
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
        connect = ConnectFour()
        connect.play()
    elif value == "5":
        pass
    elif value == "q":
        print("Thank you for playing")
        break
