"Calendar obj"
import calendar

"""firstweekday"""
c = calendar.Calendar(calendar.SUNDAY)
print(c.firstweekday)


"""iterweekdays"""
for day in c.iterweekdays():
    print(f"day: {day}", sep=" ")