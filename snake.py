

board = [[1] * 10 for _ in range(10)]

def display(board):
    print '-'*len(board[0])
    for row in board:
        print ''.join('x' if x else ' '
                      for x in row)
    print '-'*len(board[0])

display(board)


