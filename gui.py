from tkinter import *

root = Tk()

sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

var_holder = {}

for _ in range(9):
    for __ in range(9):

        var_holder['inp' + str(_) + str(__)] = Entry(root, width=4)
        var_holder['inp' + str(_) + str(__)].grid(row=_, column=__, columnspan=1)
        var_holder['inp' + str(_) + str(__)].insert(0, 0)

        locals().update(var_holder)

def puzzle(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j],end = " ")
        print()

def addNum() :
    for i in range(9):
        for j in range(9):
            sudoku[i][j] = var_holder['inp' + str(i) + str(j)].get()
    print("\n")
    print("UNSOLVED SUDOKU: ")
    puzzle(sudoku)

btn = Button(root, text="add", command=addNum).grid()

root.mainloop()