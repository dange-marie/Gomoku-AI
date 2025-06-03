import copy

from .move_function import all_four_move, all_three_move, all_two_move

class gomoku:
    def __init__(self, x, y, player1, player2):
        self.board = [[' ' for i in range(x)] for j in range(y)]
        print(len(self.board[0]))
        self.x = x-1
        self.y = y-1
        self.start = False
        self.player1 = player1
        self.player2 = player2
        self.history = []
        self.win = "nobody"

    def score(self, maximizer):
        score = 0
        if maximizer:
            p1 = self.player1
            p2 = self.player2
        else:
            p1 = self.player2
            p2 = self.player1
        for i in range(self.y + 1):
            for j in range(self.x + 1):
                if self.board[i][j] == p1:
                    score += all_four_move(j, i, maximizer, self.player1, self.player2, self.board, self.x, self.y)
                    score += all_three_move(j, i, maximizer, self.player1, self.player2, self.board, self.x, self.y)
                    score += all_two_move(j, i, maximizer, self.player1, self.player2, self.board, self.x, self.y)
        return score

    def print_board(self):
        print("_"*self.x*2)
        for i in range(self.y):
            for j in range(self.x):
                if j == 0:
                    print("|" + self.board[i][j], end="|")
                elif j == self.x-1:
                    print(self.board[i][j] + "|")
                else:
                    print(self.board[i][j], end="|")
            print("_"*self.x*2)

    def win_pattern(self, x, y, verbose=False):
        vlue = self.board[y][x]
        if ((y <= self.y-5) and
            self.board[y+1][x] == vlue and
            self.board[y+2][x] == vlue and
            self.board[y+3][x] == vlue and
            self.board[y+4][x] == vlue):
            if verbose:
                print(f"Vertical vlue [{vlue}]")
            return True
        if ((x <= self.x-5) and
            self.board[y][x+1] == vlue and
            self.board[y][x+2] == vlue and
            self.board[y][x+3] == vlue and
            self.board[y][x+4] == vlue):
            if verbose:
                print(f"Horizontal vlue [{vlue}]")
            return True
        if ((y <= self.y-5 and x <= self.x-5) and
            self.board[y+1][x+1] == vlue and
            self.board[y+2][x+2] == vlue and
            self.board[y+3][x+3] == vlue and
            self.board[y+4][x+4] == vlue):
            if verbose:
                print(f"Diagonal vlue [{vlue}]")
            return True
        if ((y <= self.y-5 and x >= 5) and
            self.board[y+1][x-1] == vlue and
            self.board[y+2][x-2] == vlue and
            self.board[y+3][x-3] == vlue and
            self.board[y+4][x-4] == vlue):
            if verbose:
                print(f"Diagonal vlue [{vlue}]")
            return True
        return False

    def no_win(self, verbose=False):
        for i in range(self.y + 1):
            for j in range(self.x + 1):
                if self.board[i][j] != ' ' and self.win_pattern(j, i, verbose):
                    if verbose:
                        print("Player ", str(j), " ", str(i), " wins")
                    if self.board[i][j] == self.player1:
                        self.win = "Player1"
                    else:
                        self.win = "Player2"
                    return False
        return True

    def set_move(self, x, y, player):
        if x > self.x or y > self.y:
            return False
        if self.board[y][x] == ' ':
            self.board[y][x] = player
            if self.start == False:
                self.start = True
            return True
        return False

    def undo_move(self, x, y):
        if x > self.x or y > self.y:
            return
        if self.board[y][x] != ' ':
            self.board[y][x] = ' '

    def get_adjacent(self, board, x, y, pl, moves):
        if x > 0 and self.board[y][x - 1] == ' ':
            board[y][x - 1] = pl
            moves.append((x - 1, y))
        if x <= self.x - 1 and self.board[y][x + 1] == ' ':
            board[y][x + 1] = pl
            moves.append((x + 1, y))
        if y > 0 and self.board[y - 1][x] == ' ':
            board[y - 1][x] = pl
            moves.append((x, y - 1))
        if y <= self.y - 1 and self.board[y + 1][x] == ' ':
            board[y + 1][x] = pl
            moves.append((x, y + 1))
        if x > 0 and y > 0 and self.board[y - 1][x - 1] == ' ':
            board[y - 1][x - 1] = pl
            moves.append((x - 1, y - 1))
        if x <= self.x - 1 and y <= self.y - 1 and self.board[y + 1][x + 1] == ' ':
            board[y + 1][x + 1] = pl
            moves.append((x + 1, y + 1))
        if x > 0 and y <= self.y - 1 and self.board[y + 1][x - 1] == ' ':
            board[y + 1][x - 1] = pl
            moves.append((x - 1, y + 1))
        if x <= self.x - 1 and y > 0 and self.board[y - 1][x + 1] == ' ':
            board[y - 1][x + 1] = pl
            moves.append((x + 1, y - 1))

    def get_moves(self, maximizer):
        moves = []
        if maximizer:
            pl = self.player1
        else:
            pl = self.player2
        board = copy.deepcopy(self.board)
        for i in range(self.y + 1):
            for j in range(self.x + 1):
                if self.board[i][j] != ' ':
                    self.get_adjacent(board, j, i, pl, moves)
        return moves
