from z3 import Bool, Solver, Distinct, sat
import math

N = 10

solver = Solver()

# Set up a NxN board
board = [[Bool(f'x_{i+1}{j+1}') for j in range(N)] for i in range(N)]

# There can only be a single queen in each row 
for i in range(N):
    solver.add(sum(board[i]) == 1)

# There can only be a single queen in each column
for j in range(N):
    col = [board[i][j] for i in range(N)]

    solver.add(sum(col) == 1)

# There can only be a single queen in each diagonal
for i in range(N):
    # Check the top right diagonals
    top_diag = [board[j][N-1-i+j] for j in range(i+1)]
    solver.add(sum(top_diag) <= 1)

    # Check the bottom left diagonals
    top_diag = [board[N-1-j][i-j] for j in range(i+1)]
    solver.add(sum(top_diag) <= 1)

    # Check the top left anti-diagonals
    top_diag = [board[j][i-j] for j in range(i+1)]
    solver.add(sum(top_diag) <= 1)

    # Check the bottom right anti-diagonals
    bot_diag = [board[N-1-j][N-1-i+j] for j in range(i+1)]
    solver.add(sum(bot_diag) <= 1)

if solver.check() == sat:
    model = solver.model()
    print("Solution:")

    for i in range(N):
        row = ""

        for j in range(N):
            if model[board[i][j]]:
                row += "1 "
            else:
                row += "0 "
        
        print(row) 
else:
    print("No solution")
