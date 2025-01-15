# row - column
# even row - even columns are white, odd columns are black
# odd row - even columns are black, odd columns are white


def get_chess_square_color(num1, num2):
    if num1 not in range(0, 8) or num2 not in range(0, 8):
        return ''
    else:
        chess_board = [[] for i in range(0, 8)]
        for i in range(0, len(chess_board)):
            if i % 2 == 0:
                for j in range(0, len(chess_board)):
                    if j % 2 == 0:
                        chess_board[i].append('white')
                    elif j % 2 != 0:
                        chess_board[i].append('black')

            elif i % 2 != 0:
                for j in range(len(chess_board)):
                    if j % 2 == 0:
                        chess_board[i].append('black')
                    elif j % 2 != 0:
                        chess_board[i].append('white')

    return chess_board[num1][num2]


assert get_chess_square_color(0, 0) == 'white'

assert get_chess_square_color(1, 0) == 'black'

assert get_chess_square_color(0, 1) == 'black'

assert get_chess_square_color(7, 7) == 'white'

assert get_chess_square_color(0, 8) == ''

assert get_chess_square_color(2, 9) == ''

print(get_chess_square_color(7, 7))
print(get_chess_square_color(1, 0))
print(get_chess_square_color(7, 7))