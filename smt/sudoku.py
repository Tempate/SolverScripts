from z3 import Int, Solver, Distinct, sat
import math


SUDOKU = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solver = Solver()

# Set up a 9x9 board
board = [[Int(f'x_{i+1}{j+1}') for j in range(9)] for i in range(9)]

# Each cell must be a number between 1 and 9
for i in range(9):
    for j in range(9):
        solver.add(board[i][j] >= 1, board[i][j] <= 9)

# The numbers in each row must be distinct 
for i in range(9):
    solver.add(Distinct(board[i]))

# The numbers in each column must be distinct
for j in range(9):
    col = [board[i][j] for i in range(9)]

    solver.add(Distinct(col))

# The numbers in each block must be distinct 
for a in range(3):
    for b in range(3):
        block = []
        for i in range(3):
            for j in range(3):
                block.append(board[3*a+i][3*b+j])

        solver.add(Distinct(block))

# Load the number requirements from the given sudoku
for i in range(9):
    for j in range(9):
        if SUDOKU[i][j] != 0:
            solver.add(board[i][j] == SUDOKU[i][j])

if solver.check() == sat:
    model = solver.model()
    print("Solution:")

    for i in range(9):
        row = " ".join(str(model[board[i][j]]) for j in range(9))
        print(row)
else:
    print("No solution")
