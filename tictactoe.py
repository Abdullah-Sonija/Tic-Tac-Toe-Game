"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for col in row:
            if col == X:    x_count +=1
            if col == O:    o_count +=1
    
    if x_count > o_count:   return O
    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action.add((i,j))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [row[:] for row in board]

    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception ("Invalid move")

    turn = player(board)

    new_board[action[0]][action[1]] = turn

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #horizontal
    for i in range(len(board)):
        x_flag = True
        o_flag = True
        for j in range(len(board[i])):
            if board[i][j] != X:    x_flag = False
            if board[i][j] != O:    o_flag = False
        if x_flag:  return X
        if o_flag:  return O

    #vertical
    for i in range(len(board[0])):
        x_flag = True
        o_flag = True
        for j in range(len(board)):
            if board[j][i] != X:    x_flag = False
            if board[j][i] != O:    o_flag = False
        if x_flag:  return X
        if o_flag:  return O

    #diagonals
    x_flag = True
    o_flag = True
    for i in range(len(board)):
        if board[i][i] != X:    x_flag = False
        if board[i][i] != O:    o_flag = False
    if x_flag:  return X
    if o_flag:  return O

    x_flag = True
    o_flag = True
    for i in range(len(board)):
        if board[i][len(board)-1-i] != X:   x_flag = False
        if board[i][len(board)-1-i] != O:   o_flag = False
    if x_flag:  return X
    if o_flag:  return O    
    
    return None
        
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (utility(board)) != 0:  return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:    return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:  return 1
    elif w == O:  return -1
    else:   return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if (terminal(board)):   return None

    if player(board) == X:
        best_score = -(math.inf)
        best_move = None
        for action in actions(board):
            score = min_value(result(board,action))
            if score > best_score:
                best_score = score
                best_move = action
        return best_move    
    
    elif player(board) == O:
        best_score = math.inf
        best_move = None
        for action in actions(board):
            score = max_value(result(board,action))
            if score < best_score:
                best_score = score
                best_move = action
        return best_move    

def min_value(board):

    if terminal(board):     return utility(board)

    value = math.inf
    for action in actions(board):
        value = min(value,max_value(result(board,action)))
        if value == -1:      return -1
    return value

def max_value(board):

    if terminal(board):     return utility(board)

    value = -math.inf
    for action in actions(board):
        value = max(value,min_value(result(board,action)))
        if value == 1:      return 1
    return value
