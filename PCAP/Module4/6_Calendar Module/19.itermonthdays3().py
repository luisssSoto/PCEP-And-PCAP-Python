"""itermonthdays3()"""

from calendar import Calendar

c = Calendar(firstweekday=6)
for year, month, day_month in c.itermonthdays3(2019, 11):
    print(f"year: {year}, month: {month}, day of month: {day_month}")