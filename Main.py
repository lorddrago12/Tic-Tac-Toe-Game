import random

Board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True
 

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    inp = int(input("Enter a number from 1-9 to place your X: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = "X"
    else:
        print("Opps player has already placed their mark there. Try again.")
        playerInput(board)


def computerMove(board):
    available = [i for i, v in enumerate(board) if v == "-"]
    move = random.choice(available)
    board[move] = "O"
    print(f"Computer placed O in position {move+1}")


# --- THE LOOP YOU WANTED ---
while gameRunning:
    printBoard(Board)

    # Player turn
    playerInput(Board)

    printBoard(Board)

    # Computer turn
    computerMove(Board)

# Not added the check win, lose or draw function.
