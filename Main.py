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
    if available:
        move = random.choice(available)
        board[move] = "O"
        print(f"Computer placed O in position {move+1}")


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    if board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    if board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True
    return False


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True
    return False


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True
    return False


def checkTie(board):
    return "-" not in board


def checkWin(board):
    if checkHorizontal(board) or checkRow(board) or checkDiagonal(board):
        return True
    return False


while gameRunning:
    printBoard(Board)

    # Player turn
    playerInput(Board)

    # Check if player won or tie
    if checkWin(Board):
        printBoard(Board)
        print(f"Winner is: {winner}")
        gameRunning = False
        break

    if checkTie(Board):
        printBoard(Board)
        print("It's a tie!")
        gameRunning = False
        break

    # Computer turn
    computerMove(Board)

    # Check if computer won or tie
    if checkWin(Board):
        printBoard(Board)
        print(f"Winner is: {winner}")
        gameRunning = False
        break

    if checkTie(Board):
        printBoard(Board)
        print("It's a tie!")
        gameRunning = False
        break
