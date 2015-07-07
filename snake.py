import random

def red(s):
    return '\x1b[31m'+s+'\x1b[39'

board = [[random.choice([0, 1])]
         for _ in range(10)]

def display(board):
    print red('-'*len(board[0]))
    for row in board:
        print ''.join('x' if x else ' '
                      for x in row)
    print '-'*len(board[0])

display(board)


