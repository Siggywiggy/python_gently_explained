def convert_int_to_str(number):
    if number == 0:
        return '0'

    if number < 0:
        number_is_negative = True
        number = abs(number)
    else:
        number_is_negative = False

    digits_int_to_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    number_string = str()
    while number > 0:
        last_digit = digits_int_to_str[number % 10]
        number_string += last_digit
        number = number // 10
    if number_is_negative:
        return '-' + number_string[::-1]
    else:
        return number_string[::-1]

"""
print(type(convert_int_to_str(142)))
print(convert_int_to_str(20567))
for i in range(-10000, 10000):
    print(i)
    print(convert_int_to_str(i))
    assert str(i) == convert_int_to_str(i)
    # assert convert_int_to_str(i) == str(i)
"""