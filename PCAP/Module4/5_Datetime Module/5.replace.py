'''replace method to change the values of day, month, year'''
from datetime import date
print(date)
currentDay = date.today()
print(currentDay)

try:
    print(currentDay.day)
    currentDay.day = 3
except Exception as e:
    print(e)
    print('Those values are only for reading')

# Instead of that use replace method
currentDay = currentDay.replace(year = 1994, month = 2, day = 4)
print(currentDay)
    