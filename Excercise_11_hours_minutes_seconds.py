
def get_hours_minutes_seconds(input_seconds):
    timestamp_dict = dict()
    if input_seconds == 0:
        return '0s'
    else:
        if input_seconds < 60:
            timestamp_dict['s'] = input_seconds
        if input_seconds >= 60:
            timestamp_dict['s'] = input_seconds % 60
            timestamp_dict['m'] = input_seconds // 60
        if timestamp_dict.setdefault('m', 0) >= 60:
            timestamp_dict['h'] = timestamp_dict['m'] // 60
            timestamp_dict['m'] = timestamp_dict['m'] % 60
        if timestamp_dict.setdefault('h', 0) >= 24:
            timestamp_dict['d'] = timestamp_dict['h'] // 24
            timestamp_dict['h'] = timestamp_dict['h'] % 24


    #print(output_string_list)
    output_string = ' '.join(str(timestamp_dict[key]) + key for key in list(reversed(timestamp_dict.keys())) if timestamp_dict[key] != 0)

    return output_string


#print(get_hours_minutes_seconds(30))
print(get_hours_minutes_seconds(30) == '30s')
print(get_hours_minutes_seconds(60) == '1m')
print(get_hours_minutes_seconds(90) == '1m 30s')
#print(get_hours_minutes_seconds(3600))
print(get_hours_minutes_seconds(3600) == '1h')
print(get_hours_minutes_seconds(3601) == '1h 1s')
print(get_hours_minutes_seconds(3661) == '1h 1m 1s')
print(get_hours_minutes_seconds(90042) == '1d 1h 42s')
print(get_hours_minutes_seconds(0) == '0s')
