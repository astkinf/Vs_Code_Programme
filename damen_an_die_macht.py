def check(board, nextY):
    nextX = len(board)
    for i in range(0, nextX):
        if nextY == board[i] or (nextX - i) == abs(nextY - board[i]):
            return False
    else:
            return True

def solve(it = 0, board = []):
    if it == queens - 1:
        for d in range(0, queens):
            if check(board, d):
                draw_board(board + [d])
                print()
    else:
        for d in range(0, queens):
            if check(board, d):
                solve(it + 1, board + [d])

def draw_board(board):
    cell = "O "
    for i in board:
        print(cell * (i) + "X "+ cell * (len(board) - (i + 1)))


print("* " * 14 + "\n      Queens Problem\n" + "* " * 14)
queens = int(input("Enter number of Queens (>=4): "))
print("Calculating ways to place", queens, "QUEENS on a {n}X{n} chess board without threatening each other".format(n = str(queens)))
print("{:^40}".format("---ALL POSSIBLE SOLUTIONS---"))
solve()
