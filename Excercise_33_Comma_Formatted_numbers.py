

def comma_format(number):
    # convert number to string
    converted = str(number)

    # remove commas from front and end of the number

    converted = converted.strip(',')

    fraction = str()

    # check if the number is a float

    if '.' in converted:
        comma_separated = converted.split('.')
        if len(comma_separated[1]) >= 3: # if the len of full numbers is >= 3
            converted = comma_separated[0]
            fraction = comma_separated[1]


    # return the unchanged string if the length of full numbers is <= 3
    if len(converted) <=3 and fraction: # if it was a fractional number add the fractions back in
        return converted + '.' + fraction
    elif len(converted) <= 3 and not fraction:
        return converted

    # deal with numbers >= 3 in length

    counter = 0
    with_commas = list()

    for x in range(len(converted) - 1, -1, -1):
        with_commas.append(converted[x])
        counter += 1
        if counter % 3 == 0 and (x != 0): # check if its been 3 numbers from the rear and its not the very first number
            with_commas.append(',')

    with_commas.reverse()

    # add or dont add the fractions
    if fraction:
        return ''.join(with_commas) + '.' + fraction
    if not fraction:
        return ''.join(with_commas)


print(comma_format(1000.123456))
print(comma_format(100.123456))