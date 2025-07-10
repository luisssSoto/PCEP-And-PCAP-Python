"""Final Test"""
import calendar

# 1. weekheader()
print(calendar.weekheader(1))

# 2. Calendar class and iterweekdays()
c = calendar.Calendar(calendar.FRIDAY)
for weekday in c.iterweekdays():
    print(weekday)