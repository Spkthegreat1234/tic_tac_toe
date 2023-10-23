#tic tac toe with tkinter UI

from tkinter import *
from tkinter import messagebox
import random

#global variables

#board
board = [' ' for x in range(10)]

#player
player = 'X'

#computer
computer = 'O'

#winning combinations
winning_combinations = ((1,2,3), (4,5,6), (7,8,9), (1,4,7),
                        (2,5,8), (3,6,9), (1,5,9), (3,5,7))

#functions

#draw board

def draw_board():
    print(f"   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print(f"   |   |   ")
    print(f"-----------")
    print(f"   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print(f"   |   |   ")
    print(f"-----------")
    print(f"   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print(f"   |   |   ")   

#check if board is full

def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
    
#check if player has won

def is_winner(board, player):

    print("Welcome to Tic Tac Toe!")
    print("You are player X and the computer is player O.")
    print("You will go first.")
    print("To play, enter the number of the square you want to play in.")
    print("The squares are numbered like this:")
    print("   |   |   ")
    print(" 1 | 2 | 3 ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" 4 | 5 | 6 ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" 7 | 8 | 9 ")
    print("   |   |   ")

    if (board[1] == player and board[2] == player and board[3] == player) or \
        (board[4] == player and board[5] == player and board[6] == player) or \
        (board[7] == player and board[8] == player and board[9] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[3] == player and board[6] == player and board[9] == player) or \
        (board[1] == player and board[5] == player and board[9] == player) or \
        (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False
    
#check if computer has won

def is_computer_winner(board, computer):
    if (board[1] == computer and board[2] == computer and board[3] == computer) or \
        (board[4] == computer and board[5] == computer and board[6] == computer) or \
        (board[7] == computer and board[8] == computer and board[9] == computer) or \
        (board[1] == computer and board[4] == computer and board[7] == computer) or \
        (board[2] == computer and board[5] == computer and board[8] == computer) or \
        (board[3] == computer and board[6] == computer and board[9] == computer) or \
        (board[1] == computer and board[5] == computer and board[9] == computer) or \
        (board[3] == computer and board[5] == computer and board[7] == computer):
        return True
    else:
        return False

#check if space is free

def is_space_free(board, position):
    if board[position] == ' ':
        return True
    else:
        return False
    
#insert letter

def insert_letter(board, letter, position):
    board[position] = letter

#player move

def player_move(board):
    run = True
    while run:
        move = input("Please select a position to place an X (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if is_space_free(board, move):
                    run = False
                    insert_letter(board, player, move)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print("Please type a number within the range!")
        except:
            print("Please type a number!")
    
#computer move

def computer_move(board):
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    for let in [computer, player]:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_computer_winner(board_copy, let):
                move = i
                return move
            
    corners_open = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners_open.append(i)
            
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move
    
    if 5 in possible_moves:
        move = 5
        return move
    
    edges_open = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            edges_open.append(i)
            
    if len(edges_open) > 0:
        move = select_random(edges_open)
        
    return move

#select random

def select_random(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

#main

def main():

    #draw board
    draw_board()

    #check if board is full
    while not(is_board_full(board)):
        if not(is_winner(board, computer)):
            player_move(board)
            draw_board()
        else:
            print("Sorry, O's won this time!")
            break
        
        if not(is_computer_winner(board, player)):
            move = computer_move(board)
            if move == 0:
                print("Tie Game!")
            else:
                insert_letter(board, computer, move)
                print(f"Computer placed an O in position {move}:")
                draw_board()
        else:
            print("X's won this time! Good Job!")
            break

    if is_board_full(board):
        print("Tie Game!")

if __name__ == "__main__":
    main()

#end of the program
