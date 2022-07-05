# importing tkinter for gui creation
from tkinter import *

# creating gui root widget
root =  Tk()

# printing the the sudoku matrix without using numpy
def puzzle(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j],end = " ")
        print()

# creating a function to check the possibility of a correct answer at a particular position 
def solve(grid, row, col, num):

    # does the number appear in the row ?
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    # does the number appear in the colomn ? 
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    # does the number appear in the given square?
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
# creating a function to check the correct answer 
def Suduko(grid, row, col):
 
    if (row == 9 - 1 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, 9 + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

# creating a list named as grid with sudoku game input
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]

# printing the grid
print("\n")
print("UNSOLVED SUDOKU: ")
puzzle(grid)
 
if (Suduko(grid, 0, 0)):
    print("\n")
    print("SOLVED SUDOKU: ")
    puzzle(grid)
    print("\n")
else:
    print("Solution does not exist:(")