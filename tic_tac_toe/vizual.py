import tkinter as tk
from tic_tac_toe.logic import *


window = tk.Tk()
window.title('Крестики-нолики')
field = []

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'cyan'

def click(row, col):
    player1 = 'X'
    player2 = 'O'
    field[row][col]['text'] = player2
    while True:
        if moving(field) is False:
            break
        game(field, player1, player2)
        game(field, player2, player1)


for row in range(3):
    line = []
    for col in range(3):
        button = tk.Button(window, text=' ', width=4, height=2,
                           font=('Verdana', 20, 'bold'),
                           background='cyan',
                           command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = tk.Button(window, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

window.mainloop()