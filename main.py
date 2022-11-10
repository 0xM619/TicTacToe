"""
Python TicTacToe
A Game by Max Lockett 0xM619
"""

from random import randint
from simple_colors import *

def welcome_message():
    print(" --------------------------- ")
    print("|                           |")
    print("|                           |")
    print("|     Welcome to 0xM619     |")
    print("|      TicTacToe Game!      |")
    print("|                           |")
    print("|                           |")
    print(" --------------------------- ")

def choose_opponent():
    global opponent
    global humanplayer
    global roboplayer
    humanplayer = str()
    roboplayer = str()
    opponent = int()
    while True:
        try:
            opponent = int(input("Enter 1 to play against another human or 2 to play against the computer: "))
            if opponent not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Please enter 1 or 2.")
    if opponent == 2:
        while True:
            try:
                humanplayer = input("Do you want to play as X or O?: ").upper()
                if humanplayer not in ["X", "O"]:
                    raise ValueError
                break
            except ValueError:
                print("Please enter \"X\" or \"O\".")
        if humanplayer == "X":
            roboplayer = "O"
        elif humanplayer == "O":
            roboplayer = "X"

    elif opponent == 1:
        input("Decide who is Xes and who is Os, and type enter when you are ready: ")



gridarray = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def display_grid():
    print("       Col   Col   Col")
    print("        1     2     3   ")
    print("      $$$$$$$$$$$$$$$$$")
    print("Row 1 $  " + red(gridarray[0][0]) + " |  " + red(gridarray[0][1]) + "  | " + red(gridarray[0][2]) + "  $")
    print("      $---------------$")
    print("Row 2 $  " + red(gridarray[1][0]) + " |  " + red(gridarray[1][1]) + "  | " + red(gridarray[1][2]) + "  $")
    print("      $---------------$")
    print("Row 3 $  " + red(gridarray[2][0]) + " |  " + red(gridarray[2][1]) + "  | " + red(gridarray[2][2]) + "  $")
    print("      $$$$$$$$$$$$$$$$$\n")

def whofirst():
    if randint(0,1) == 1:  #Randomly selects who will go first in a player vs player game
        print("\nX goes first!\n")
        firstplayer = "X"
    else:
        print("\nO goes first!\n")
        firstplayer = "O"
    return firstplayer



def make_move_2player():
    winCondition = False
    currentplayer = firstplayer
    totalmoves = 0


    while winCondition != True:
        while True:
            # Catches an error if user enters a value outside the array.
            try:
                rowpos = int(input(currentplayer + "es, please enter the " + red("ROW", ["bold", "underlined"]) + " you'd like to put your symbol on: ")) - 1
                columnpos = int(input(currentplayer + "es, please enter the " + red("COLUMN", ["bold", "underlined"]) + " you'd like to put your symbol on: ")) - 1
            except (ValueError):
                print("Please enter a whole number only\n")
                continue
            try:
                if gridarray[rowpos][columnpos] == " ":  # Checks to make sure the selected square is empty
                    gridarray[rowpos][
                        columnpos] = currentplayer  # Sets the specified row/col position in the gridarray to current player value
                    totalmoves += 1
                    break
                else:
                    print("Please select an empty position\n")
            except IndexError:
                print("Please enter a valid position\n")
                continue
        display_grid()  #Displays updated grid
        winCondition = check_win()  #Checks to see if a win condition exists and updates winCondition variable

        # If a tie exists (9 moves have been made and a win condition has not been reached) the game exits
        if totalmoves == 9 and not winCondition:
            print("\nTie! Nobody wins :(")
            quit()

        # Switches the current player to the other one at the end of each turn
        if currentplayer == "X": currentplayer = "O"
        elif currentplayer == "O": currentplayer = "X"


def make_move_computer():
    winCondition = False
    totalmoves = 0

    display_grid()
    while winCondition != True:
        while True:
            # Catches an error if user enters a value outside the array.
            try:
                rowpos = int(input(humanplayer + "es, please enter the " + red("ROW", ["bold", "underlined"]) + " you'd like to put your symbol on: ")) - 1
                columnpos = int(input(humanplayer + "es, please enter the " + red("COLUMN", ["bold", "underlined"]) + " you'd like to put your symbol on: ")) - 1
            except (ValueError):
                print("Please enter a whole number only\n")
                continue
            try:
                if gridarray[rowpos][columnpos] == " ":  # Checks to make sure the selected square is empty
                    gridarray[rowpos][columnpos] = humanplayer  # Sets the specified row/col position in the gridarray to current player value
                    totalmoves += 1
                    break
                else:
                    print("Please select an empty position\n")
            except IndexError:
                print("Please enter a valid position\n")
                continue
        display_grid()  #Displays updated grid
        winCondition = check_win()  #Checks to see if a win condition exists and updates winCondition variable
        if totalmoves == 9 and not winCondition:
            print("\nTie! Nobody wins :(")
            quit()

        while True:
            # Randomly selects coordinates for the robot player
            roborowpos = randint(0,2)
            robocolpos = randint(0, 2)

            if gridarray[roborowpos][robocolpos] == " ":  # Checks to make sure the selected square is empty
                gridarray[roborowpos][robocolpos] = roboplayer  # Sets the specified row/col position in the gridarray to current player value
                totalmoves += 1
                print(f"The computer moved to row {roborowpos + 1}, column {robocolpos + 1}.\n")
                break
            else:
                continue
        display_grid()  # Displays updated grid
        winCondition = check_win()  # Checks to see if a win condition exists and updates winCondition variable

        # Checks for a tie
        if totalmoves == 9 and not winCondition:
            print("\nTie! Nobody wins :(")
            quit()

def check_win():
    # Checking the first row for winners
    if gridarray[0][0] == "X" and gridarray[0][1] == "X" and gridarray[0][2] == "X":
        print("X wins! Three in a row!"); return True
    elif gridarray[0][0] == "O" and gridarray[0][1] == "O" and gridarray[0][2] == "O":
        print("O wins! Three in a row!"); return True

    # Checking the second row for winners
    if gridarray[1][0] == "X" and gridarray[1][1] == "X" and gridarray[1][2] == "X":
        print("X wins! Three in a row!"); return True
    elif gridarray[1][0] == "O" and gridarray[1][1] == "O" and gridarray[1][2] == "O":
        print("O wins! Three in a row!"); return True

        # Checking the third row for winners
    if gridarray[2][0] == "X" and gridarray[2][1] == "X" and gridarray[2][2] == "X":
        print("X wins! Three in a row!"); return True
    elif gridarray[2][0] == "O" and gridarray[2][1] == "O" and gridarray[2][2] == "O":
        print("O wins! Three in a row!"); return True

        # Checking the first column for winners
    if gridarray[0][0] == "X" and gridarray[1][0] == "X" and gridarray[2][0] == "X":
        print("X wins! Three in a row!"); return True
    elif gridarray[0][0] == "O" and gridarray[1][0] == "O" and gridarray[2][0] == "O":
        print("O wins! Three in a row!"); return True

        # Checking the second column for winners
    if gridarray[0][1] == "X" and gridarray[1][1] == "X" and gridarray[2][1] == "X":
        print("X wins! Three in a row!"); return True
    elif gridarray[0][1] == "O" and gridarray[1][1] == "O" and gridarray[2][1] == "O":
        print("O wins! Three in a row!"); return True

        # Checking the third column for winners
    if gridarray[0][2] == "X" and gridarray[1][2] == "X" and gridarray[2][2] == "X":
        print("X wins! Three in a row!"); return True
    elif gridarray[0][2] == "O" and gridarray[1][2] == "O" and gridarray[2][2] == "O":
        print("O wins! Three in a row!"); return True
    
        # Checking diagonal for winners
    if gridarray[0][0] == "X" and gridarray[1][1] == "X" and gridarray[2][2] == "X":
        print("X wins! Three in a row!"); return True
    elif gridarray[0][0] == "O" and gridarray[1][1] == "O" and gridarray[2][2] == "O":
        print("O wins! Three in a row!"); return True

        # Checking other diagonal for winner
    if gridarray[0][2] == "X" and gridarray[1][1] == "X" and gridarray[2][0] == "X":
        print("X wins! Three in a row!"); return True
    elif gridarray[0][2] == "O" and gridarray[1][1] == "O" and gridarray[2][0] == "O":
        print("O wins! Three in a row!"); return True

welcome_message()
choose_opponent()
if opponent == 2:
    make_move_computer()
elif opponent == 1:
    firstplayer = whofirst()
    make_move_2player()


