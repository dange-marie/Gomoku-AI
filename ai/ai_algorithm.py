import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.data_structure import gomoku

def minimax(board: gomoku, depth: int, maximizingPlayer: bool, alpha: int, beta: int):
    if depth == 0 or not board.no_win():
        return board.score(maximizingPlayer)

    if maximizingPlayer:
        maxEval = float('-inf')
        for move in board.get_moves(True):
            board.set_move(move[0], move[1], board.player1)
            eval = minimax(board, depth - 1, False, alpha, beta)
            board.undo_move(move[0], move[1])
            maxEval = max(maxEval, eval)
            alpha = max(alpha, maxEval)
            if alpha <= beta:
                break
        return maxEval
    else:
        minEval = float('inf')
        for move in board.get_moves(False):
            board.set_move(move[0], move[1], board.player2)
            eval = minimax(board, depth - 1, True, alpha, beta)
            board.undo_move(move[0], move[1])
            minEval = min(minEval, eval)
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval

def respond_to_three(board: list, i: int, j: int, player: str, size_x: int, size_y: int) -> list:
    if ((i > 0 and i <= size_y-4) and
        board[i+1][j] == player and
        board[i+2][j] == player and
        board[i-1][j] == ' ' and
        board[i+3][j] == ' '):
        return [j, i-1]
    if ((j > 0 and j <= size_x-4) and
        board[i][j+1] == player and
        board[i][j+2] == player and
        board[i][j-1] == ' ' and
        board[i][j+3] == ' '):
        return [j-1, i]
    if ((i > 0 and i <= size_y-4 and j > 0 and j <= size_x-4) and
        board[i+1][j+1] == player and
        board[i+2][j+2] == player and
        board[i-1][j-1] == ' ' and
        board[i+3][j+3] == ' '):
        return [j-1, i-1]
    if ((i > 0 and i <= size_y-4 and j > 3 and j <= size_x-1) and
        board[i+1][j-1] == player and
        board[i+2][j-2] == player and
        board[i-1][j+1] == ' ' and
        board[i+3][j-3] == ' '):
        return [j+1, i-1]
    return []

def respond_to_four(board: list, i: int, j: int, player: str, size_x: int, size_y: int) -> list:
    if ((i > 0 and i <= size_y-5) and
        board[i+1][j] == player and
        board[i+2][j] == player and
        board[i+3][j] == player):
        if board[i-1][j] == ' ':
            return [j, i-1]
        if board[i+4][j] == ' ':
            return [j, i+4]
    if ((j > 0 and j <= size_x-5) and
        board[i][j+1] == player and
        board[i][j+2] == player and
        board[i][j+3] == player):
        if board[i][j-1] == ' ':
            return [j-1, i]
        if board[i][j+4] == ' ':
            return [j+4, i]
    if ((i > 0 and i <= size_y-5 and j > 0 and j <= size_x-5) and
        board[i+1][j+1] == player and
        board[i+2][j+2] == player and
        board[i+3][j+3] == player):
        if board[i-1][j-1] == ' ':
            return [j-1, i-1]
        if board[i+4][j+4] == ' ':
            return [j+4, i+4]
    if ((i > 0 and i <= size_y-5 and j >= 5) and
        board[i+1][j-1] == player and
        board[i+2][j-2] == player and
        board[i+3][j-3] == player):
        if board[i-1][j+1] == ' ':
            return [j+1, i-1]
        if board[i+4][j-4] == ' ':
            return [j-4, i+4]
    return []

def respond_to_cheating(board: list, y: int, x: int, player, size_x: int, size_y: int):
    need = 0
    block = []
    if x > 0 and x <= size_x - 5 and board[y][x-1] == ' ' and board[y][x+4] == ' ':
        if (board[y][x+1] == player and 
            board[y][x+2] == ' ' and
            board[y][x+3] == player):
            return [x+2, y]
        if (board[y][x+1] == ' ' and 
            board[y][x+2] == player and
            board[y][x+3] == player):
            return [x+1, y]
        if (board[y][x+1] == player and 
            board[y][x+2] == player and
            board[y][x+3] == ' '):
            return [x+3, y]
    if y > 0 and y <= size_y - 5 and board[y-1][x] == ' ' and board[y+4][x] == ' ':
        if (board[y+1][x] == player and 
            board[y+2][x] == ' ' and
            board[y+3][x] == player):
            return [x, y+2]
        if (board[y+1][x] == ' ' and 
            board[y+2][x] == player and
            board[y+3][x] == player):
            return [x, y+1]
        if (board[y+1][x] == player and 
            board[y+2][x] == player and
            board[y+3][x] == ' '):
            return [x, y+3]
    if x > 0 and y > 0 and x <= size_x - 5 and y <= size_y - 5 and board[y-1][x-1] == ' ' and board[y+4][x+4] == ' ':
        if (board[y+1][x+1] == player and 
            board[y+2][x+2] == ' ' and
            board[y+3][x+3] == player):
            return [x+2, y+2]
        if (board[y+1][x+1] == ' ' and
            board[y+2][x+2] == player and
            board[y+3][x+3] == player):
            return [x+1, y+1]
        if (board[y+1][x+1] == player and
            board[y+2][x+2] == player and
            board[y+3][x+3] == ' '):
            return [x+3, y+3]
    if x <= size_y-1 and x >= 4 and y > 0 and y <= size_y - 5 and board[y-1][x+1] == ' ' and board[y+4][x-4] == ' ':
        if (board[y+1][x-1] == player and 
            board[y+2][x-2] == ' ' and
            board[y+3][x-3] == player):
            return [x-2, y+2]
        if (board[y+1][x-1] == ' ' and
            board[y+2][x-2] == player and
            board[y+3][x-3] == player):
            return [x-1, y+1]
        if (board[y+1][x-1] == player and
            board[y+2][x-2] == player and
            board[y+3][x-3] == ' '):
            return [x-3, y+3]
    return []

def respond_to_cross(board: list, i: int, j: int, player: str, size_x: int, size_y: int):
    if ((j <= size_x - 3 and i <= size_y-3) and
        board[i+2][j] == player and
        board[i+1][j-1] == player and
        board[i+1][j+1] == player and
        board[i+1][j] == ' '):
            return [j, i+1]
    return []

def respond_to_final_win(board: list, i: int, j: int, player: str, size_x: int, size_y: int):
    streak = 0
    failed = False
    res = []
    for k in range(1, 5):
        if j+k > size_x:
            failed = True
            break
        if board[i][j+k] == player:
            streak += 1
        if board[i][j+k] == ' ':
            res = [j+k, i]
    if not failed and streak == 3:
        return res
    streak = 0
    failed = False
    res = []
    for k in range(1, 5):
        if i+k > size_y:
            failed = True
            break
        if board[i+k][j] == player:
            streak += 1
        if board[i+k][j] == ' ':
            res = [j, i+k]
    if not failed and streak == 3:
        return res
    streak = 0
    failed = False
    res = []
    for k in range(1, 5):
        if i+k > size_y or j+k > size_x:
            failed = True
            break
        if board[i+k][j+k] == player:
            streak += 1
        if board[i+k][j+k] == ' ':
            res = [j+k, i+k]
    if not failed and streak == 3:
        return res
    streak = 0
    failed = False
    res = []
    for k in range(1, 5):
        if i+k > size_y or j-k < 0:
            failed = True
            break
        if board[i+k][j-k] == player:
            streak += 1
        if board[i+k][j-k] == ' ':
            res = [j-k, i+k]
    if not failed and streak == 3:
        return res
    return []

def is_obvious_move(gmk: gomoku) -> list:
    dic = {"win_4": [], "win_3": [], "lose_4": [], "lose_3": [], "cheat_3": [], "cross": [], "final_cheat": []}
    for i in range(gmk.y+1):
        for j in range(gmk.x+1):
            if gmk.board[i][j] == gmk.player2:
                move = respond_to_three(gmk.board, i, j, gmk.player2, gmk.x, gmk.y)
                if len(move) != 0:
                    dic["lose_3"] = move
                move = respond_to_four(gmk.board, i, j, gmk.player2, gmk.x, gmk.y)
                if len(move) != 0:
                    dic['lose_4'] = move
                move = respond_to_cheating(gmk.board, i, j, gmk.player2, gmk.x, gmk.y)
                if len(move) != 0:
                    dic['cheat_3'] = move
                move = respond_to_cross(gmk.board, i, j, gmk.player2, gmk.x, gmk.y)
                if len(move) != 0:
                    dic['cross'] = move
                move = respond_to_final_win(gmk.board, i, j, gmk.player2, gmk.x, gmk.y)
                if len(move) != 0:
                    dic['final_cheat'] = move
            if gmk.board[i][j] == gmk.player1:
                move = respond_to_three(gmk.board, i, j, gmk.player1, gmk.x, gmk.y)
                if len(move) != 0:
                    dic["win_3"] = move
                move = respond_to_four(gmk.board, i, j, gmk.player1, gmk.x, gmk.y)
                if len(move) != 0:
                    dic['win_4'] = move
                move = respond_to_cross(gmk.board, i, j, gmk.player1, gmk.x, gmk.y)
                if len(move) != 0:
                    dic['cross'] = move
    if len(dic['win_4']) != 0:
        return dic['win_4']
    elif len(dic['lose_4']) != 0:
        return dic['lose_4']
    elif len(dic['final_cheat']) != 0:
        return dic['final_cheat']
    elif len(dic['win_3']) != 0:
        return dic['win_3']
    elif len(dic['lose_3']) != 0:
        return dic['lose_3']
    elif len(dic['cheat_3']) != 0:
        return dic['cheat_3']
    elif len(dic['cross']) != 0:
        return dic['cross']
    return []

def best_move(board: gomoku, depth: int):
    if not board.start:
        return [board.x//2, board.y//2]
    bestMove = [0, 0]
    bestEval = float('-inf')
    res = is_obvious_move(board)
    if len(res) != 0:
        return res
    for move in board.get_moves(True):
        board.set_move(move[0], move[1], board.player1)
        eval = minimax(board, depth - 1, True, float("-inf"), float("inf"))
        board.undo_move(move[0], move[1])
        if eval > bestEval:
            bestEval = eval
            bestMove = move
    return bestMove