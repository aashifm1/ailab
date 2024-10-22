N = 4

def printsolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def issafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solvenqueen(board, col):
    if col >= N:
        return True
    for i in range(N):
        if issafe(board, i, col):
            board[i][col] = 1
            if solvenqueen(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solvenq():
    board = [[0, 0, 0, 0] for _ in range(N)]
    if not solvenqueen(board, 0):
        print("No solution exists")
        return False
    printsolution(board)
    return True

solvenq()
