from random import randrange

def gen_lights_out_board(n, level) :
    board = []
    for row in range(n) :
        board.append([])
        for col in range(n) :
            board[row].append(1)
    match (level.lower()) :
        case 'easy' :
            numMoves = (n+1)//2
        case 'hard' :
            numMoves = n*n
        case _ :
            numMoves = n
    for i in range(numMoves) :
        row, col = random_row_col(n)
        apply_move(board, row, col)
    return board

def random_row_col(n) :
    return randrange(n), randrange(n)

def apply_move(board, row, col) :
    n = len(board)
    board[row][col] *= -1
    if row > 0 :
        board[row-1][col] *= -1
    if row < n-1 :
        board[row+1][col] *= -1
    if col > 0 :
        board[row][col-1] *= -1
    if col < n-1 :
        board[row][col+1] *= -1

def print_board(board) :
    n = len(board)
    edge = ' +' + '-+'*n
    rownum = 1
    print(edge)
    for row in board :
        print(f'{rownum}|',end="")
        for ch in row :
            print(f'{" " if ch==1 else "X"}{"|"}',end="")
        print()
        rownum += 1
        print(edge)
    print(' ',end="")
    for i in range(1,n+1) :
        print(f'{i:2}', end="")
    print()

def game_over(board) :
    n = len(board)
    for row in board :
        for ch in row :
            if ch == -1 :
                return False
    return True

def lights_out(n=5, level = 'Medium') :
    board = gen_lights_out_board(n, level)
    while (not game_over(board)) :
        print_board(board)
        val = input('Enter row,col to press --> ')
        try :
            row, col = val.split(",")
        except :
            row, col = val.split()
        apply_move(board, int(row)-1, int(col)-1)
    print_board(board)
    print('Congratulations!')
    print()

def game_over(board):
    for row in board:
        for square in row:
            if square == -1:
                return False
    return True

def lights_out(n=5) :
    board = gen_lights_out_board(n)
    while (not game_over(board)) :
        print_board(board)
        row,col = input('Enter row,col to press --> ').split(',')
        apply_move(board, int(row)-1, int(col)-1)
    print_board(board)
    print('Congratulations!')

