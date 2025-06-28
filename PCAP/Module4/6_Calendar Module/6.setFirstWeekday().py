"""setFirstWeekday()"""
import calendar

sunday = calendar.SUNDAY
print(sunday)
calendar.setfirstweekday(sunday) # the parameter is only an integer
calendar.prmonth(2025, 1)
print()

calendar.setfirstweekday(1)
print(calendar.month(2025, 1))