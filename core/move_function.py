def four_in_a_row_a_side(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-5) and
        board[y+1][x] == p1 and
        board[y+2][x] == p1 and
        board[y+3][x] == p1 and
        (board[y-1][x] == p2 or
        board[y+4][x] == p2)):
        score += 1000
    if ((x > 0 and x <= size_x-5) and
        board[y][x+1] == p1 and
        board[y][x+2] == p1 and
        board[y][x+3] == p1 and
        (board[y][x-1] == p2 or
        board[y][x+4] == p2)):
        score += 1000
    if ((y > 0 and y <= size_y-5 and x > 0 and x <= size_x-5) and
        board[y+1][x+1] == p1 and
        board[y+2][x+2] == p1 and
        board[y+3][x+3] == p1 and
        (board[y-1][x-1] == p2 or
        board[y+4][x+4] == p2)):
        score += 1000
    if ((y <= size_y-5 and x >= 5) and
        board[y+1][x-1] == p1 and
        board[y+2][x-2] == p1 and
        board[y+3][x-3] == p1 and
        (board[y-1][x+1] == p2 or
        board[y+4][x-4] == p2)):
        score += 1000
    return score

def four_in_a_row(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-5) and
        board[y+1][x] == p1 and
        board[y+2][x] == p1 and
        board[y+3][x] == p1 and
        (board[y-1][x] == ' ' and
        board[y+4][x] == ' ')):
        score += 100000
    if ((x > 0 and x <= size_x-5) and
        board[y][x+1] == p1 and
        board[y][x+2] == p1 and
        board[y][x+3] == p1 and
        (board[y][x-1] == ' ' and
        board[y][x+4] == ' ')):
        score += 100000
    if ((y > 0 and y <= size_y-5 and x > 0 and x <= size_x-5) and
        board[y+1][x+1] == p1 and
        board[y+2][x+2] == p1 and
        board[y+3][x+3] == p1 and
        (board[y-1][x-1] == ' ' and
        board[y+4][x+4] == ' ')):
        score += 100000
    if ((y <= size_y-5 and x >= 5) and
        board[y+1][x-1] == p1 and
        board[y+2][x-2] == p1 and
        board[y+3][x-3] == p1 and
        (board[y-1][x+1] == ' ' and
        board[y+4][x-4] == ' ')):
        score += 100000
    return score

def four_in_a_row_first_case(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-5) and
        board[y+1][x] == p1 and
        board[y+2][x] == p1 and
        board[y+3][x] == p1 and
        board[y+4][x] == ' ' and
        board[y+5][x] == p1 and
        board[y-1][x] == p2):
        score += 1400
    if ((x > 0 and x <= size_x-5) and
        board[y][x+1] == p1 and
        board[y][x+2] == p1 and
        board[y][x+3] == p1 and
        board[y][x+4] == ' ' and
        board[y][x+5] == p1 and
        board[y][x-1] == p2):
        score += 1400
    if ((y > 0 and y <= size_y-5 and x > 0 and x <= size_x-5) and
        board[y+1][x+1] == p1 and
        board[y+2][x+2] == p1 and
        board[y+3][x+3] == p1 and
        board[y+4][x+4] == ' ' and
        board[y+5][x+5] == p1 and
        board[y-1][x-1] == p2):
        score += 1400
    if ((y > 0 and y <= size_y-5 and x > 0 and x <= size_x-5) and
        board[y+1][x-1] == p1 and
        board[y+2][x-2] == p1 and
        board[y+3][x-3] == p1 and
        board[y+4][x-4] == ' ' and
        board[y+5][x-5] == p1 and
        board[y-1][x+1] == p2):
        score += 1400
    return score

def three_in_a_row(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-4) and
        board[y+1][x] == p1 and
        board[y+2][x] == p1 and
        board[y-1][x] == ' ' and
        board[y+3][x] == ' '):
        score += 1000
    if ((x > 0 and x <= size_x-4) and
        board[y][x+1] == p1 and
        board[y][x+2] == p1 and
        board[y][x-1] == ' ' and
        board[y][x+3] == ' '):
        score += 1000
    if ((y > 0 and y <= size_y-4 and x > 0 and x <= size_x-4) and
        board[y+1][x+1] == p1 and
        board[y+2][x+2] == p1 and
        board[y-1][x-1] == ' ' and
        board[y+3][x+3] == ' '):
        score += 1000
    if ((y > 0 and y <= size_y-4 and x > 0 and x <= size_x-4) and
        board[y+1][x-1] == p1 and
        board[y+2][x-2] == p1 and
        board[y-1][x+1] == ' ' and
        board[y+3][x-3] == ' '):
        score += 1000
    return score

def three_in_a_row_a_side(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-3) and
        board[y+1][x] == p1 and
        board[y+2][x] == p1 and
        (board[y-1][x] == p2 or
        board[y+3][x] == p2)):
        score += 100
    if ((x > 0 and x <= size_x-3) and
        board[y][x+1] == p1 and
        board[y][x+2] == p1 and
        (board[y][x-1] == p2 or
        board[y][x+3] == p2)):
        score += 100
    if ((y > 0 and y <= size_y-3 and x > 0 and x <= size_x-3) and
        board[y+1][x+1] == p1 and
        board[y+2][x+2] == p1 and
        (board[y-1][x-1] == p2 or
        board[y+3][x+3] == p2)):
        score += 100
    if ((y > 0 and y <= size_y-3 and x > 0 and x <= size_x-3) and
        board[y+1][x-1] == p1 and
        board[y+2][x-2] == p1 and
        (board[y-1][x+1] == p2 or
        board[y+3][x-3] == p2)):
        score += 100
    return score

def three_in_a_row_first_case(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 1 and y <= size_y-6) and
        board[y+1][x] == p1 and
        board[y+2][x] == p1 and
        (board[y-2][x] == p2 or
        board[y+4][x] == p2)):
        score += 1800
    if ((x > 1 and x <= size_x-6) and
        board[y][x+1] == p1 and
        board[y][x+2] == p1 and
        (board[y][x-2] == p2 or
        board[y][x+4] == p2)):
        score += 1800
    if ((y > 1 and y <= size_y-6 and x > 1 and x <= size_x-6) and
        board[y+1][x+1] == p1 and
        board[y+2][x+2] == p1 and
        (board[y-2][x-2] == p2 or
        board[y+4][x+4] == p2)):
        score += 1800
    if ((y > 1 and y <= size_y-6 and x > 1 and x <= size_x-6) and
        board[y+1][x-1] == p1 and
        board[y+2][x-2] == p1 and
        (board[y-2][x+2] == p2 or
        board[y+4][x-4] == p2)):
        score += 1800
    return score

def three_in_a_row_second_case(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-5) and
        board[y+1][x] == p1 and
        board[y+2][x] == ' ' and
        board[y+3][x] == p1 and
        board[y-1][x] == ' ' and
        board[y+4][x] == ' '):
        score += 2000
    if ((x > 0 and x <= size_x-5) and
        board[y][x+1] == p1 and
        board[y][x+2] == ' ' and
        board[y][x+3] == p1 and
        board[y][x-1] == ' ' and
        board[y][x+4] == ' '):
        score += 2000
    if ((y > 0 and y <= size_y-5 and x > 0 and x <= size_x-5) and
        board[y+1][x+1] == p1 and
        board[y+2][x+2] == ' ' and
        board[y+3][x+3] == p1 and
        board[y-1][x-1] == ' ' and
        board[y+4][x+4] == ' '):
        score += 2000
    if ((y > 0 and y <= size_y-5 and x > 0 and x <= size_x-5) and
        board[y+1][x-1] == p1 and
        board[y+2][x-2] == ' ' and
        board[y+3][x-3] == p1 and
        board[y-1][x+1] == ' ' and
        board[y+4][x-4] == ' '):
        score += 2000
    return score

def three_in_a_row_a_side(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-4) and
        board[y+1][x] == p1 and
        board[y+2][x] == p1 and
        board[y+3][x] == p1 and
        (board[y-1][x] == p2 or
        board[y+4][x] == p2)):
        score += 100
    if ((x > 0 and x <= size_x-4) and
        board[y][x+1] == p1 and
        board[y][x+2] == p1 and
        board[y][x+3] == p1 and
        (board[y][x-1] == p2 or
        board[y][x+4] == p2)):
        score += 100
    if ((y > 0 and y <= size_y-4 and x > 0 and x <= size_x-4) and
        board[y+1][x+1] == p1 and
        board[y+2][x+2] == p1 and
        board[y+3][x+3] == p1 and
        (board[y-1][x-1] == p2 or
        board[y+4][x+4] == p2)):
        score += 100
    if ((y > 0 and y <= size_y-4 and x > 0 and x <= size_x-4) and
        board[y+1][x-1] == p1 and
        board[y+2][x-2] == p1 and
        board[y+3][x-3] == p1 and
        (board[y-1][x+1] == p2 or
        board[y+4][x-4] == p2)):
        score += 100
    return score

def two_in_a_row(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-3) and
        board[y+1][x] == p1 and
        board[y-1][x] == ' ' and
        board[y+2][x] == ' '):
        score += 100
    if ((x > 0 and x <= size_x-3) and
        board[y][x+1] == p1 and
        board[y][x-1] == ' ' and
        board[y][x+2] == ' '):
        score += 100
    if ((y > 0 and y <= size_y-3 and x > 0 and x <= size_x-3) and
        board[y+1][x+1] == p1 and
        board[y-1][x-1] == ' ' and
        board[y+2][x+2] == ' '):
        score += 100
    if ((y > 0 and y <= size_y-3 and x >= 2 and x <= size_x-1) and
        board[y+1][x-1] == p1 and
        board[y-1][x+1] == ' ' and
        board[y+2][x-2] == ' '):
        score += 100
    return score

def three_seperated_by_space(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-5) and
        board[y+1][x] == ' ' and
        board[y+2][x] == p1 and
        board[y+3][x] == ' ' and
        board[y+4][x] == p1):
        score += 100
    if ((x > 0 and x <= size_x-5) and
        board[y][x+1] == ' ' and
        board[y][x+2] == p1 and
        board[y][x+3] == ' ' and
        board[y][x+4] == p1):
        score += 100
    if ((y > 0 and y <= size_y-5 and x > 0 and x <= size_x-5) and
        board[y+1][x+1] == ' ' and
        board[y+2][x+2] == p1 and
        board[y+3][x+3] == ' ' and
        board[y+4][x+4] == p1):
        score += 100
    if ((y > 0 and y <= size_y-5 and x > 0 and x >= 5) and
        board[y+1][x-1] == ' ' and
        board[y+2][x-2] == p1 and
        board[y+3][x-3] == ' ' and
        board[y+4][x-4] == p1):
        score += 100
    return score

def five_in_a_row(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    if maximizer:
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    if ((y > 0 and y <= size_y-4) and
        board[y+1][x] == p1 and
        board[y+2][x] == p1 and
        board[y+3][x] == p1 and
        board[y+4][x] == p1):
        score += 1000000
    if ((x > 0 and x <= size_x-4) and
        board[y][x+1] == p1 and
        board[y][x+2] == p1 and
        board[y][x+3] == p1 and
        board[y][x+4] == p1):
        score += 1000000
    if ((y > 0 and y <= size_y-4 and x > 0 and x <= size_x-4) and
        board[y+1][x+1] == p1 and
        board[y+2][x+2] == p1 and
        board[y+3][x+3] == p1 and
        board[y+4][x+4] == p1):
        score += 1000000
    if ((y > 0 and y <= size_y-4 and x > 0 and x >= 4) and
        board[y+1][x-1] == p1 and
        board[y+2][x-2] == p1 and
        board[y+3][x-3] == p1 and
        board[y+4][x-4] == p1):
        score += 1000000
    return score

def all_four_move(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    score += five_in_a_row(x, y, maximizer, player1, player2, board, size_x, size_y)
    score += four_in_a_row_first_case(x, y, maximizer, player1, player2, board, size_x, size_y)
    score += four_in_a_row(x, y, maximizer, player1, player2, board, size_x, size_y)
    score += four_in_a_row_a_side(x, y, maximizer, player1, player2, board, size_x, size_y)
    return score

def all_three_move(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    score += three_in_a_row_first_case(x, y, maximizer, player1, player2, board, size_x, size_y)
    score += three_in_a_row_second_case(x, y, maximizer, player1, player2, board, size_x, size_y)
    score += three_in_a_row(x, y, maximizer, player1, player2, board, size_x, size_y)
    score += three_in_a_row_a_side(x, y, maximizer, player1, player2, board, size_x, size_y)
    return score

def all_two_move(x, y, maximizer, player1, player2, board, size_x, size_y):
    score = 0
    score += two_in_a_row(x, y, maximizer, player1, player2, board, size_x, size_y)
    return score