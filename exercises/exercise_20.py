# rock paper scissor game

import random

options = ("ROCK", "PAPER", "SCISSOR")
win_map = {"ROCK": "SCISSOR", "PAPER": "ROCK", "SCISSOR": "PAPER"}

bot_win = 0
win = 0
rounds = 0

while True:
    print("\nselect gesture: rock, paper, scissor")
    print("or 'q' to quit")
    choice = input("\nyour gesture: ").upper()

    if choice == "Q":
        print(f"\ngame rounds: {rounds}")
        print(f"you won: {win}\nbot won: {bot_win}\ndraws: {rounds - (win + bot_win)}")

        if win > bot_win:
            print("\nyou won the game!")
        elif win < bot_win:
            print("\nbot won the game!")
        else:
            print("\ngame ended in a tie!")
        break

    if choice not in options:
        print("invalid gesture! try again.")
        continue

    bot_choice = random.choice(options)
    print(f"bot chose: {bot_choice}")
    rounds += 1

    if choice == bot_choice:
        print("game is a draw!")
    elif win_map[choice] == bot_choice:
        win += 1
        print("you won this round!")
    else:
        bot_win += 1
        print("you lost this round!")
