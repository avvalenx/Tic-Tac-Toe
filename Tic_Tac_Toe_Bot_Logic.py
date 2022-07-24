def computer_move_2(player_move):
    #all corner moves are even numbers
    if player_move == 0:
        return 8
    elif player_move == 2:
        return 6
    elif player_move == 6:
        return 2
    elif player_move == 8:
        return 0
    #all edge moves
    elif player_move == 1:
        return 7
    elif player_move == 5:
        return 3
    elif player_move == 7:
        return 1
    elif player_move == 3:
        return 5

def find_int_index(list):
    for item in list:
        if type(item) == int:
            return list.index(item)

def computer_defense(board):
    #check rows
    for row in range(3):
        if board[row].count('X') == 2:
            try:
                return find_int_index(board[row]) + 3*row
            except Exception:
                pass
    #check columns
    for column_list_num in range(3):                
        #convert columns into list
        column_list = [board[0][column_list_num], board[1][column_list_num], board[2][column_list_num]]
        if column_list.count('X') == 2:
            try:
                return find_int_index(column_list) * 3 + column_list_num
            except Exception:
                pass
            
    #check diagonals
    #convert diagonals into 2 lists
    diagonal_list_1 = [board[0][0], board[1][1], board[2][2]]
    if diagonal_list_1.count('X') == 2:
        try:
            return find_int_index(diagonal_list_1)*4
        except Exception:
            pass
    diagonal_list_2 = [board[2][0], board[1][1], board[0][2]]
    if diagonal_list_2.count('X') == 2:
        try:
            return 6 - find_int_index(diagonal_list_1)*2
        except Exception:
            pass
    
def computer_win(board):
    #check rows
    for row in range(3):
        if board[row].count('O') == 2:
            try:
                return find_int_index(board[row]) + 3*row
            except Exception:
                pass
    #check columns
    for column_list_num in range(3):                
        #convert columns into list
        column_list = [board[0][column_list_num], board[1][column_list_num], board[2][column_list_num]]
        if column_list.count('O') == 2:
            try:
                return find_int_index(column_list) * 3 + column_list_num
            except Exception:
                pass
            
    #check diagonals
    #convert diagonals into 2 lists
    diagonal_list_1 = [board[0][0], board[1][1], board[2][2]]
    if diagonal_list_1.count('O') == 2:
        try:
            return find_int_index(diagonal_list_1)*4
        except Exception:
            pass
    diagonal_list_2 = [board[2][0], board[1][1], board[0][2]]
    if diagonal_list_2.count('O') == 2:
        try:
            return 6 - find_int_index(diagonal_list_2)*2
        except Exception:
            pass

def computer_move_3(last_move, board):
    if last_move == 0:
        #possible moves 1 or 3
        if board[0][1] == 'X':
            return 3
        else:
            return 1
    if last_move == 1:
        #possible moves 0 or 2
        if board[0][0] == 'X' or board[0][2] == 'X':
            return None
        else:
            return 0 #does not matter if play 0 or 2 computer wins

    if last_move == 2:
        #possible moves 1 or 5
        if board[0][1] == 'X':
            return 5
        else:
            return 1
    if last_move == 3:
        #possible moves 0 and 6
        if board[0][0] == 'X' or board[2][0] == 'X':
            return None
        else:
            return 0 #does not matter if play 0 or 6 computer wins

    if last_move == 5:
        #possible moves 2 and 8
        if board[0][2] == 'X' or board[2][2] == 'X':
            return None
        else:
            return 2 #does not matter if play 2 or 8 computer wins

    if last_move == 6:
        #possible oves 3 or 7
        if board[1][0] == 'X':
            return 7
        else:
            return 3
    if last_move == 7:
        #possible moves 6 or 8
        if board[2][0] == 'X' or board[2][2] == 'X':
            return None
        else:
            return 6 #does not matter if play 6 or 8 computer wins

    if last_move == 8:
        #possible moves 5 or 7
        if board[1][2] == 'X':
            return 7
        else:
            return 5