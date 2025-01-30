'''today() method'''
import datetime

currentDate = datetime.date.today()
print(currentDate)

'''Attributes of date class'''
print(f'Year: {currentDate.year}')
print(f'Month: {currentDate.month}')
print(f'Day: {currentDate.day}')
print(hasattr(currentDate, 'year'))