hours = 0
am_pm = 'am'

for i in range(0, 23):
    hours += 1
    minutes = 0
    if hours > 12:
        am_pm = 'pm'
    
    for i in range(0, 4):
        if hours > 12 and minutes == 0:
            print(f'{hours - 12}:00{am_pm}')
        elif hours <= 12 and minutes == 0:
            print(f'{hours}:00{am_pm}')
        elif hours <= 12:
            print(f'{hours}:{minutes}{am_pm}')
        else:
            print(f'{hours - 12}:{minutes}{am_pm}')

        minutes = minutes + 15