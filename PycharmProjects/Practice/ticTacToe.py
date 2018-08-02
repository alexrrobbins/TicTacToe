#This program represents a tic-tac-toe game

#Initializes empty board
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

#Prints out the board
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


for num in range(1,9):
    if num%2 == 0:
        turn = 'O'
    else:
        turn = 'X'
    print('It is now ' + turn + "'s turn. Move on which space?")
    move = input()
    if theBoard[move] == ('X' or 'O'):
        print('Invalid move')
        continue
    else:
        theBoard[move] = turn
    printBoard(theBoard)