import tkinter as tk
from tic_tac_toe.logic import *




def new_game():
    '''
        Рестарт игры.
    '''
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'cyan'

def click(row, col):
    '''
        Запускает игру, после того, как пользователь выберет, куда поставить первым 0. Логика игры берется из модуля
        logic.py . После выбора точки дальше играет компьютер сам с собой.
    '''
    player1 = 'X'
    player2 = 'O'
    field[row][col]['text'] = player2
    while True:
        if moving(field) is False:
            break
        game(field, player1, player2)
        game(field, player2, player1)

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Крестики-нолики')
    field = []
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