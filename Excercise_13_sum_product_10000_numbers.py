import random
from Excercise_13_sum_product import calculate_product, calculate_sum

numbers = [random.randint(1, 10000) for i in range(1000)]

print('Numbers:', numbers)
print(f'Sum is {calculate_sum(numbers)}')
print(f'Product is {calculate_product(numbers)}')