def merge_two_lists(list_1, list_2):
    merged_list = list()

    while list_1 or list_2:  # while either of the lists exists
        # if the first list is empty append all numbers
        # in the second list to the merged list
        if not list_1:
            merged_list.append(list_2.pop(0))
        # if the second list is empty append all numbers
        # in the first list to the merged list
        elif not list_2:
            merged_list.append(list_1.pop(0))
        # if the values are equal merge both in to the merged list
        elif list_1[0] == list_2[0]:
            merged_list.append(list_1.pop(0))
            merged_list.append(list_2.pop(0))
        # if the value at index 0 in first list is < 0
        # append it to the merged list and pop it off
        elif list_1[0] < list_2[0]:
            merged_list.append(list_1.pop(0))
        # if the value at index 0 in second list is < 0
        # append it to the merged list and pop it off
        else:
            # print(list_2[pointer_2])
            merged_list.append(list_2.pop(0))

    return merged_list


print(merge_two_lists([1, 3, 6], [5, 7, 8, 9]))
print(merge_two_lists([1, 2, 3], [4, 5]))
print(merge_two_lists([4, 5], [1, 2, 3]))
print(merge_two_lists([1, 2, 3], []))
print(merge_two_lists([], [1, 2, 3]))


def merge_two_lists_pointers(list_1, list_2):
    pointer_1 = 0
    pointer_2 = 0
    merged_list = list()

    # while loop runs until one of the pointers reaches the end of its respective list
    # or both reach the end if equal lists
    while pointer_1 < len(list_1) and pointer_2 < len(list_2):
        if list_1[pointer_1] < list_2[pointer_2]:
            merged_list.append(list_1[pointer_1])
            pointer_1 += 1
        elif list_2[pointer_2] < list_1[pointer_1]:
            merged_list.append(list_2[pointer_2])
            pointer_2 += 1
        # values are equal in both lists
        else:
            merged_list.append(list_1[pointer_1])
            merged_list.append(list_2[pointer_2])
            pointer_1 += 1
            pointer_2 += 1

    # merged list contains all the merged values from both lists
    # both pointers are at the end of both lists
    # - do nothing

    # if pointer_1 has not reached the end merge a slice pointer -> end
    if pointer_1 < len(list_1):
        for i in range(pointer_1, len(list_1)):
            merged_list.append(list_1[i])
    # if pointer_2 has not reached the end merge a slice pointer -> end
    elif pointer_2 < len(list_2):
        for j in range(pointer_2, len(list_2)):
            merged_list.append(list_2[j])

    # print(merged_list)
    return merged_list


print(merge_two_lists_pointers([1, 3, 6], [5, 7, 8, 9]))
print(merge_two_lists_pointers([1, 2, 3], [4, 5]))
print(merge_two_lists_pointers([4, 5], [1, 2, 3]))
print(merge_two_lists_pointers([2, 2, 2], [2, 2, 2]))
print(merge_two_lists_pointers([1, 2, 3], []))
print(merge_two_lists_pointers([], [1, 2, 3]))