import numpy as np
rowCount = 5
colCount = 5

def creatBoard ():
    return np.zeros((rowCount, colCount))

def dropDisc(board, row, col, disc):
    board[row][col] = disc

def is_valid_location(board, col):
    return board[rowCount - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(rowCount):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, disc):
    # Check horizontal locations
    for c in range(colCount-3):
        for r in range(rowCount):
            if board[r][c] == disc and board[r][c+1] == disc and board[r][c+2] == disc and board[r][c+3] == disc:
                return True

    # Check vertical locations
    for c in range(colCount):
        for r in range(rowCount-3):
            if board[r][c] == disc and board[r+1][c] == disc and board[r+2][c] == disc and board[r+3][c] == disc:
                return True


    # Check positively sloped diagonals
    for c in range(colCount-3):
        for r in range(rowCount-3):
            if board[r][c] == disc and board[r+1][c+1] == disc and board[r+2][c+2] == disc and board[r+3][c+3] == disc:
                return True

    # Check negatively sloped diagonals
    for c in range(colCount-3):
        for r in range(3, rowCount):
            if board[r][c] == disc and board[r-1][c+1] == disc and board[r-2][c+2] == disc and board[r-3][c+3] == disc:
                return True


board = creatBoard()
print_board(board)
game_over = False
turn = 1



while not game_over:
    # Ask for Player 1 input
    if turn == 1:
        col = int(input("Player 1 make your selection (0-5):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            dropDisc(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 wins!")
                game_over = True

        # Ask for Player 2 input
    else:
            col = int(input("Player 2 make your selection (0-5):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                dropDisc(board, row, col, 2)

                if winning_move(board, 2):
                    print("Player 2 wins!")
                    game_over = True

    print_board(board)
    turn = (turn+1) % 2


