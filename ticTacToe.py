""" This program represents a tic-tac-toe game
Written by Alex Robbins alexrrobbins@gmail.com
"""

import sys

print('''Welcome to tic-tac-toe!
Rules: Three X's or O's in any direction wins the game.
An invalid move will result in a skipped turn, so be careful!
Below is a diagram of the board. Type in the spot where you want to place your letter to make your move.

''')

print('topL | topM | topR')
print('_____|______|______')
print('midL | midM | midR')
print('_____|______|______')
print('lowL | lowM | lowR')
print('     |      |      ')

# Initializes empty board
theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ',
            'midL': ' ', 'midM': ' ', 'midR': ' ',
            'lowL': ' ', 'lowM': ' ', 'lowR': ' '}


# Prints out the board
def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])


# Sets conditions for winning
def setConditions(theBoard):
    conditionX1 = theBoard['topL'] == theBoard['topM'] == theBoard['topR'] == 'X'
    conditionX2 = theBoard['midL'] == theBoard['midM'] == theBoard['midR'] == 'X'
    conditionX3 = theBoard['lowL'] == theBoard['lowM'] == theBoard['lowR'] == 'X'
    conditionX4 = theBoard['topL'] == theBoard['midM'] == theBoard['lowR'] == 'X'
    conditionX5 = theBoard['topR'] == theBoard['midM'] == theBoard['lowL'] == 'X'
    conditionX6 = theBoard['topL'] == theBoard['midL'] == theBoard['lowL'] == 'X'
    conditionX7 = theBoard['topM'] == theBoard['midM'] == theBoard['lowM'] == 'X'
    conditionX8 = theBoard['topR'] == theBoard['midR'] == theBoard['lowR'] == 'X'

    conditionO1 = theBoard['topL'] == theBoard['topM'] == theBoard['topR'] == 'O'
    conditionO2 = theBoard['midL'] == theBoard['midM'] == theBoard['midR'] == 'O'
    conditionO3 = theBoard['lowL'] == theBoard['lowM'] == theBoard['lowR'] == 'O'
    conditionO4 = theBoard['topL'] == theBoard['midM'] == theBoard['lowR'] == 'O'
    conditionO5 = theBoard['topR'] == theBoard['midM'] == theBoard['lowL'] == 'O'
    conditionO6 = theBoard['topL'] == theBoard['midL'] == theBoard['lowL'] == 'O'
    conditionO7 = theBoard['topM'] == theBoard['midM'] == theBoard['lowM'] == 'O'
    conditionO8 = theBoard['topR'] == theBoard['midR'] == theBoard['lowR'] == 'O'
    return [conditionX1, conditionX2, conditionX3, conditionX4, conditionX5, conditionX6, conditionX7, conditionX8,
            conditionO1, conditionO2, conditionO3, conditionO4, conditionO5, conditionO6, conditionO7, conditionO8]


# Plays the game
for num in range(0, 999):
    # Switches turns
    if num % 2 == 0:
        turn = 'O'
    else:
        turn = 'X'
    print('It is now ' + turn + "'s turn. Move on which space?")

    # Sets the move
    move = str( input() )

    # Checks if move is valid and if it is performs move
    if theBoard[move] == ('X' or 'O'):
        print('Invalid move')
    else:
        theBoard[move] = turn

    # Prints the board after every move
    printBoard(theBoard)

    """Resets conditions after every move to check if any are met
     Passes the state of the "board" to the function which sets the conditions as boolean values
     The function returns the booleans in a list so they can be used in the next if-elif statements"""
    c = setConditions(theBoard)

    # Checks each returned boolean from the list above to see if any conditions are met.
    # If a condition is met, the program will print out the winner and exit.
    if c[0] or c[1] or c[2] or c[3] or c[4] or c[5] or c[6] or c[7]:
        print('X is the winner!')
        sys.exit()
    elif c[8] or c[9] or c[10] or c[11] or c[12] or c[13] or c[14] or c[15]:
        print('O is the winner!')
        sys.exit()
    # If the board is filled and there are no winners, the game will be tied and the program will exit.
    elif ' ' not in theBoard.values():
        print('The game is tied.')
        sys.exit()
