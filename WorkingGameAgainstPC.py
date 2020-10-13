from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

# Global Variables
ActivePlayer = 1
p1 =[] # what player 1 selected
p2 = [] # what Player 2 selected

root = Tk()
root.title("Tic Tac Toe: Player1:")

style = ttk.Style()
style.theme_use("classic")

# Add Buttons
Bu1 = ttk.Button(root, text=' ')
Bu1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
Bu1.config(command=lambda: BuClick(1))

Bu2 = ttk.Button(root, text=' ')
Bu2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
Bu2.config(command=lambda: BuClick(2))

Bu3 = ttk.Button(root, text=' ')
Bu3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
Bu3.config(command=lambda: BuClick(3))

Bu4 = ttk.Button(root, text=' ')
Bu4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
Bu4.config(command=lambda: BuClick(4))

Bu5 = ttk.Button(root, text=' ')
Bu5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
Bu5.config(command=lambda: BuClick(5))

Bu6 = ttk.Button(root, text=' ')
Bu6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
Bu6.config(command=lambda: BuClick(6))

Bu7 = ttk.Button(root, text=' ')
Bu7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
Bu7.config(command=lambda: BuClick(7))

Bu8 = ttk.Button(root, text=' ')
Bu8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
Bu8.config(command=lambda: BuClick(8))

Bu9 = ttk.Button(root, text=' ')
Bu9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
Bu9.config(command=lambda: BuClick(9))


def BuClick(id):
    global ActivePlayer
    global p1
    global p2
    if ActivePlayer == 1:
        SetLayout(id, "X")
        p1.append(id)
        root.title("Tic Tac Toe: Player 2:")
        ActivePlayer = 2
        print("P1: {}".format(p1))
        Autoplay()
    else:
        SetLayout(id, "O")
        p2.append(id)
        root.title("Tic Tac Toe: Player 1:")
        ActivePlayer = 1
        print("P2: {}".format(p2))
        Checkwinner()

def SetLayout(id, PlayerSymbol):
    if id == 1:
        Bu1.config(text=PlayerSymbol)
        Bu1.state(['disabled'])
    elif id == 2:
        Bu2.config(text=PlayerSymbol)
        Bu2.state(['disabled'])
    elif id == 3:
        Bu3.config(text=PlayerSymbol)
        Bu3.state(['disabled'])
    elif id == 4:
        Bu4.config(text=PlayerSymbol)
        Bu4.state(['disabled'])
    elif id == 5:
        Bu5.config(text=PlayerSymbol)
        Bu5.state(['disabled'])
    elif id == 6:
        Bu6.config(text=PlayerSymbol)
        Bu6.state(['disabled'])
    elif id == 7:
        Bu7.config(text=PlayerSymbol)
        Bu7.state(['disabled'])
    elif id == 8:
        Bu8.config(text=PlayerSymbol)
        Bu8.state(['disabled'])
    elif id == 9:
        Bu9.config(text=PlayerSymbol)
        Bu9.state(['disabled'])

def Checkwinner():
    Winner = -1
    if 1 in p1 and 2 in p1 and 3 in p1:
        Winner = 1
    if 1 in p2 and 2 in p2 and 3 in p2:
        Winner = 2
    if 4 in p1 and 5 in p1 and 6 in p1:
        Winner = 1
    if 4 in p2 and 5 in p2 and 6 in p2:
        Winner = 2
    if 7 in p1 and 8 in p1 and 9 in p1:
        Winner = 1
    if 7 in p2 and 8 in p2 and 9 in p2:
        Winner = 2
    if 1 in p1 and 4 in p1 and 9 in p1:
        Winner = 1
    if 1 in p2 and 4 in p2 and 9 in p2:
        Winner = 2
    if 2 in p1 and 5 in p1 and 8 in p1:
        Winner = 1
    if 2 in p2 and 5 in p2 and 8 in p2:
        Winner = 2
    if 3 in p1 and 6 in p1 and 9 in p1:
        Winner = 1
    if 3 in p2 and 6 in p2 and 9 in p2:
        Winner = 2
    if 1 in p1 and 5 in p1 and 9 in p1:
        Winner = 1
    if 1 in p2 and 5 in p2 and 9 in p2:
        Winner = 2
    if 3 in p1 and 5 in p1 and 7 in p1:
        Winner = 1
    if 3 in p2 and 5 in p2 and 7 in p2:
        Winner = 2
    if Winner == 1:
        messagebox.showinfo(title="Congratulations!", message="Player 1 is the winner")
    elif Winner == 2:
        messagebox.showinfo(title="Congratulations!", message="Player 2 is the winner")

def Autoplay():
    global p1
    global p2
    EmptyCells = []
    for cell in range(9):
        if not( cell+1 in p1 or cell+1 in p2):
            EmptyCells.append(cell+1)
    RandIndex = randint(0, len(EmptyCells)-1)
    BuClick(EmptyCells[RandIndex])


root.mainloop()