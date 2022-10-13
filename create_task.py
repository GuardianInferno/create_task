import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# define a print board
# define a player move
# define what is victory
# define what a draw is
# Create a Loop for iteration

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

move = " "
playermove = 0
player = ""


# visual board
def board1():
    print(" " + board.get(1) + " | " + board.get(2) + " | " + board.get(3) + " \n___|___|___\n " + board.get(
        4) + " | " + board.get(5) + " | " + board.get(6) + " \n___|___|___\n " + board.get(7) + " | " + board.get(
        8) + " | " + board.get(9) + " \n   |   |  \n")




def check_victory():
    while playermove >= 5:
        if board.get(1).strip() == board.get(2) == board.get(3):  # 1-2-3 horiz
            print("Player " + board.get(1) + " wins!")
            global vict
            vict = 1
            play_again()
            break
        if board.get(4).strip() == board.get(5) == board.get(6):  # 4-5-6 horiz
            print("Player " + board.get(4) + " wins!")
            vict = 1
            play_again()
            break
        if board.get(7).strip() == board.get(8) == board.get(9):  # 7-8-9 horiz
            print("Player " + board.get(7) + " wins!")
            vict = 1
            play_again()
            break
        if board.get(1) == board.get(4) == board.get(7) != " ":  # 1-4-7 vert
            print("Player " + board.get(1) + " wins!")
            vict = 1
            play_again()
            break
        if board.get(2) == board.get(5) == board.get(8) != " ":  # 2-5-8 vert
            print("Player " + board.get(2) + " wins!")
            vict = 1
            play_again()
            break
        if board.get(3) == board.get(6) == board.get(9) != " ":  # 3-6-9 vert
            print("Player " + board.get(3) + " wins!")
            vict = 1
            play_again()
            break
        if board.get(1) == board.get(5) == board.get(9) != " ":  # 1-5-9 diag
            print("Player " + board.get(3) + " wins!")
            vict = 1
            play_again()
            break
        if board.get(3) == board.get(5) == board.get(7) != " ":  # 3-5-7 diag
            print("Player " + board.get(3) + " wins!")
            vict = 1
            play_again()
            break
        break




def check_move():
    move = int(input("Player " + player + " choose a spot: "))
    while board[move] != " ":
        clearConsole()
        board1()
        print("Sorry that spot is already taken!")
        move = int(input("Player " + player + " choose a spot: "))
    if board[move] == " ":
        board[move] = player
        clearConsole()
        board1()





def game():
    global playermove
    global player
    global vict
    vict = 0
    # print blank board
    clearConsole()
    board.update({1: " ", 2: " ", 3: " ",
                  4: " ", 5: " ", 6: " ",
                  7: " ", 8: " ", 9: " "})
    board1()

    for i in range(2):
        # move1,3
        player = "X"
        check_move()
        playermove += 1

        # move2,4
        player = "O"
        check_move()
        playermove += 1

        # move5
    player = "X"
    check_move()
    playermove += 1
    check_victory()

    # move6,8
    for i in range(2):
        if vict != 1:
            player = "O"
            check_move()
            playermove += 1
            check_victory()
            # move7,9
        if vict != 1:
            player = "X"
            check_move()
            playermove += 1
            check_victory()

    if vict != 1:
        print("It's a draw!")


def play_again():
    time.sleep(.5)
    c = input("Want to play again? ")
    if c.lower().strip()[0] == 'y':
        play('y')
    elif c.lower().strip()[0] == 'n':
        play('n')
    else:
        print('Ok')


def play(option: str):
    if option == 'y':
        game()
    elif option == 'n':
        print('Awwww. Maybe next time!')
    else:
        print("See you another time!")


def main():
    clearConsole()

    choice = input('Want to play tictactoe against your friend?')
    if choice.lower().strip()[0] == 'y':
        play('y')
    elif choice.lower().strip()[0] == 'n':
        play('n')
    else:
        print("That is not a choice. Goodbye.")

if __name__ == "__main__":
    main()
