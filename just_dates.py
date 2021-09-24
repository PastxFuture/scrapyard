# from module import class(es)
from datetime import date, datetime

x = datetime.today()
y = x.strftime('%A, %dth %B, %Y')

print(f'Todays date is: {y}')


print(f'Year: {x.year}')
print(f'month: {x.month}')
print(f'day: {x.day}')