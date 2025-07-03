"""itermonths()"""
import calendar 
c = calendar.Calendar()
count_days = 0
for date in c.itermonthdates(2019, 11):
    if count_days == 7:
        print('end of the week')
        count_days = 0
    print(date, end=" | ")
    count_days += 1