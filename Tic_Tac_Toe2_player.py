from tkinter import *
import sys
from tkinter import messagebox

root = Tk()

#make font size larger

#initialize variables
x_or_o = 1
board = [['0','1','2'],
         ['3','4','5'],
         ['6','7','8'],
         ]
counter = 0

def check_win():
#check rows
    for column in range(3):
        if board[column][0] == board[column][1] and board[column][0] == board[column][2]:
            return True
#check columns
    for row in range(3):
        if board[0][row] == board[1][row] and board[0][row] == board[2][row]:
            return True
#check diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            return True
    if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
            return True
    return False

#if someone wins a popup asking to quit or play again shows up
def win_popup():
    global button00
    global button01
    global button02
    global button10
    global button11
    global button12
    global button20
    global button21
    global button22
    global board
    global counter
    
    win = messagebox.askyesno('Winner!', 'Would you like to play again?')
    if win == 0:
        sys.exit()
    elif win == 1:
        board = [['0','1','2'],
            ['3','4','5'],
            ['6','7','8'],
            ]
        counter = 0
    button00 = Button(root, text='', padx=50, pady=50, command=click00)
    button01 = Button(root, text='', padx=50, pady=50, command=click01)
    button02 = Button(root, text='', padx=50, pady=50, command=click02)
    button10 = Button(root, text='', padx=50, pady=50, command=click10)
    button11 = Button(root, text='', padx=50, pady=50, command=click11)
    button12 = Button(root, text='', padx=50, pady=50, command=click12)
    button20 = Button(root, text='', padx=50, pady=50, command=click20)
    button21 = Button(root, text='', padx=50, pady=50, command=click21)
    button22 = Button(root, text='', padx=50, pady=50, command=click22)

    button00.grid(row=0, column=0)
    button01.grid(row=0, column=1)
    button02.grid(row=0, column=2)
    button10.grid(row=1, column=0)
    button11.grid(row=1, column=1)
    button12.grid(row=1, column=2)
    button20.grid(row=2, column=0)
    button21.grid(row=2, column=1)
    button22.grid(row=2, column=2)

def tie_popup():
    global button00
    global button01
    global button02
    global button10
    global button11
    global button12
    global button20
    global button21
    global button22
    global board
    global counter
    
    tie = messagebox.askyesno('Tie', 'Would you like to play again?')
    if tie == 0:
        sys.exit()
    elif tie == 1:
        board = [['0','1','2'],
            ['3','4','5'],
            ['6','7','8'],
            ]
        counter = 0
    button00 = Button(root, text='', padx=50, pady=50, command=click00)
    button01 = Button(root, text='', padx=50, pady=50, command=click01)
    button02 = Button(root, text='', padx=50, pady=50, command=click02)
    button10 = Button(root, text='', padx=50, pady=50, command=click10)
    button11 = Button(root, text='', padx=50, pady=50, command=click11)
    button12 = Button(root, text='', padx=50, pady=50, command=click12)
    button20 = Button(root, text='', padx=50, pady=50, command=click20)
    button21 = Button(root, text='', padx=50, pady=50, command=click21)
    button22 = Button(root, text='', padx=50, pady=50, command=click22)

    button00.grid(row=0, column=0)
    button01.grid(row=0, column=1)
    button02.grid(row=0, column=2)
    button10.grid(row=1, column=0)
    button11.grid(row=1, column=1)
    button12.grid(row=1, column=2)
    button20.grid(row=2, column=0)
    button21.grid(row=2, column=1)
    button22.grid(row=2, column=2)

def click00():
    global x_or_o
    global button00
    global counter
    counter += 1
    button00.grid_forget()

    if x_or_o % 2 == 0:
        label = Label(root, text='X', padx=27, pady=23, font=('Arial', 50)).grid(row=0, column=0)
        board[0][0] = 'X'
    else:
        label = Label(root, text='O', padx=27, pady=23, font=('Arial', 50)).grid(row=0, column=0)
        board[0][0] = 'O'
    x_or_o += 1
    #check to see if someone won
    if check_win() == True:
        win_popup()
    elif counter == 9:
        tie_popup()

def click01():
    global x_or_o
    global button01
    global counter
    counter += 1
    button01.grid_forget()

    if x_or_o % 2 == 0:
        label1 = Label(root, text='X', padx=27, pady=23, font=('Arial', 50)).grid(row=0, column=1)
        board[0][1] = 'X'
    else:
        label1 = Label(root, text='O', padx=27, pady=23, font=('Arial', 50)).grid(row=0, column=1)
        board[0][1] = 'O'
    x_or_o += 1
    #check to see if someone won
    if check_win() == True:
        win_popup()
    elif counter == 9:
        tie_popup()

def click02():
    global x_or_o
    global button02
    global counter
    counter += 1
    button02.grid_forget()

    if x_or_o % 2 == 0:
        label1 = Label(root, text='X', padx=27, pady=23, font=('Arial', 50)).grid(row=0, column=2)
        board[0][2] = 'X'
    else:
        label1 = Label(root, text='O', padx=27, pady=23, font=('Arial', 50)).grid(row=0, column=2)
        board[0][2] = 'O'
    x_or_o += 1
    #check to see if someone won
    if check_win() == True:
        win_popup()
    elif counter == 9:
        tie_popup()

def click10():
    global x_or_o
    global button10
    global counter
    counter += 1
    button10.grid_forget()

    if x_or_o % 2 == 0:
        label1 = Label(root, text='X', padx=27, pady=23, font=('Arial', 50)).grid(row=1, column=0)
        board[1][0] = 'X'
    else:
        label1 = Label(root, text='O', padx=27, pady=23, font=('Arial', 50)).grid(row=1, column=0)
        board[1][0] = 'O'
    x_or_o += 1
    #check to see if someone won
    if check_win() == True:
        win_popup()
    elif counter == 9:
        tie_popup()

def click11():
    global x_or_o
    global button11
    global counter
    counter += 1
    button11.grid_forget()

    if x_or_o % 2 == 0:
        label1 = Label(root, text='X', padx=27, pady=23, font=('Arial', 50)).grid(row=1, column=1)
        board[1][1] = 'X'
    else:
        label1 = Label(root, text='O', padx=27, pady=23, font=('Arial', 50)).grid(row=1, column=1)
        board[1][1] = 'O'
    x_or_o += 1
    #check to see if someone won
    if check_win() == True:
        win_popup()
    elif counter == 9:
        tie_popup()

def click12():
    global x_or_o
    global button12
    global counter
    counter += 1
    button12.grid_forget()

    if x_or_o % 2 == 0:
        label1 = Label(root, text='X', padx=27, pady=23, font=('Arial', 50)).grid(row=1, column=2)
        board[1][2] = 'X'
    else:
        label1 = Label(root, text='O', padx=27, pady=23, font=('Arial', 50)).grid(row=1, column=2)
        board[1][2] = 'O'
    x_or_o += 1
    #check to see if someone won
    if check_win() == True:
        win_popup()
    elif counter == 9:
        tie_popup()

def click20():
    global x_or_o
    global button20
    global counter
    counter += 1
    button20.grid_forget()

    if x_or_o % 2 == 0:
        label1 = Label(root, text='X', padx=27, pady=23, font=('Arial', 50)).grid(row=2, column=0)
        board[2][0] = 'X'
    else:
        label1 = Label(root, text='O', padx=27, pady=23, font=('Arial', 50)).grid(row=2, column=0)
        board[2][0] = 'O'
    x_or_o += 1
    #check to see if someone won
    if check_win() == True:
        win_popup()
    elif counter == 9:
        tie_popup()

def click21():
    global x_or_o
    global button21
    global counter
    counter += 1
    button21.grid_forget()

    if x_or_o % 2 == 0:
        label1 = Label(root, text='X', padx=27, pady=23, font=('Arial', 50)).grid(row=2, column=1)
        board[2][1] = 'X'
    else:
        label1 = Label(root, text='O', padx=27, pady=23, font=('Arial', 50)).grid(row=2, column=1)
        board[2][1] = 'O'
    x_or_o += 1
    #check to see if someone won
    if check_win() == True:
        win_popup()
    elif counter == 9:
        tie_popup()

def click22():
    global x_or_o
    global button22
    global counter
    counter += 1
    button22.grid_forget()

    if x_or_o % 2 == 0:
        label1 = Label(root, text='X', padx=27, pady=23, font=('Arial', 50)).grid(row=2, column=2)
        board[2][2] = 'X'
    else:
        label1 = Label(root, text='O', padx=27, pady=23, font=('Arial', 50)).grid(row=2, column=2)
        board[2][2] = 'O'
    x_or_o += 1
    #check to see if someone won
    if check_win() == True:
        win_popup()
    elif counter == 9:
        tie_popup()

def play():
    button00 = Button(root, text='', padx=50, pady=50, command=click00)
    button01 = Button(root, text='', padx=50, pady=50, command=click01)
    button02 = Button(root, text='', padx=50, pady=50, command=click02)
    button10 = Button(root, text='', padx=50, pady=50, command=click10)
    button11 = Button(root, text='', padx=50, pady=50, command=click11)
    button12 = Button(root, text='', padx=50, pady=50, command=click12)
    button20 = Button(root, text='', padx=50, pady=50, command=click20)
    button21 = Button(root, text='', padx=50, pady=50, command=click21)
    button22 = Button(root, text='', padx=50, pady=50, command=click22)

    button00.grid(row=0, column=0)
    button01.grid(row=0, column=1)
    button02.grid(row=0, column=2)
    button10.grid(row=1, column=0)
    button11.grid(row=1, column=1)
    button12.grid(row=1, column=2)
    button20.grid(row=2, column=0)
    button21.grid(row=2, column=1)
    button22.grid(row=2, column=2)

    root.mainloop()