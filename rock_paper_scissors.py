import random


def r_p_s():
    print("Let's play Rock Paper Scissors")
    r = "rock"
    p = "paper"
    s = "scissors"
    all_choices = [r, p, s]
    while True:
        user_input = input(f"Select a choice either {r}, {p} or {s}: ")
        computer_input = random.choice(all_choices)
        if user_input not in all_choices:
            print("Invalid Choice")
            return
        print(f"You chose {user_input} and The Computer chose {computer_input}")
        if user_input == computer_input:
            print("Tie")
        elif user_input == r and computer_input == s:
            print(f"You won. {r} smashes {s}")
        elif user_input == p and computer_input == r:
            print(f"You won. {p} covers {r}")
        elif user_input == s and computer_input == p:
            print(f"You won {s} cuts {p}")
        elif computer_input == r and user_input == s:
            print(f"The Computer won. {r} smashes {s}")
        elif computer_input == p and user_input == r:
            print(f"The Computer won. {p} covers {r}")
        else:
            print(f"The Computer won. {s} cuts {p}")
        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.lower() != "y":
            break
