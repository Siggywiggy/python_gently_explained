from random import randint, shuffle

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = [letter.upper() for letter in lowercase_letters]
numbers = [str(num) for num in range(0, 10)]
special_characters = '~!@#$%^&*()_+.'

symbols = [lowercase_letters, uppercase_letters, numbers, special_characters]


def check_upper(letters):
    for letter in letters:
        if letter in uppercase_letters:
            return True
    return False


def check_lower(letters):
    for letter in letters:
        if letter in lowercase_letters:
            return True
    return False


def check_numbers(letters):
    for letter in letters:
        if letter in numbers:
            return True
    return False


def check_special(letters):
    for letter in letters:
        if letter in special_characters:
            return True
    return False


def generate_password(length):
    password = list()
    if length < 12:
        length = 12

    for i in range(0, length):
        if check_lower(password) != False:  # not false aka has lowercase letters
            selection_lists = [uppercase_letters, numbers, special_characters]
            sublist = randint(0, len(selection_lists) - 1)
            # print(selection_lists[sublist])
            symbol = randint(0, len(selection_lists[sublist]) - 1)
            # b print(symbol)
            password.append(selection_lists[sublist][symbol])
        elif check_upper(password) != False:  # has uppercase letters already
            selection_lists = [lowercase_letters, numbers, special_characters]
            sublist = randint(0, len(selection_lists) - 1)
            # print(selection_lists[sublist])
            symbol = randint(0, len(selection_lists[sublist]) - 1)
            # b print(symbol)
            password.append(selection_lists[sublist][symbol])
        elif check_numbers(password) != False:  # has numbers already
            selection_lists = [lowercase_letters, uppercase_letters, special_characters]
            sublist = randint(0, len(selection_lists) - 1)
            # print(selection_lists[sublist])
            symbol = randint(0, len(selection_lists[sublist]) - 1)
            # b print(symbol)
            password.append(selection_lists[sublist][symbol])
        elif check_special(password) != False:  # has a symbol already
            selection_lists = [lowercase_letters, uppercase_letters, numbers]
            sublist = randint(0, len(selection_lists) - 1)
            # print(selection_lists[sublist])
            symbol = randint(0, len(selection_lists[sublist]) - 1)
            # b print(symbol)
            password.append(selection_lists[sublist][symbol])
        else:  # has all the mandatory 1 upper, 1 lower, 1 symbol and 1 number already
            selection_lists = [lowercase_letters, uppercase_letters, numbers, special_characters]
            sublist = randint(0, len(selection_lists) - 1)
            # print(selection_lists[sublist])
            symbol = randint(0, len(selection_lists[sublist]) - 1)
            # b print(symbol)
            password.append(selection_lists[sublist][symbol])

    shuffle(password)  # shuffling the password list to add a layer of randomness
    return ''.join(password)


pw = generate_password(14)
print(pw)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False

for character in pw:

    if character in lowercase_letters:
        hasLowercase = True

    if character in uppercase_letters:
        hasUppercase = True

    if character in numbers:
        hasNumber = True

    if character in special_characters:
        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial