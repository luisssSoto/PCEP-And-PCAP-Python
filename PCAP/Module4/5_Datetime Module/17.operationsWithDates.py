from datetime import date
from datetime import datetime

date1 = date(2021, 11, 4)
date2 = date(2020, 11, 4)
print(f"date 1: {date1} and date 2: {date2}")
print(date1 - date2)

datetime1 = datetime(2021, 11, 4, 15, 30, 20, 0)
datetime2 = datetime(2020, 10, 3, 15, 25, 15, 0)
print(f"date time 1: {datetime1} and date time 2: {datetime2}")
print(datetime1 - datetime2)