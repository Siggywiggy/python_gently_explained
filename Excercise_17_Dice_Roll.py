import random


def roll_dice(repetitions):
    sum_rolls = 0
    for y in range(0, repetitions):
        sum_rolls += random.randint(1, 6)
    return sum_rolls


print(roll_dice(0))
print(roll_dice(2))
print(2 <= roll_dice(2) <= 12)
print(3 <= roll_dice(3) <= 18)
print(roll_dice(1000) != roll_dice(1000))
print(100 <= roll_dice(100) <= 600)