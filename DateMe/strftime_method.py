# The strftime() method is used to convert date and time objects to their string representation. It takes one or more input of formatted code and returns the string representation.

# syntax = datetime.strftime(format)

from datetime import datetime 

def full_date(date):
    '''Takes in a date object and converst to a string representation. Example: Monday, Dec 2021'''
    format = '%A, %b %Y'

    return date.strftime(format)

date_obj = datetime.now().replace(microsecond=0)

print(full_date(date_obj))

