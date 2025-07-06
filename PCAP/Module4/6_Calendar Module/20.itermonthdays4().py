"""itermonthdays4()"""
from calendar import Calendar

c = Calendar(6)

for date in c.itermonthdays4(2019, 11):
    print(f"date: {date}")