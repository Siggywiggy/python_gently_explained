def draw_box(size):
    if size < 1:
        return None

    pipe = '|'
    corner = '+'
    space = ' '
    diagonal = '/'
    bottom_horizontal = corner + (size * 2 * '-') + corner
    middle_horizontal = bottom_horizontal + (size * ' ') + '+'
    top_horizontal = ((size + 1) * ' ') + bottom_horizontal

    print(top_horizontal)
    for i in range(1, size + 1):
        side_row = space + ((size - i) * space) + diagonal + (2 * size * space) + diagonal + space * (i - 1) + pipe
        print(side_row)

    print(middle_horizontal)
    for i in range(1, size + 1):
        side_row = pipe + (2 * size * space) + pipe + (space * (size - i)) + diagonal
        print(side_row)

    print(bottom_horizontal)


draw_box(1)