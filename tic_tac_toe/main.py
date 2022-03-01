import random

board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

def moving(board):
    for row in board:
        if '_' in row:
            return True
    return False


def check_win(board, player1, player2):
    for row in range(0, 3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == player1:
                return 10
            elif board[row][0] == player2:
                return -10

    for col in range(0, 3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == player1:
                return 10
            elif board[0][col] == player2:
                return -10

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if board[0][0] == player1:
            return 10
        elif board[0][0] == player2:
            return -10

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if board[0][2] == player1:
            return 10
        elif board[0][2] == player2:
            return -10
    return 0


def minimax(board, ismax, player1, player2):
    score = check_win(board, player1, player2)

    if score == 10:
        return score

    if score == -10:
        return score

    if moving(board) is False:
        return 0

    if ismax:
        best = - 1500
        for row in board:
            for col in row:
                if board[row][col] == '_':
                    board[row][col] = player1
                    best = max(best, minimax(board, not ismax, player1, player2))
                    board[row][col] = '_'
        return best
    else:
        best = 1500
        for row in board:
            for col in row:
                if board[row][col] == '_':
                    board[row][col] = player2
                    best = min(best, minimax(board, not ismax, player1, player2))
                    board[row][col] = '_'
        return best


def best(board, player1, player2):
    bestVal = -1500
    bestMove = (-1, -1)
    for row in board:
        for col in row:
            if board[row][col] == '_':
                board[row][col] = player1
                currentVal = minimax(board, True, player1, player2)
                board[row][col] = '_'
                if currentVal > bestVal:
                    bestVal = currentVal
                    bestMove = (row, col)
    return bestMove




