
N = 8  # Size of the board

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n" + "-" * 16 + "\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False
    return True

def solve(board, row):
    if row == N:
        print_board(board)
        return True  # To find only one solution, return True here
        # To find all solutions, comment this line and let it continue

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True  # To find only one solution
            board[row][col] = 0  # Backtrack
    return False

# Initialize board
board = [[0 for _ in range(N)] for _ in range(N)]

# Start solving
solve(board, 0)
