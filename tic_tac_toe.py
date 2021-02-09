'''
Tic-Tac-Toe Game.
You vs NPC Player.

@author = Bran Oliver
@status = Done!!
@version = 2.0.0
'''

import os
import random
from colorama import Fore

play_again = 'y'
win = 'n'
player = 2
turns = 0
max_turns = 9
tic_tac_toe = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

clear = "os.system('cls')"


def screen():
    eval(clear)
    print(Fore.RED + "    0   1   2")
    print(f"0:  {tic_tac_toe[0][0]} | {tic_tac_toe[0][1]} | {tic_tac_toe[0][2]}")
    print("   -----------")
    print(f"1:  {tic_tac_toe[1][0]} | {tic_tac_toe[1][1]} | {tic_tac_toe[1][2]}")
    print("   -----------")
    print(f"2:  {tic_tac_toe[2][0]} | {tic_tac_toe[2][1]} | {tic_tac_toe[2][2]} \n" + Fore.RESET)
    print("Turns: " + Fore.GREEN + f"{str(turns)}" + Fore.RESET)


def player_turn():
    global player
    global turns
    global max_turns
    if player == 2 and turns < max_turns:
        try:
            row = int(input("Row....: "))
            col = int(input("Column.: "))
            while tic_tac_toe[row][col] != " ":
                row = int(input("Row..: "))
                col = int(input("Column.: "))
            tic_tac_toe[row][col] = "X"
            player = 1
            turns += 1
        except Exception:
            print("Invalid!!!!")
            os.system("pause")


def npc_turn():
    global player
    global turns
    global max_turns
    if player == 1 and turns < max_turns:
        row = random.randrange(0, 3)
        col = random.randrange(0, 3)
        while tic_tac_toe[row][col] != " ":
            row = random.randrange(0, 3)
            col = random.randrange(0, 3)
        tic_tac_toe[row][col] = "O"
        turns += 1
        player = 2


def victory():
    global tic_tac_toe
    vic = 'n'
    symbol = ["X", "O"]
    for s in symbol:
        # lines
        if (tic_tac_toe[0][0] == s) and (tic_tac_toe[0][1] == s) and (tic_tac_toe[0][2] == s):
            vic = s
        if (tic_tac_toe[1][0] == s) and (tic_tac_toe[1][1] == s) and (tic_tac_toe[1][2] == s):
            vic = s
        if (tic_tac_toe[2][0] == s) and (tic_tac_toe[2][1] == s) and (tic_tac_toe[2][2] == s):
            vic = s
        # columns
        if (tic_tac_toe[0][0] == s) and (tic_tac_toe[1][0] == s) and (tic_tac_toe[2][0] == s):
            vic = s
        if (tic_tac_toe[0][1] == s) and (tic_tac_toe[1][1] == s) and (tic_tac_toe[2][1] == s):
            vic = s
        if (tic_tac_toe[0][2] == s) and (tic_tac_toe[1][2] == s) and (tic_tac_toe[2][2] == s):
            vic = s
        # diagonals
        if (tic_tac_toe[0][0] == s) and (tic_tac_toe[1][1] == s) and (tic_tac_toe[2][2] == s):
            vic = s
        if (tic_tac_toe[0][2] == s) and (tic_tac_toe[1][1] == s) and (tic_tac_toe[2][0] == s):
            vic = s

    return vic


def reset():
    global win
    global player
    global turns
    global max_turns
    global tic_tac_toe
    win = 'n'
    player = 2
    turns = 0
    max_turns = 9
    tic_tac_toe = [
                    [" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]
    ]


if __name__ == "__main__":
    while play_again == 'y':
        play = True
        while play:
            screen()
            win = victory()
            if (win == 'n') and (turns < max_turns):
                player_turn()

            screen()

            win = victory()
            if (win == 'n') and (turns < max_turns):
                npc_turn()

            if (win != 'n') or (turns >= max_turns):
                play = False

        print(Fore.BLUE + 'GAME OVER!!!!' + Fore.YELLOW)
        if win == 'O':
            print('Result: NPC won!!!!' + Fore.RESET)
        elif win == 'X':
            print('Result: You won!!! Congratulations!!! \\o/' + Fore.RESET)
        else:
            print('TIC TAC TOE!!!' + Fore.RESET)

        play_again = input(Fore.GREEN + 'Do you wanna play again? (y/n): ' + Fore.RESET)
        reset()
