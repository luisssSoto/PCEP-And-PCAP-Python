"""weekheader()"""
import calendar
print(calendar.weekheader(1))

# Note: if use setfirstweekday affects the result of weekheader()
calendar.setfirstweekday(2)
print(calendar.weekheader(1))
print(calendar.weekheader(10))