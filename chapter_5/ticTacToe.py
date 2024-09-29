

theBoard = {'tl': ' ', 'tm': ' ', 'tr': ' ',
            'ml': ' ', 'mm': ' ', 'mr': ' ',
            'll': ' ', 'lm': ' ', 'lr': ' '}



def printBoard(board):
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['ll'] + '|' + board['lm'] + '|' + board['lr'])
     

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    choice = input('Turn for ' + turn + '. Choose a field: ')
    theBoard[choice] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)


