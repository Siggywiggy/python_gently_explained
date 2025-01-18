def get_title_case(string):
    # if the string is empty return an empty string
    if len(string) == 0:
        return ''

    #print(string)
    # uppercase letters dict
    uppercase_dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I',
                      'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
                      's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    # constructing list of possible separators - special characters + numbers 0-9
    separators = [' ', '~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '.', ',', '']
    numbers = [str(num) for num in range(0, 10)]
    for number in numbers:
        separators.append(number)

    # separate the words in to a list of strings, word and separators are list items
    separated_words = list()
    while True:
        sub_word = str()
        counter = 0 # counting letters worked trought o break out of the loop in the end
        for x in range(0, len(string)):
            # if the current letter is in separators add the constructed sub_word to
            # separated words list, and add the separator as a separate list item right after it
            if string[x] in separators:
                separated_words.append(sub_word) #adding the word before the separator
                separated_words.append(string[x]) # adding the separator
                sub_word = str() # reset sub word
                counter += 1
                continue
            # once we have reached the end of the original string append the last sub_word to the list
            elif string[x] == string[-1]:
                sub_word += string[x]
                separated_words.append(sub_word)
                counter += 1
            else: # if the current letter not in separators and not the final letter add the letter to constructed sub_word
                sub_word += string[x]

            counter += 1 # add to the counter

        if counter >= len(string): # break out of the loop if we have reached the end of the original string
            break

    # turn all the separated words in to lowercase words
    #print(separated_words)
    lowercase_separated_words = [word.lower() for word in separated_words]
    #print(lowercase_separated_words)

    # convert all words in to Title case:
    titlecase_words_list = list()
    for word in lowercase_separated_words:
        if word not in separators:
            # take the first letter of the word
            first_letter = word[0]
            # append the first letter in Title case + the rest of the letter in the word
            # to new titlecase words list
            titlecase_words_list.append(uppercase_dict[first_letter] + word[1:])
        else:
            # adding the separator to the list
            titlecase_words_list.append(word)

    #print(titlecase_words_list)

    return (''.join(titlecase_words_list))



print(get_title_case('hElLo'))
print(get_title_case('cat,dog,RAT'))
print(get_title_case('Hello, world!'))
print(get_title_case('abc123xyz'))
print(get_title_case('HELLO'))