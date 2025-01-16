from Excercise_20_Leap_year import is_leap_year


def is_valid_date(year, month, day):
    # check for invalid month and day values
    if month == 0 or day == 0:
        return False
    # set up the basic days per month list
    days_in_months = [31 for i in range(0, 12)]
    # editexceptions (30 day months)
    days_in_months[3] = 30
    days_in_months[5] = 30
    days_in_months[8] = 30
    days_in_months[10] = 30

    #print(days_in_months)
    # check for leap years and num of days in february
    if is_leap_year(year) == True:
        #print('its leap year!')
        days_in_months[1] = 29
    else:
        days_in_months[1] = 28

    # check if month is a valid month (invalid > 13!)
    if month > len(days_in_months):
        return False
    # check if days is a valid value
    elif day > days_in_months[month - 1]:
        return False
    else:
        return True






print(is_valid_date(1999, 12, 31))

print(is_valid_date(2000, 2, 29))
print(is_valid_date(2001, 2, 29))
print(is_valid_date(2029, 13, 1))
print(is_valid_date(1000000, 1, 1))
print(is_valid_date(2015, 4, 31))
print(is_valid_date(1970, 5, 99))
print(is_valid_date(1981, 0, 3))
print(is_valid_date(1666, 4, 0))
