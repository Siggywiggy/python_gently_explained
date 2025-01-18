def make_change(pennies):
    nickel_pennies = 5
    dime_pennies = 10
    quarter_pennies = 25
    change_dict = {}

    quarters = pennies // quarter_pennies

    if quarters:
        pennies = pennies % quarter_pennies
        change_dict['quarters'] = quarters

    dimes = pennies // dime_pennies

    if dimes:
        pennies = pennies % quarter_pennies
        change_dict['dimes'] = dimes


    nickels = pennies // nickel_pennies

    if nickels:
        change_dict['nickels'] = nickels
        pennies = pennies % nickel_pennies

    if pennies > 0:
        change_dict['pennies'] = pennies


    return change_dict

print(make_change(57))