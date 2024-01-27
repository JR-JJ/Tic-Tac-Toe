print('Welcome to our game of Tic-Tac-Toe!')
print('Here is an initial view of the board with positions to choose from.')
print('Player One will be X, and Player Two will be O.')

print('''
        _1|_2|_3
        _4|_5|_6
         7| 8| 9
      ''')

board = [['','',''],['','',''],['','','']]

def update_board(board,x,y,c):
    if not board[x][y]:
        board[x][y] = c
    else:
        print('Spot is taken')
        player_turn()
    winner(board)
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
    else:
        return False
    
    

def player_one():
    choice = input('P1 - Position choice: ')

    if choice == '1':
        update_board(board, 0, 0, 'X')
    elif choice == '2':
        update_board(board, 0, 1, 'X')
    elif choice == '3':
        update_board(board, 0, 2, 'X')
    elif choice == '4':
        update_board(board, 1, 0, 'X')
    elif choice == '5':
        update_board(board, 1, 1, 'X')
    elif choice == '6':
        update_board(board, 1, 2, 'X')
    elif choice == '7':
        update_board(board, 2, 0, 'X')
    elif choice == '8':
        update_board(board, 2, 1, 'X')
    elif choice == '9':
        update_board(board, 2, 2, 'X')
    else:
        print('Please try again')
        player_one()

def player_two():
    choice = input('P2 - Position choice: ')
    if choice == '1':
        update_board(board, 0, 0, 'O')
    elif choice == '2':
        update_board(board, 0, 1, 'O')
    elif choice == '3':
        update_board(board, 0, 2, 'O')
    elif choice == '4':
        update_board(board, 1, 0, 'O')
    elif choice == '5':
        update_board(board, 1, 1, 'O')
    elif choice == '6':
        update_board(board, 1, 2, 'O')
    elif choice == '7':
        update_board(board, 2, 0, 'O')
    elif choice == '8':
        update_board(board, 2, 1, 'O')
    elif choice == '9':
        update_board(board, 2, 2, 'O')
    else:
        print('Please try again')
        player_two()

def player_turn():
    turn = 1
    win = False
    while win == winner(board):
        if turn%2 == 0:
            player_two()
            turn += 1
        else:
            player_one()
            turn += 1

player_turn()