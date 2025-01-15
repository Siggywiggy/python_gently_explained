def get_smallest(nums):

    if len(nums) == 0:
        return None
    else:
        smallest = nums[0]
        for num in nums:
            if num < smallest:
                smallest = num

    return smallest

print(get_smallest([3, 2, 1]))
print(get_smallest([28, 25, 42, 2, 28]))
print(get_smallest([1]))
print(get_smallest([]))

def get_biggest(nums):
    if len(nums) == 0:
        return None
    else:
        biggest = nums[0]
        for num in nums:
            if num > biggest:
                biggest = num

    return biggest