
def merge_lists(list_1, list_2):
    resulting_list = list()
    pointer_1 = 0
    pointer_2 = 0

    while pointer_1 < len(list_1) and pointer_2 < len(list_2):
        if list_1[pointer_1] < list_2[pointer_2]:
            resulting_list.append(list_1[pointer_1])
            pointer_1 += 1
        elif list_1[pointer_1] > list_2[pointer_2]:
            resulting_list.append(list_2[pointer_2])
            pointer_2 += 1
        elif list_1[pointer_1] == list_2[pointer_2]:
            resulting_list.append(list_2[pointer_2])
            resulting_list.append(list_1[pointer_1])
            pointer_1 += 1
            pointer_2 += 1

    if pointer_1 < len(list_1):
        for x in range(pointer_1,len(list_1)):
            resulting_list.append(list_1[x])
    elif pointer_2 < len(list_2):
        for x in range(pointer_2,len(list_2)):
            resulting_list.append(list_2[x])

    return resulting_list

print(merge_lists([1, 3, 6], [5, 7, 8, 9]))
print(merge_lists([1, 2, 3], [4, 5]))
print(merge_lists([4, 5], [1, 2, 3]))
print(merge_lists([2, 2, 2], [2, 2, 2]))
print(merge_lists([1, 2, 3], []))
print(merge_lists([], [1, 2, 3]))
