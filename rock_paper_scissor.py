import random

user_win = 0
computer_wins = 0

options = ['rock', 'paper', 'scirrors']

while True:
    user_input = input("Type Rock/Paper/Scirrors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("Computer picked: ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scirrors":
        print("you won!")
        user_win += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_win += 1
    elif user_input == "scirrors" and computer_pick == "paper":
        print("you won!")
        user_win += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_win, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")


