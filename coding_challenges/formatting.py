# Write a function named 'format_number' that takes a non-negative number as its only parameter. 
# Your function should convert the number to a string and add commas as a thousand separators. 
# For example, calling format_number(1000000) should return "1,000,000". 

def format_number(number):
    #return 'The number is: {:,.0f}'.format(int(number))
    return f'The number is: {int(number):,}'


print(format_number('4000000'))