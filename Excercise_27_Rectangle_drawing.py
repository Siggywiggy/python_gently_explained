def draw_rectangle(width, height):
    if width <= 0 or height <= 0:
        return None

    row = '#' * width * 2
    for x in range(height):
        print(row)


draw_rectangle(4, 6)