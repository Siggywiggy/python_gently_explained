def rot13(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pointer = 0
    new_string = str()

    for x in range(0, len(input_string)):
        # if the letter is not a letter, add it to the resulting string unchanged
        if not input_string[x].isalpha():
            new_string += input_string[x]
            continue

        # check if letter is uppercase
        letter_is_uppercase = input_string[x].isupper()
        # get the letters current index
        old_index = alphabet.find(input_string[x].lower())
        # add 13 to the current index and use % 26 to "wrap around" to start
        # if the new index is larger than the length of alphabet
        new_index = (old_index + 13) % 26
        # if letter was uppercase, append uppercase letter
        if letter_is_uppercase:
            new_string += alphabet[new_index].upper()
        else:
            new_string += alphabet[new_index]

    return new_string


print(rot13('Hello, WORLD'))
print(rot13('Hello, World'))
print(rot13(rot13('Hello, World!')))
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'