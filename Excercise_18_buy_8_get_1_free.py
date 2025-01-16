def get_cost_of_coffe(num_coffees, price_per_coffee):
    # for every eight coffees you get 1 extra for free
    # num_coffees - number of coffees you order total
    if num_coffees <= 8:
        return num_coffees * price_per_coffee

    full_price_coffees = (num_coffees // 8) * 8
    free_coffees = num_coffees // 8
    extra_coffees = num_coffees - full_price_coffees - free_coffees

    total_cost = full_price_coffees * price_per_coffee + extra_coffees * price_per_coffee
    return total_cost


print(get_cost_of_coffe(7, 2.5))
print(get_cost_of_coffe(8, 2.50))
print(get_cost_of_coffe(9, 2.50))
print(get_cost_of_coffe(10, 2.50))

for i in range(1, 4):
    assert get_cost_of_coffe(0, i) == 0
    assert get_cost_of_coffe(8, i) == 8 * i
    assert get_cost_of_coffe(9, i) == 8 * i
    assert get_cost_of_coffe(18, i) == 16 * i
    assert get_cost_of_coffe(19, i) == 17 * i
    assert get_cost_of_coffe(30, i) == 27 * i

print(get_cost_of_coffe(1000000000, 2.50))