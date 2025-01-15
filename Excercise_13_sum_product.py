def calculate_sum(nums):
    if len(nums) == 0:
        return 0
    else:
        result = 0
        for num in nums:
            result += num

        return result

def calculate_product(nums):
    if len(nums) == 0:
        return 1
    else:
        product = 1
        for num in nums:
            product *= num

        return product

print(calculate_sum([]))
print(calculate_sum([2, 4, 6, 8, 10]) == 30)
print(calculate_product([]) == 1)
print(calculate_product([2, 4, 6, 8, 10]))