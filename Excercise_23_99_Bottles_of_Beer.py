for i in range(99, -1, -1):
    if i == 0:
        print('No mode bottles of beer on the wall!')
    elif i == 1:
        print(f'{i} bottle of beer on the wall, \n{i} bottle of beer, \nTake one down, \nPass it around,')
    else:
        print(f'{i} bottles of beer on the wall, \n{i} bottles of beer, \nTake one down, \nPass it around,')