# importing numpy for matrix and array calculations
import numpy as np

# creating a list named as grid with sudoku game input
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

# printing the grid
print(np.matrix(grid))

# creating a function to check the possibility of a correct answer at a particular position 
def possible(row, column, number):

    global grid

    # does the number appear in the row ? 
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    # does the number appear in the colomn ?
    for i in range(0,9):
        if grid[i][column] == number:
            return False

    # does the number appear in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3

    for i in range(0, 3):
        for i in range(0, 3):
            if grid[y0 + i][x0 + i] == number:
                return False

    return True 

# creating a function to check the correct answer 
def solve():

    global grid

    # checking the possibility of the correct sudoku
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    
                    # calling the possible function 
                    if possible(row, column, number):
                        grid[row][column] = number

                        # calling the solve function (recursion)
                        solve()
    
    # printing the solved sudoku
    print(np.matrix(grid))

# calling the solve function
solve()
