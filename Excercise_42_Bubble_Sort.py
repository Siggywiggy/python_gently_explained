def bubble_sort(nums_list):
    for x in range(0, len(nums_list) - 1):
        swap_occurred = False
        for y in range(0, len(nums_list) - x - 1):
            if nums_list[y] > nums_list[y + 1]:
                swap_occurred = True
                nums_list[y], nums_list[y + 1] = nums_list[y + 1], nums_list[y]

        if swap_occurred:
            break

    return nums_list


print(bubble_sort([2, 0, 4, 1, 3]))
print(bubble_sort([2, 2, 2, 2]))