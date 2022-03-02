import random


def my_print(board):
    for row in board:
        print(row)
    print()


def moving(board):
    for row in range(3):
        for col in range(3):
            if (board[row][col] == '_'):
                return True
    return False


def check_win(board, player1, player2):

    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            if (board[row][0] == player1):
                return 10
            elif (board[row][0] == player2):
                return -10

    for col in range(3):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]):
            if (board[0][col] == player1):
                return 10
            elif (board[0][col] == player2):
                return -10

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if (board[0][0] == player1):
            return 10
        elif (board[0][0] == player2):
            return -10

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if (board[0][2] == player1):
            return 10
        elif (board[0][2] == player2):
            return -10

    return 0


def minimax(board, isMax, player1, player2):
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
                if (board[row][col] == '_'):
                    board[row][col] = player1
                    best = max(best, minimax(board, not isMax, player1, player2))
                    board[row][col] = '_'
        return best
    else:
        best = 1000
        for row in range(3):
            for col in range(3):
                if (board[row][col] == '_'):
                    board[row][col] = player2
                    best = min(best, minimax(board, not isMax, player1, player2))
                    board[row][col] = '_'
        return best


def game(board, player1, player2):
    bestVal = -1000
    bestMove = (-1, -1)
    for row in range(3):
        for col in range(3):
            if (board[row][col] == '_'):
                board[row][col] = player1
                moveVal = minimax(board, False, player1, player2)
                board[row][col] = '_'
                if (moveVal > bestVal):
                    bestMove = (row, col)
                    bestVal = moveVal
    board[bestMove[0]][bestMove[1]] = player1


board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']]


if __name__ == '__main__':
    player, opponent = 'x', 'o'
    board[random.randint(0,2)][random.randint(0,2)] = opponent
    my_print(board)
    while True:
        value = check_win(board, player, opponent)
        if moving(board) is False:
            break
        game(board, player, opponent)
        my_print(board)
        game(board, opponent, player)
        my_print(board)
