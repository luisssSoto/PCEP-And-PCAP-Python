"""itermonthdays()"""

from calendar import Calendar

c = Calendar()

for day_month, day_week in c.itermonthdays2(2019, 11):
    print(f"day of month: {day_month}, day of week: {day_week}" )