import pyfiglet
import random
import time
from termcolor import colored

win_game = False


def show():
    change_color = 2
    for row in game_board:
        for cell in row:
            if change_color % 2 == 0:
                print(cell, end=" ")
        print()


def check_game():
    global win_game
    for row in range(3):
        sum = 0
        sum1 = 0
        for cell in range(3):
            if game_board[cell][row] == "X":
                sum1 += 1
            elif game_board[row][cell] == "X":
                sum += 1
        if sum == 3 or sum1 == 3:
            print("Player 1 win!🥳")
            win_game = True

    for row in range(3):
        sam = 0
        sam1 = 0
        for cell in range(3):
            if game_board[cell][row] == "O":
                sam1 += 1
            elif game_board[row][cell] == "O":
                sam += 1
        if sum == 3 or sum1 == 3:
            print("Player 2 win!🥳")
            win_game = True

    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("Player 1 wins!")
        win_game = True

    elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("Player 2 wins!")
        win_game = True

    elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        print("Player 1 wins!")
        win_game = True

    elif game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
        print("Player 2 wins!")
        win_game = True

    ave = 0
    for row in range(3):
        for cell in range(3):
            if game_board[row][cell] != "-":
                ave += 1
    if ave == 9:
        print("The game equalised\n")
        win_game = True


title = pyfiglet.figlet_format("Tic Toc Toe", font="slant")
print(title)

start = time.time()
while True:
    print("1.Player vs Computer")
    print("2.Player vs Player")
    print("3.Quit")
    print()

    choice = input("enter your choice: ")

    if choice == "1":
        print()
        game_board = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]]

        show()

        while True:
            print()
            print("Player 1")
            while True:
                row = int(input("row: "))
                cell = int(input("cell: "))

                if 0 <= row <= 2 and 0 <= cell <= 2:
                    if game_board[row][cell] == "-":
                        game_board[row][cell] = colored("X", 'red')
                        break
                    else:
                        print("jerdo jer nazan!")
                else:
                    print("mesl adam vared kon")

            show()
            check_game()
            if win_game == True:
                break

            print("\nComputer")
            print()
            while True:
                row = random.randint(0, 2)
                cell = random.randint(0, 2)

                if 0 <= row <= 2 and 0 <= cell <= 2:
                    if game_board[row][cell] == "-":
                        game_board[row][cell] = colored("O", 'blue')
                        break

            show()
            check_game()
            if win_game == True:
                break

    elif choice == "2":
        print()
        game_board = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]]

        show()

        while True:
            print()
            print("Player 1")
            while True:
                row = int(input("row: "))
                cell = int(input("cell: "))

                if 0 <= row <= 2 and 0 <= cell <= 2:
                    if game_board[row][cell] == "-":
                        game_board[row][cell] = colored("X", 'red')
                        break
                    else:
                        print("jerdo jer nazan!")
                else:
                    print("mesl adam vared kon")

            show()
            check_game()
            if win_game == True:
                break

            print("Player 2")
            print()
            while True:
                row = int(input("row: "))
                cell = int(input("cell: "))

                if 0 <= row <= 2 and 0 <= cell <= 2:
                    if game_board[row][cell] == "-":
                        game_board[row][cell] = colored("O", 'blue')
                        break
                    else:
                        print("jerdo jer nazan!")
                else:
                    print("mesl adam vared kon")

            show()
            check_game()
            if win_game == True:
                break

    elif choice == "3":
        break

    else:
        print("mesl adam vared kon")

end = time.time()

hour = 0
min = 0
sec = int(end - start)
if sec >= 3600:
    hour = sec/3600
    sec = sec % 3600
    if sec > 60:
        min = sec/60
        sec = sec % 60

elif sec < 3600:
    min = sec/60
    sec = sec % 60


print("\ntime is: ", int(hour), ":", int(min), ":", sec)
