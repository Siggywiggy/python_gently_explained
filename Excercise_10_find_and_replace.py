def find_and_replace(inputstr, old_text, new_text):
    # start with the first pointer at index 0
    # and end pointer at the final index of the word we are searching for

    start_pointer = 0
    end_pointer = len(old_text)
    # the very last index we wish to search to - end of the string
    final_index = len(inputstr)
    # a new string variable that will contain our corrected string
    final_text = str()

    while start_pointer < final_index:  # True if the start pointer has not reached the end of the string
        # if the slice between pointers == string we are searching for
        if inputstr[start_pointer:end_pointer] == old_text:
            # print(f'found {inputstr[start_pointer:end_pointer]} between {start_pointer} and {end_pointer} indexes!')
            final_text += new_text  # append replacement string to corrected string
            start_pointer += len(
                old_text)  # increment the pointers by the lenght of the term we are searching for, skipping the rest of the letters
            end_pointer += len(old_text)
        else:
            # if no match add the character at start pointer to corrected string
            final_text += inputstr[start_pointer]
            # increment pounters by 1
            start_pointer += 1
            end_pointer += 1

    return final_text


assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
print(find_and_replace('The fox', 'fox', 'dog') == 'The dog')
print(find_and_replace('fox', 'fox', 'dog') == 'dog')
print(find_and_replace('foxfox', 'fox', 'dog') == 'dogdog')
print(find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.')