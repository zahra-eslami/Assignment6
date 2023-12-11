import pyfiglet
import random
import colorama
import time

title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

def show(board):
    for row in board:
        for cell in row:
            if cell == "X":
                print(colorama.Fore.RED + cell, colorama.Fore.RESET, end=" ")
            elif cell == "O":
                print(colorama.Fore.BLUE + cell, colorama.Fore.RESET, end=" ")
            else:
                print(cell, end="  ")
        print()

def check_winner(board, player):
    # Check rows
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

    
def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                empty_cells.append((i, j))
    return empty_cells


def player_choice():
    while True:
        try:
            row = int(input("Row: "))
            col = int(input("Column: "))
            if not (0 <= row <= 2 and 0 <= col <= 2):
                raise ValueError
            return row, col
        except ValueError:
            print("The Range of Row & Cell are between 0 and 2")

def play_game():
    game_board=[["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]]

    print("Who Do you want to play with:")
    print("1 - Computer")
    print("2 - Another player")
    try:
        choice = int(input("Enter choice (1 or 2): "))
    except ValueError:
        print("You must enter an integer number between 1 & 2")

    show(game_board)

    current_player = "X"

    while True:

        if choice == 1 and current_player == "O":
            row, col = random.choice(get_empty_cells(game_board))
        else:
            print(f"Player {current_player}:")
            row, col = player_choice()

        if game_board[row][col] == "-":
            game_board[row][col] = current_player
            if choice==1 and current_player == "O":
                print("Computer Choice:")

            show(game_board)

            if check_winner(game_board, current_player):
                if choice == 1 and current_player == "O":
                    print("Computer wins!")
                else:
                    print(f"Player {current_player} wins!")
                break
            elif all(cell != "-" for row in game_board for cell in row):
                print("It's a tie!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        else:
            print("You Can't choose this cell; Try again.")

start = time.time()
play_game()
print(f"Game Time: {time.time() - start:.2f} seconds")
