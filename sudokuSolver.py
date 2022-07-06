# importing tkinter for gui creation
from tkinter import *

# creating gui root widget
root = Tk()
root.title("SUDOKU SOLVER")
root.configure(background='#202020')

# defining an empty sudoku list
sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# heading label
myLabel = Label(root, text="Fill in Numbers & click Solve ", width=33, font = ('courier', 15, 'bold'), fg="#fff", bg="#202020").grid(row=0, column=0, columnspan= 9, pady=10)

# creating an empty dictionary to store variables 
var_holder = {}

# creating a function to solve when clicked on the button
def solveSudoku() :

    # adding inputs to the sudoku list
    for i in range(9):
        for j in range(9):
            sudoku[i][j] = var_holder['inp' + str(i+1) + str(j)].get()
    
    # printing the the sudoku matrix without using numpy
    def puzzle(a):
        for i in range(9):
            for j in range(9):
                print(a[i][j],end = " ")
            print()

    # creating a function to check the possibility of a correct answer at a particular position 
    def solve(sudoku, row, col, num):

        # does the number appear in the row ?
        for x in range(9):
            if int(sudoku[row][x]) == num:
                return False

        # does the number appear in the column ?
        for x in range(9):
            if int(sudoku[x][col]) == num:
                return False

        # does the number appear in the 3X3 square box ?
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if int(sudoku[i + startRow][j + startCol]) == num:
                    return False

        return True

    # creating a function to check the correct answer 
    def Suduko(sudoku, row, col):

        if (row == 9 - 1 and col == 9):
            return True
        if col == 9:
            row += 1
            col = 0
        if int(sudoku[row][col]) > 0: 
            return Suduko(sudoku, row, col + 1)
        for num in range(1, 9 + 1, 1): 
        
            if solve(sudoku, row, col, num):
                sudoku[row][col] = num
                if Suduko(sudoku, row, col + 1):
                    return True
            sudoku[row][col] = 0
        return False

    # if the sudoku is solvable
    if (Suduko(sudoku, 0, 0)):

        # printing the resfreshed empty sudoku
        var_holder_ = {}
        for _ in range(9):
            for __ in range(9):
                var_holder_['inpt' + str(_+1) + str(__)] = Entry(root, width=3, justify=CENTER, font = ('courier', 15, 'bold'), bg="#3cb043")
                var_holder_['inpt' + str(_+1) + str(__)].grid(row=_+1, column=__, columnspan=1, ipady=5, padx=3, pady=3)
                var_holder_['inpt' + str(_+1) + str(__)].insert(0, sudoku[_][__])
        btn = Button(root, text="IT'S SOLVED, AGAIN?", command=init, width=33, font = ('courier', 15, 'bold'), fg="#fff", bg="#000").grid(row=11, column=0, columnspan= 9, pady=10)

    # if the sudoku is not solvable the program hangs
    else:
        for _ in range(9):
            for __ in range(9):
                var_holder_['inpt' + str(_) + str(__)] = Entry(root, width=3, justify=CENTER, font = ('courier', 15, 'bold'), bg="#ff6961")

# defining an initialisation function to clear the sudoku list
def init():

    # printing the resfreshed empty sudoku
    for _ in range(9):
        for __ in range(9):

            var_holder['inp' + str(_+1) + str(__)] = Entry(root, width=3, justify=CENTER, font = ('courier', 15, 'bold'), bg="#aec6cf")
            var_holder['inp' + str(_+1) + str(__)].grid(row=_+1, column=__, columnspan=1, ipady=5, padx=3, pady=3)
            var_holder['inp' + str(_+1) + str(__)].insert(0, 0)

            locals().update(var_holder)

    # refresh button to restart with an empty sudoku list
    btn = Button(root, text="SOLVE SUDOKU", command=solveSudoku, width=33, font = ('courier', 15, 'bold'), fg="#fff", bg="#000").grid(row=11, column=0, columnspan= 9, pady=10)

# calling the initialisation function
init()

# solve button which calls the whole function of the sudoku solving code
btn = Button(root, text="SOLVE SUDOKU", command=solveSudoku, width=33, font = ('courier', 15, 'bold'), fg="#fff", bg="#000").grid(row=11, column=0, columnspan= 9, pady=10)

# creating a while loop to continously show the frame
root.mainloop()