def draw_border(width, height):
    if width < 2 or height < 2:
        return None

    corner = '+'
    edge = '|'
    top_bottom_line = corner + '-' * (width - 2) + corner
    print(top_bottom_line)

    for x in range(0, (height - 2)):
        mid_line = edge + ' ' * (width - 2) + edge
        print(mid_line)

    print(top_bottom_line)


draw_border(2, 2)