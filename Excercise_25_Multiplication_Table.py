print(' 1|  2  3  4  5  6  7  8  9  10')
print('--+------------------------------')

# constructing the multiplication table 2D array
multiplication_table = [[] for i in range(0, 10)]

for x in range(1, 11):
    for y in range(1, 11):
        multiplication_table[x - 1].append(x * y)

# adjust the numbers to be right-adjusted in every column

column_widths = [len(str(i)) for i in multiplication_table[-1]]

row_list = list()
for x in range(len(multiplication_table)):
    row_string = str()
    for y in range(len(multiplication_table)):
        # add | tro the leftmost number in every row
        if y == 0:
            row_string += str(multiplication_table[x][y]).rjust(column_widths[y], ' ') + '|' + ' '
        else:
            row_string += str(multiplication_table[x][y]).rjust(column_widths[y], ' ') + ' '
    print(row_string)