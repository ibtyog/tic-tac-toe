board = [['.','.','.'],
         ['.','.','.'],
         ['.','.','.']]

def print_board():
    line = ''
    for row in board:
        line += f'{row[0]} | {row[1]} | {row[2]}\n----------\n'
    line = line[:-11]
    print(line)

def player_move(symbol):
    coor = ''
    while not coor.isdigit() or int(coor) < 11 or int(coor) > 33 or board[int(coor[1]) -1][int(coor[0]) -1] != '.':
        coor = input('Put XY (1-3)')
    board[int(coor[1]) - 1][int(coor[0]) - 1] = symbol

def canMove(x,y):
    if board[y][x] == '.':
        return True
    return False
def check_for_win():
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != '.':
        print(f'{board[0][0]} Won!')
        return True
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != '.':
        print(f'{board[1][0]} Won!')
        return True
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != '.':
        print(f'{board[2][0]} Won!')
        return True

    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != '.':
        print(f'{board[0][0]} Won!')
        return True
    if board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != '.':
        print(f'{board[0][1]} Won!')
        return True
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != '.':
        print(f'{board[0][2]} Won!')
        return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '.':
        print(f'{board[0][0]} Won!')
        return True
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[2][0] != '.':
        print(f'{board[0][2]} Won!')
        return True
    return False

def chech_if_blank():
    for row in board:
        for char in row:
            if char == '.':
                return True
    print('Tie')
    return False


def game():
    symbol = 'X'
    print_board()

    while not check_for_win() and chech_if_blank():
         player_move(symbol)
         print_board()
         if symbol == 'X':
            symbol = 'O'
         else:
             symbol = 'X'
game()