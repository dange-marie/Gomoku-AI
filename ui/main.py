#!/usr/bin/env python3
import pygame as py
import sys, time, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.data_structure import gomoku
from ai.ai_algorithm import *

py.init()
font = py.font.Font(None, 36)
player1_text = font.render("AI (white)", True, (255, 255, 255))
player2_text = font.render("Human (black)", True, (255, 255, 255))

def display_board(screen, board, turn):
    for i in range(20):
        for j in range(20):
            py.draw.rect(screen, (238, 209, 177), py.Rect(j * 50, i * 50, 50, 50))
            py.draw.rect(screen, (0, 0, 0), py.Rect(j * 50, i * 50, 50, 50), 1)
            if board.board[i][j] == 'X':
                py.draw.circle(screen, (255, 255, 255), (j * 50 + 25, i * 50 + 25), 20)
            if board.board[i][j] == 'O':
                py.draw.circle(screen, (0, 0, 0), (j * 50 + 25, i * 50 + 25), 20)
    py.draw.rect(screen, (177, 126, 105), py.Rect(1000, 0, 300, 1000))
    py.draw.rect(screen, (0, 0, 0), py.Rect(1000, 0, 300, 1000), 2)
    turn_text = font.render("Turn: " + str(turn), True, (255, 255, 255))
    screen.blit(player1_text, (1050, 300))
    screen.blit(player2_text, (1050, 350))
    screen.blit(turn_text, (1050, 100))

def display_win(screen, board):
    winner = board.win
    if winner == 'Player1':
        winner = 'AI'
    else:
        winner = 'Human'
    display_board(screen, board, 0)
    py.draw.rect(screen, (177, 126, 105), py.Rect(1000, 0, 300, 1000))
    py.draw.rect(screen, (0, 0, 0), py.Rect(1000, 0, 300, 1000), 2)
    win_text = font.render(winner + " win", True, (255, 255, 255))
    screen.blit(win_text, (1050, 100))

def init_board():
    f = open(sys.argv[1], "r")
    tab = f.read().split("\n")
    board = gomoku(20, 20, 'X', 'O')
    turn = True
    for i in tab:
        tmp = i.split(",")
        if turn == True:
            board.set_move(int(tmp[0]), int(tmp[1]), board.player2)
            turn = False
        else:
            board.set_move(int(tmp[0]), int(tmp[1]), board.player1)
            turn = True
    return board

def main():
    screen = py.display.set_mode((1300, 1000))
    py.display.set_caption("Gomoku")
    board = gomoku(20, 20, 'X', 'O')
    turn = 0
    play = False

    try:
        if sys.argv[1] == "AI":
            move = best_move(board, 3)
            board.set_move(move[0], move[1], board.player1)
            turn += 1
    except:
        pass
    while 1:
        display_board(screen, board, turn)
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_r:
                    board = gomoku(20, 20, 'X', 'O')
                    turn = 0
                    play = False
            if event.type == py.MOUSEBUTTONDOWN and board.no_win() == True:
                x, y = event.pos
                x = x // 50
                y = y // 50
                res = board.set_move(x, y, board.player2)
                if res == False:
                    continue
                play = True
        if board.no_win() == True and play:
            display_board(screen, board, turn)
            move = best_move(board, 3)
            board.set_move(move[0], move[1], board.player1)
            play = False
            turn += 1
        if board.no_win() == False:
            display_win(screen, board)
        if board.no_win() == True:
            display_board(screen, board, turn)
        if board.no_win() == False:
            display_win(screen, board)
        py.display.update()

    py.quit()

if __name__ == "__main__":
    main()