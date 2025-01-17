def print_handshakes(list_names):
    names = list_names
    handshakes = 0
    while names:
        shaker = names.pop(-1)
        for x in range(len(names)):
            print(f'{shaker} shakes hands with {names[x]}')
            handshakes += 1

    return handshakes


print(print_handshakes(['Alice', 'Bob', 'Carol', 'David']))