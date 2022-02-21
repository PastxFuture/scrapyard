from datetime import datetime

def house_date(date2):
    '''The following program takes a datetime object as an argument and finds the difference between the current date in days. '''
    date1 = datetime.now().replace(microsecond=0)

    return date2 - date1

# object - datetime(year, month, day, hour, minute, second)
date2 = datetime(2022, 3, 25, 12, 00, 00)

print(house_date(date2))