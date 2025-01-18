def convert_str_to_int(string):
    symbols_dict =  {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7': 7, '8' : 8, '9' : 9 }

    is_negative = False

    if string[0] == '-':
        is_negative = True
        string = string[1:]

    #print(is_negative)

    multiplier = 1
    sum = int()

    for x in reversed(range(0, len(string))):
        sum += symbols_dict[string[x]] * multiplier
        multiplier *= 10

    if is_negative:
        return -abs(sum)
    else:
        return sum





print(convert_str_to_int('-456'))