'''
This program represents a tic-tac-toe game
Written by Alex Robbins alexrrobbins@gmail.com
'''
import sys

print('''Welcome to tic-tac-toe!
Rules: Three X's or O's in any direction wins the game.
An invalid move will result in a skipped turn, so be careful!
Below is a diagram of the board.
Type in the spot where you want to place your letter to make your move.
''')

print('topL | topM | topR')
print('_____|______|______')
print('midL | midM | midR')
print('_____|______|______')
print('lowL | lowM | lowR')
print('     |      |      ')

# Initializes empty board
the_board = {'topL': ' ', 'topM': ' ', 'topR': ' ',
            'midL': ' ', 'midM': ' ', 'midR': ' ',
            'lowL': ' ', 'lowM': ' ', 'lowR': ' '}

def print_board(the_board):
    '''
    This function prints out the board
    '''
    print(the_board['topL'] + '|' + the_board['topM'] + '|' + the_board['topR'])
    print('-+-+-')
    print(the_board['midL'] + '|' + the_board['midM'] + '|' + the_board['midR'])
    print('-+-+-')
    print(the_board['lowL'] + '|' + the_board['lowM'] + '|' + the_board['lowR'])


# Sets conditions for winning
def set_conditions(the_board):
    '''
    This function sets the conditions for winning
    '''
    conditionX1 = the_board['topL'] == the_board['topM'] == the_board['topR'] == 'X'
    conditionX2 = the_board['midL'] == the_board['midM'] == the_board['midR'] == 'X'
    conditionX3 = the_board['lowL'] == the_board['lowM'] == the_board['lowR'] == 'X'
    conditionX4 = the_board['topL'] == the_board['midM'] == the_board['lowR'] == 'X'
    conditionX5 = the_board['topR'] == the_board['midM'] == the_board['lowL'] == 'X'
    conditionX6 = the_board['topL'] == the_board['midL'] == the_board['lowL'] == 'X'
    conditionX7 = the_board['topM'] == the_board['midM'] == the_board['lowM'] == 'X'
    conditionX8 = the_board['topR'] == the_board['midR'] == the_board['lowR'] == 'X'

    conditionO1 = the_board['topL'] == the_board['topM'] == the_board['topR'] == 'O'
    conditionO2 = the_board['midL'] == the_board['midM'] == the_board['midR'] == 'O'
    conditionO3 = the_board['lowL'] == the_board['lowM'] == the_board['lowR'] == 'O'
    conditionO4 = the_board['topL'] == the_board['midM'] == the_board['lowR'] == 'O'
    conditionO5 = the_board['topR'] == the_board['midM'] == the_board['lowL'] == 'O'
    conditionO6 = the_board['topL'] == the_board['midL'] == the_board['lowL'] == 'O'
    conditionO7 = the_board['topM'] == the_board['midM'] == the_board['lowM'] == 'O'
    conditionO8 = the_board['topR'] == the_board['midR'] == the_board['lowR'] == 'O'
    return [conditionX1, conditionX2, conditionX3, conditionX4,
            conditionX5, conditionX6, conditionX7, conditionX8,
            conditionO1, conditionO2, conditionO3, conditionO4,
            conditionO5, conditionO6, conditionO7, conditionO8]


# Plays the game
for num in range(0, 999):
    # Switches turns
    if num % 2 == 0:
        turn = 'O'
    else:
        turn = 'X'
    print('It is now ' + turn + "'s turn. Move on which space?")
    # Sets the move
    move = str(input())
    # Checks if move is valid and if it is performs move
    if the_board[move] == ('X' or 'O'):
        print('Invalid move')
    else:
        the_board[move] = turn

    # Prints the board after every move
    print_board(the_board)
    '''
    Resets conditions after every move to check if any are met.
    Passes the state of the "board" to the function
    which sets the conditions as boolean values.
    The function returns the booleans in a list
    so they can be used in the next if-elif statements
     '''
    c = set_conditions(the_board)

    '''
    Checks each returned boolean from the list above
    to see if any conditions are met.
    If a condition is met, the program will print out the winner and exit.
    '''
    x_wins = c[0] or c[1] or c[2] or c[3] or c[4] or c[5] or c[6] or c[7]
    o_wins = c[8] or c[9] or c[10] or c[11] or c[12] or c[13] or c[14] or c[15]

    if x_wins:
        print('X is the winner!')
        sys.exit()
    elif o_wins:
        print('O is the winner!')
        sys.exit()
    elif ' ' not in the_board.values():
        print('The game is tied.')
        sys.exit()
