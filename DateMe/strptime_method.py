# the strptime() method is used to format the time stamp which is in a string format to datetime object

# Syntax = datetime.strptime(time_data, format_data)

# time_data = is the time present in string format
# format_data = is the data present in datetime format which is converted from time_data using this function

from datetime import datetime

# Consider the time stamp in string format
time_data = '22/02/21 16:16:00'

# format the string in the given format as time_data
format_data = '%y/%m/%d %H:%M:%S'

date = datetime.strptime(time_data, format_data)

print('date = ', date)

print('day = ', date.day)

print('hour = ', date.hour)