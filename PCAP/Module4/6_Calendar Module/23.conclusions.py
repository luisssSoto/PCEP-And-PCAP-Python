"""Conclusions of the Section 6"""

# 1. calendar and constant days
import calendar

week = []
week.append(calendar.MONDAY)
week.append(calendar.TUESDAY)
week.append(calendar.WEDNESDAY)
week.append(calendar.THURSDAY)
week.append(calendar.FRIDAY)
week.append(calendar.SATURDAY)
week.append(calendar.SUNDAY)
for day_int in week:
    print(f"day of the week: {day_int}")
print()

# 2. calendar() and prcal()
from calendar import calendar, prcal
print(calendar(2025, 3, 1))
prcal(2025, 3, 1)
print()

# 3. month() and prmonth()
from calendar import month, prmonth
print(month(2025, 2, 2, 1))
prmonth(2025, 2, 4, 2)
print()

# 4. setfirstweekday
from calendar import setfirstweekday
import calendar
setfirstweekday(calendar.THURSDAY)
prmonth(2025, 2, 2, 1)
print()

# 5. weekday()
from calendar import weekday
independence_day = 4
print(weekday(2026, 7, independence_day))
print()

# 6. weekheader() if its parameter is more than 3... 
# it only will show us 3 words
from calendar import weekheader
print(weekheader(4))
print()

# 7. isleap()
from calendar import isleap
print(isleap(2025))
print()

# 8. Calendar class
from calendar import Calendar
c = Calendar(calendar.FRIDAY)
print(c.firstweekday)
print()

# 9. iterweekdays()
for day in c.iterweekdays():
    print(f"day: {day}", end=" ")