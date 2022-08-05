# Write a function to detect 13th Friday. The function can accept two parameters, and both will be numbers. 
# The first parameter will be the number indicating the month, and the second will be the year in four digits. 
# Your function should parse the parameters, and it must return True when the month contains a Friday with the 13th, else return False. 

from datetime import datetime
import calendar

def friday(month_no, year_no):

    # date with a friday 
    date = f'{year_no} {month_no} 13'

    # converting the date string to an object
    spooky = datetime.strptime(date, '%Y %m %d').weekday()

    # if the calendar month/year contains friday, return true, else false
    return (calendar.day_name[spooky]) == 'Friday'

print(friday(3, 2020))