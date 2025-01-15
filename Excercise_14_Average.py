def average(nums):
    if len(nums) == 0:
        return None

    sum_result = 0
    for num in nums:
        sum_result += num
    return int(sum_result / len(nums))

print(average([1, 2, 3]) == 2)
print(average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2)
print(average([12, 20, 37]) == 23)
print(average([0, 0, 0, 0, 0]) == 0)

import random
random.seed(42)
test_data = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(test_data)
    print(average(test_data) == 2)