# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:18:53 2019

@author: John
"""

import numpy as np

ROW_COUNT = 12
COLUMN_COUNT = 8

def position(row, col):
    

def create_board():
    board = np.zeros((12,8))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece
    
def is_valid_location(board, col):
    return board[11][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
        
def print_board(board):
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = int(input("P1 make your column selection (0-7):"))
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
        
    

    #Ask Player 2 input
    else:
        col = int(input("P2 make your column selection (0-7):"))
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            
    print_board(board)
        
    turn += 1
    turn = turn % 2        
    
    

