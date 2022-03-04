import random


def my_print(board):
    for row in board:
        print(row)
    print()


def moving(board):
    '''
        Проверка возможности сделать ход.
    '''
    for row in range(3):
        for col in range(3):
            if (board[row][col]['text'] == ' '):
                return True
    return False


def check_win(board, player1, player2):
    '''
        Проверка на конец игры (победа/проигрыш/ничья). Возвращает 10 очков, если победил player1, -10 очков для player2,
        при ничье вернет 0 очков.
    '''
    for row in range(3):
        if (board[row][0]['text'] == board[row][1]['text'] and board[row][1]['text'] == board[row][2]['text']):
            if (board[row][0]['text'] == player1):
                return 10
            elif (board[row][0]['text'] == player2):
                return -10

    for col in range(3):
        if (board[0][col]['text'] == board[1][col]['text'] and board[1][col]['text'] == board[2][col]['text']):
            if (board[0][col]['text'] == player1):
                return 10
            elif (board[0][col]['text'] == player2):
                return -10

    if (board[0][0]['text'] == board[1][1]['text'] and board[1][1]['text'] == board[2][2]['text']):
        if (board[0][0]['text'] == player1):
            return 10
        elif (board[0][0]['text'] == player2):
            return -10

    if (board[0][2]['text'] == board[1][1]['text'] and board[1][1]['text'] == board[2][0]['text']):
        if (board[0][2]['text'] == player1):
            return 10
        elif (board[0][2]['text'] == player2):
            return -10

    return 0


def minimax(board, isMax, player1, player2):
    '''
        Функция, реализующая алгоритм максимум и минимум для крестики-нолики. При переборе всех возможных комбинаций
        игры. Возвращает количество очков в конце игры для каждой комбинации.
    '''
    score = check_win(board, player1, player2)

    if (score == 10):
        return score

    if (score == -10):
        return score

    if (moving(board) == False):
        return 0

    if (isMax):
        best = -1000
        for row in range(3):
            for col in range(3):
                if (board[row][col]['text'] == ' '):
                    board[row][col]['text'] = player1
                    best = max(best, minimax(board, not isMax, player1, player2))
                    board[row][col]['text'] = ' '
        return best
    else:
        best = 1000
        for row in range(3):
            for col in range(3):
                if (board[row][col]['text'] == ' '):
                    board[row][col]['text'] = player2
                    best = min(best, minimax(board, not isMax, player1, player2))
                    board[row][col]['text'] = ' '
        return best


def game(board, player1, player2):
    '''
        Функция, которая выполняет ход, который приводит к победе/ничье player1.
    '''
    bestVal = -1000
    bestMove = (-1, -1)
    for row in range(3):
        for col in range(3):
            if (board[row][col]['text'] == ' '):
                board[row][col]['text'] = player1
                moveVal = minimax(board, False, player1, player2)
                board[row][col]['text'] = ' '
                if (moveVal > bestVal):
                    bestMove = (row, col)
                    bestVal = moveVal
    board[bestMove[0]][bestMove[1]]['text'] = player1


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']]


if __name__ == '__main__':
    player, opponent = 'x', 'o'
    board[random.randint(0,2)][random.randint(0,2)] = opponent # Первый ход делается рандомом для opponent.
    my_print(board)
    while True:
        if moving(board) is False:
            break
        game(board, player, opponent)
        my_print(board)
        game(board, opponent, player)
        my_print(board)