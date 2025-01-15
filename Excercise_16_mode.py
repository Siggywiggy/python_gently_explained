def mode(nums):
    if len(nums) == 0:
        return None
    else:
        frequency_dict = dict()
        for num in nums:
            frequency_dict.setdefault(num, 0)
            frequency_dict[num] += 1

    freq_num, largest_frequency = 0, 0
    for key, value in frequency_dict.items():
        if value > largest_frequency:
            freq_num = key
            largest_frequency = value

    return freq_num


print(mode([]) == None)

print(mode([1, 2, 3, 4, 4]) == 4)
print(mode([1, 1, 2, 3, 4]) == 1)
print(mode([1, 1, 2, 3, 4]) == 1)

import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    print(mode(testData) == 4)