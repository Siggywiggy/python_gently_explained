import random

def shuffle(list_nums):
    for i in range(len(list_nums)):
        new_index = random.randint(0, len(list_nums) - 1)
        list_nums[i], list_nums[new_index] = list_nums[new_index], list_nums[i]

    #return list_nums

print(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(shuffle([]))

for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)
    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10
    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

