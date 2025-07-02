"""calendar.TextCalendar"""
from calendar import TextCalendar

my_text_calendar = TextCalendar(1)
print(my_text_calendar.formatmonth(2025, 7, 3, 1))
print()

from calendar import LocaleTextCalendar
"""calendar.LocaleTextCalendar"""
my_local_text_calendar = LocaleTextCalendar(0, "HELLO")
print(my_local_text_calendar)