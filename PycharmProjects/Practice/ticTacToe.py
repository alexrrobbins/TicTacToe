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

#Sets the conditions for X winning
conditionX1 = theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == 'X'
conditionX2 = theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] == 'X'
conditionX3 = theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] == 'X'
conditionX4 = theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] == 'X'
conditionX5 = theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] == 'X'
conditionX6 = theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] == 'X'
conditionX7 = theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] == 'X'
conditionX8 = theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] == 'X'

#Sets the conditions for O winning
conditionO1 = theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == 'O'
conditionO2 = theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] == 'O'
conditionO3 = theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] == 'O'
conditionO4 = theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] == 'O'
conditionO5 = theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] == 'O'
conditionO6 = theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] == 'O'
conditionO7 = theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] == 'O'
conditionO8 = theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] == 'O'

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
    if ' ' not in theBoard.values():
        break