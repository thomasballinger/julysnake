import random

## create random board
board = [[random.choice([0, 1])]
         for _ in range(10)]

def display(board):
    ## top border
    print '-'*len(board[0])
    ## display board
    for row in board:
        print ''.join('x' if x else ' '
                      for x in row)
    ## bottom border
    print '-'*len(board[0])

display(board)


