import random
from Excersice_12_Smallest_Biggest import get_smallest

numbers = [random.randint(1, 1000) for i in range(1000000)]
print('Numbers:', numbers)
print(f'smallest number is {get_smallest(numbers)}')