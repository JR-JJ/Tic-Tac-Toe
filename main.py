print('Welcome to our game of Tic-Tac-Toe!')
print('Here is an initial view of the board with positions to choose from.')

print('''
        _1|_2|_3
        _4|_5|_6
         7| 8| 9
      ''')

def update_board():
    board = [['','',''],['','',''],['','','']]
    return board

def print_board(board):
    for item in board:
        print(item)

print_board(update_board())