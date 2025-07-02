"""calendar.HTMLCalendar"""
from calendar import HTMLCalendar

my_html_calendar = HTMLCalendar(0)
print(my_html_calendar.formatyear(2025, 5))
print()

from calendar import LocaleHTMLCalendar
"""calendar.LocaleHTMLCalendar"""
my_locale_html_calendar = LocaleHTMLCalendar(0, "Test")
print(my_locale_html_calendar.formatday(2025, 5))