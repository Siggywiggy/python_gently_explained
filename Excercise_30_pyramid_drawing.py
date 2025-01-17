def draw_pyramid(height):
    for x in range(0, height):
        row = ' ' * (height - x) + '#' * (x * 2 + 1)
        print(row)
        # print(row.rjust(len(row) // 2, ' '))
        # print(row.rjust(height / 2 - x))


draw_pyramid(8)