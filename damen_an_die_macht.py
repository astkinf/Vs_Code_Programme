# DAS N-DAMEN PROBLEM

# Auf einem n*n Damenspielbrett müssen n Damen untergebracht werden,
# die sich waagerecht, senkrecht und diagonal nicht in die Quere kommen dürfen.
# Bsp.: 4*4
#       O X O O
#       O O O X
#       X O O O
#       O O X O

# Methode um zu checken, ob die nächste Position frei ist.
# nextY: Y Koordinate | nextX: X Koordinate
def check(board, nextY):
    nextX = len(board)
    for i in range(0, nextX):
        if nextY == board[i] or (nextX - i) == abs(nextY - board[i]):
            return False
    else:
            return True

# Rekursive Methode, um das Problem lösen zu können, mit Hilfe von Backtracking.
def solve(it = 0, board = []):
    if it == queens - 1:
        for d in range(0, queens):
            if check(board, d):
                draw_board(board + [d]) # Finales Spielbrett wird "draw_board" mitgeteilt
                print() # und ausgegeben
    else:
        for d in range(0, queens):
            if check(board, d):
                solve(it + 1, board + [d])

# Diese Methode zeichnet das Spielfeld mit "O" und "X".
def draw_board(board):
    cell = "O " # Für Felder auf denen keine Damen stehen/Lückenfüller
    for i in board:
        print(cell * (i) + "X "+ cell * (len(board) - (i + 1)))
        # Die Felder vor der Dame und dahinter werden mit "O" aufgefüllt


# Titel/Überschrift
print("* " * 14 + "\n      Queens Problem\n" + "* " * 14)
# In der Variable "queens" wird die Anzahl der Damen gespeichert, die auf dem Brett verteilt werden
# Da das Programm erst ab vier Damen das Probem lösen kann muss eine Zahl über vier eingegeben werden
queens = int(input("Enter number of Queens (>=4): "))
print("Calculating ways to place", queens, "QUEENS on a {n}X{n} chess board without threatening each other".format(n = str(queens)))
print("{:^40}".format("---ALL POSSIBLE SOLUTIONS---"))
# Methodenaufruf von "solve()"
solve()
