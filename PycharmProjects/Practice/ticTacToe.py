#This program represents a tic-tac-toe game

import sys

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

def setConditions(theBoard):
    conditionX1 = theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == 'X'
    conditionX2 = theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] == 'X'
    conditionX3 = theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] == 'X'
    conditionX4 = theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] == 'X'
    conditionX5 = theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] == 'X'
    conditionX6 = theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] == 'X'
    conditionX7 = theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] == 'X'
    conditionX8 = theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] == 'X'

    conditionO1 = theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == 'O'
    conditionO2 = theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] == 'O'
    conditionO3 = theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] == 'O'
    conditionO4 = theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] == 'O'
    conditionO5 = theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] == 'O'
    conditionO6 = theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] == 'O'
    conditionO7 = theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] == 'O'
    conditionO8 = theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] == 'O'
    return [conditionX1, conditionX2, conditionX3, conditionX4, conditionX5, conditionX6, conditionX7, conditionX8,
            conditionO1, conditionO2, conditionO3, conditionO4, conditionO5, conditionO6, conditionO7, conditionO8]

for num in range(int(sys.maxsize)):
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

    c = []
    c = setConditions(theBoard)

    if c[0] or c[1] or c[2] or c[3] or c[4] or c[5] or c[6] or c[7]:
        print('X is the winner!')
        break
    elif c[8] or c[9] or c[10] or c[11] or c[12] or c[13] or c[14] or c[15]:
        print('O is the winner!')
        break
    elif ' ' not in theBoard.values():
        print('The game is tied.')
        break
