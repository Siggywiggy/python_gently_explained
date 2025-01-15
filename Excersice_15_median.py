import math

from Excercise_14_Average import test_data


def median(nums):
    if len(nums) == 0:
        return None

    sorted_numbers = sorted(nums)
    print(sorted_numbers)
    if (len(sorted_numbers) % 2) != 0: # odd length list
        return sorted_numbers[(len(sorted_numbers) // 2)]
    elif (len(sorted_numbers) % 2) == 0: #even length list
        middle_1, middle_2  = (len(sorted_numbers) // 2 - 1), ((len(sorted_numbers) // 2))
        return (sorted_numbers[int(middle_1)] + sorted_numbers[int(middle_2)]) / 2

print(median([]))
print(median([1,2,3]))
print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]))
print(median([3, 7, 10, 4, 1, 9, 6, 2, 8]))

import random
random.seed(42)
test_data = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(test_data)
    print(median(test_data))