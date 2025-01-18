def reverse_string(string):
    if len(string) == 0:
        return ''


    reversed_string = str()
    for x in (range(len(string)-1, -1, -1)):
        reversed_string += string[x]

    return reversed_string

print(reverse_string('Hello'))
print(reverse_string(''))
print(reverse_string('aaazzz'))

def reverse_string_2(string):
    char_list = list(string)
    for x in range(0, (len(string) // 2)):
        char_list[x], char_list[len(string) - 1 - x] = char_list[len(string) - 1 - x], char_list[x]

    return ''.join(char_list)

print(reverse_string_2('Hello'))