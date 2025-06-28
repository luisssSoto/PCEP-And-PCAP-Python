"""weekday function"""
import calendar
unknown_day = calendar.weekday(2025, 6, 28)
print(unknown_day)

def guessing_day(day):
    match day:
        case calendar.SUNDAY:
            print("Sunday")
        case calendar.MONDAY:
            print("Monday")
        case calendar.TUESDAY:
            print("Tuesday")
        case calendar.WEDNESDAY:
            print("Wednesday")
        case calendar.THURSDAY:
            print("Thursday")
        case calendar.FRIDAY:
            print("Friday")
        case calendar.SATURDAY:
            print("Saturday")

guessing_day(unknown_day)
