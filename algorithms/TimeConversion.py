# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
def convert_to_military_time(time_str):
    if time_str[-2:] == 'PM' and time_str[:2] != '12':
        hours = str(int(time_str[:2]) + 12)
    elif time_str[-2:] == 'AM' and time_str[:2] == '12':
        hours = '00'
    else:
        hours = time_str[:2]
    
    military_time = hours + time_str[2:-2]
    return military_time

# Input the time in 12-hour format
time_12_hour = input("Enter time in 12-hour format: ")

military_time = convert_to_military_time(time_12_hour)
print("Time in 24-hour military format:", military_time)
