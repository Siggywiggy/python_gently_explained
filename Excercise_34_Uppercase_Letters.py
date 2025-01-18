def get_uppercase(string):
    uppercase_dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

    new_string = str()
    for letter in string:
        if letter not in uppercase_dict.keys():
            new_string += (letter)
        else:
            new_string += (uppercase_dict[letter])

    return new_string

assert get_uppercase('Hello') == 'HELLO'
assert get_uppercase('hello') == 'HELLO'
assert get_uppercase('HELLO') == 'HELLO'
assert get_uppercase('Hello, world!') == 'HELLO, WORLD!'
assert get_uppercase('goodbye 123!') == 'GOODBYE 123!'
assert get_uppercase('12345') == '12345'
assert get_uppercase('') == ''