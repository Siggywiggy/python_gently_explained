from Excercise_20_Leap_year import is_leap_year


def is_valid_date(year, month, day):
    days_in_months = [31 for i in range(0, 12)]

    days_in_months[3] = 30
    days_in_months[5] = 30
    days_in_months[8] = 30
    days_in_months[10] = 30

    if is_leap_year(year) == True:
        days_in_months[1] = 29
    else:
        days_in_months[1] = 28

    if month > len(days_in_months):
        return False
    elif day > days_in_months[month - 1]:
        return False

    return True


print(is_valid_date(1999, 12, 31))
"""
print(is_valid_date(2000, 2, 29))
print(is_valid_date(2001, 2, 29))
print(is_valid_date(2029, 13, 1))
print(is_valid_date(1000000, 1, 1))
print(is_valid_date(2015, 4, 31))
print(is_valid_date(1970, 5, 99))
print(is_valid_date(1981, 0, 3))
print(is_valid_date(1666, 4, 0))
"""