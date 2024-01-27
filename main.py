print('Welcome to our game of Tic-Tac-Toe!')
print('Here is an initial view of the board with positions to choose from.')

print('''
        _1|_2|_3
        _4|_5|_6
         7| 8| 9
      ''')

board = [['','',''],['','',''],['','','']]

def update_board(board):
    
    print_board(board)

def print_board(board):
    for item in board:
        print(item)

def winner(board):
    if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        print('Player Two Wins!')
        return True
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        print('Player Two Wins!')
        return True
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        print('Player Two Wins!')
        return True
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        print('Player Two Wins!')
        return True
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        print('Player Two Wins!')
        return True
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        print('Player Two Wins!')
        return True
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        print('Player Two Wins!')
        return True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        print('Player Two Wins!')
        return True
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        print('Player One Wins!')
        return True
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        print('Player One Wins!')
        return True
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        print('Player One Wins!')
        return True
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        print('Player One Wins!')
        return True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        print('Player One Wins!')
        return True
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print('Player Two Wins!')
        return True
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print('Player Two Wins!')
        return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        print('Player Two Wins!')
        return True
    
    

def player_one():
    print('One')
def player_two():
    print('Two')

def player_turn():
    turn = 1
    if turn%2 == 0:
        player_two()
    else:
        player_one()