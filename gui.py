from tkinter import *

root = Tk()
root.title("SUDOKU SOLVER")
root.configure(background='#202020')

sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

myLabel = Label(root, text="Fill in Numbers & click Solve ", width=33, font = ('courier', 15, 'bold'), fg="#fff", bg="#202020").grid(row=0, column=0, columnspan= 9, pady=10)

var_holder = {}

for _ in range(9):
    for __ in range(9):

        var_holder['inp' + str(_+1) + str(__)] = Entry(root, width=3, justify=CENTER, font = ('courier', 15, 'bold'), bg="#aec6cf")
        var_holder['inp' + str(_+1) + str(__)].grid(row=_+1, column=__, columnspan=1, ipady=5, padx=3, pady=3)
        var_holder['inp' + str(_+1) + str(__)].insert(0, 0)

        locals().update(var_holder)

def addNum() :
    for i in range(9):
        for j in range(9):
            sudoku[i][j] = var_holder['inp' + str(i+1) + str(j)].get()
    
    def puzzle(a):
        for i in range(9):
            for j in range(9):
                print(a[i][j],end = " ")
            print()

    def solve(sudoku, row, col, num):

        for x in range(9):
            if int(sudoku[row][x]) == num:
                return False

        for x in range(9):
            if int(sudoku[x][col]) == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if int(sudoku[i + startRow][j + startCol]) == num:
                    return False

        return True

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

    if (Suduko(sudoku, 0, 0)):

        var_holder_ = {}
        for _ in range(9):
            for __ in range(9):
                var_holder_['inpt' + str(_+1) + str(__)] = Entry(root, width=3, justify=CENTER, font = ('courier', 15, 'bold'), bg="#77dd77")
                var_holder_['inpt' + str(_+1) + str(__)].grid(row=_+1, column=__, columnspan=1, ipady=5, padx=3, pady=3)
                var_holder_['inpt' + str(_+1) + str(__)].insert(0, sudoku[_][__])
        btn = Button(root, text="IT'S SOLVED", command=addNum, width=33, font = ('courier', 15, 'bold'), fg="#fff", bg="#000").grid(row=11, column=0, columnspan= 9, pady=10)

    else:
        for _ in range(9):
            for __ in range(9):
                var_holder_['inpt' + str(_) + str(__)] = Entry(root, width=3, justify=CENTER, font = ('courier', 15, 'bold'), bg="#ff6961")

btn = Button(root, text="SOLVE SUDOKU", command=addNum, width=33, font = ('courier', 15, 'bold'), fg="#fff", bg="#000").grid(row=11, column=0, columnspan= 9, pady=10)

root.mainloop()