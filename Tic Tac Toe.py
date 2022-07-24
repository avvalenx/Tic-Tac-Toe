# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 22:24:55 2021

@author: AV
"""
import sys
import random
import Tic_Tac_Toe_Bot_Logic

board = [[0,1,2],
         [3,4,5],
         [6,7,8],
         ]

def print_board():
    for i in range(3):
        print(board[i])
    print()

def check_win():
#check rows
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2]:
            return True
#check columns
    for column in range(3):
        if board[0][column] == board[1][column] and board[0][column] == board[2][column]:
            return True
#check diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            return True
    if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
            return True
    return False

def place_x_or_o(place, x_or_o):
    #FIXME in 2 player mode going somewhere already played results in turn being skipped
    #FIXME in single player mode going somewhere already played breaks everything
    try:
        #first row placement
        if place <= 2:
            #make sure space is not taken
            if board[0][place] == 'X' or board[0][place] == 'O':
                print('Choose a different space that one is taken')
            #place move add to counter change turn and display board
            else:
                board[0][place] = x_or_o
                print_board()
        #second row placement
        elif place <= 5:
            #make sure space is not taken
            if board[1][place-3] == 'X' or board[1][place-3] == 'O':
                print('Choose a different space that one is taken')
            #place move add to counter change turn and display board
            else:
                board[1][place-3] = x_or_o
                print_board()
        #third row placement
        else:
            #make sure space is not taken
            if board[2][place-6] == 'X' or board[2][place-6] == 'O':
                print('Choose a different space that one is taken')
            #place move add to counter change turn and display board
            else:
                board[2][place-6] = x_or_o
                print_board()
    #except statement if invalid entry
    except Exception:
        print('Invalid entry\nYou must enter a number between 0 and 8')

def two_player_mode():
    #initialize counter at 0 and set win to false
    counter = 0
    win = False
    #show the board before a move is made
    print_board()
    while win == False:
        #determine whos turn it is to go
        if counter % 2 == 0:
            x_or_o = 'X'
        else:
            x_or_o = 'O'
        #normal operation should work if user enters number from 0 - 8
        place = int(input('choose where to place your move:\n'))
        place_x_or_o(place, x_or_o)
        counter += 1
        #check for win after every iteration of loop
        win = check_win()
        #ends program if board is full and no winner and declares a tie
        if win == False and counter == 9:
            print('Its a tie')
            sys.exit()

    print('we have a winner!')

def single_player_mode():
    #set up the available moves for the computer initialize counter to 0 and set win to false
    available_moves = [0,1,2,3,4,5,6,7,8]
    win = False
    #computer turn 1
    #go in the middle to guarantee win or tie
    place_x_or_o(4, 'O')
    available_moves.remove(4)

    #user turn 1
    player_place = int(input('choose where to place your move:\n'))
    place_x_or_o(player_place, 'X')
    available_moves.remove(player_place)

    #computer turn 2 where player move is mirrored
    place = Tic_Tac_Toe_Bot_Logic.computer_move_2(player_place)
    place_x_or_o(place, 'O')
    available_moves.remove(place)
    cpu_last_turn = place

    #user turn 2
    place = int(input('choose where to place your move:\n'))
    place_x_or_o(place, 'X')
    available_moves.remove(place)
    
    #computer turn 3
    #first play defense
    place = Tic_Tac_Toe_Bot_Logic.computer_defense(board)
    #the computer plays defense if needed or sets up guaranteed win
    if place != None: #have to play defense and guarantee tie
        place_x_or_o(place, 'O')
        print('computer plays defense and goes in space', place)
        available_moves.remove(place)

        #user turn 3
        place = int(input('choose where to place your move:\n'))
        place_x_or_o(place, 'X')
        available_moves.remove(place)

        #computer turn 4
        place = Tic_Tac_Toe_Bot_Logic.computer_win(board)
        #play defense if computer can not win
        if place == None:
            place = Tic_Tac_Toe_Bot_Logic.computer_defense(board)
            #play randomly if computer can not play defense
            if place == None:
                place = available_moves[random.randint(0, len(available_moves)-1)]
        place_x_or_o(place, 'O')
        available_moves.remove(place)

        #check for win
        if check_win() == True:
            print('we have a winner')
            sys.exit()
        
        #user turn 4
        place = int(input('choose where to place your move:\n'))
        place_x_or_o(place, 'X')
        available_moves.remove(place)

        #computer turn 5
        place = available_moves[0]
        place_x_or_o(place, 'O')
        
        #check for win
        if check_win() == True:
            print('we have a winner')
            sys.exit()
        else:
            print('Its a tie')
            sys.exit()

    else: #able to set up situation where computer gives 2 options to win
        place = Tic_Tac_Toe_Bot_Logic.computer_move_3(cpu_last_turn, board)

        #must play out game tieing or  winning
        if place == None:
            #play randomly can't guarantee win
            place = available_moves[random.randint(0, len(available_moves)-1)]
            place_x_or_o(place, 'O')
            available_moves.remove(place)

            #user turn 3
            place = int(input('choose where to place your move:\n'))
            place_x_or_o(place, 'X')
            available_moves.remove(place)

            #computer turn 4
            place = available_moves[0]
            place_x_or_o(place, 'O')
            available_moves.remove(place)
            
            #check for win
            if check_win() == True:
                print('we have a winner')
                sys.exit()
            
            #user turn 4
            place = int(input('choose where to place your move:\n'))
            place_x_or_o(place, 'X')
            available_moves.remove(place)

            #computer turn 5
            place = available_moves[0]
            place_x_or_o(place, 'O')
            
            #check for win
            if check_win() == True:
                print('we have a winner')
                sys.exit()
            else:
                print('Its a tie')
                sys.exit()

        place_x_or_o(place, 'O')
        available_moves.remove(place)

        #user turn 3
        place = int(input('choose where to place your move:\n'))
        place_x_or_o(place, 'X')
        available_moves.remove(place)

        #computer turn 3
        place = Tic_Tac_Toe_Bot_Logic.computer_win(board)
        place_x_or_o(place, 'O')
        print('Computer Wins!')
        sys.exit()

if __name__ == '__main__':
    mode = int(input('Type 1 for single player mode or 2 for two player mode:\n'))
    if mode == 1:
        single_player_mode()
    elif mode == 2:
        two_player_mode()
    else:
        print('invalid selection goodbye')

#Archived Computer Random Move Code
"""
#randomly select a place to go
place = available_moves[random.randint(0, len(available_moves)-1)]
place_x_or_o(place, 'O')
available_moves.remove(place)
counter += 1
"""