"""LAB """
# •	Crea una clase llamada MyCalendar que se extiende de la clase Calendar.
# •	Crea el método count_weekday_in_year con los parámetros de year y weekday. 
# El parámetro weekday debe tener un valor entre 0 y 6, donde 0 es el lunes y 
# 6 es el domingo. El método debe devolver el número de días como un número entero.
# •	En tu implementación, usa el método monthdays2calendar de la clase Calendar.

from calendar import Calendar

class MyCalendar(Calendar):
    def __init__(self, set_first_weekday):
        Calendar.__init__(self, set_first_weekday)
    def count_weekday_in_year(self, year, weekday):
        amount_days = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                for month_weekday in range(len(week)):
                    print(f"month: {week[month_weekday][0]}", end=" | ")
                    print(f"weekday: {week[month_weekday][1]}")
                    if week[month_weekday][1] == weekday and week[month_weekday][0] != 0:
                        amount_days += 1
        return amount_days

mc = MyCalendar(0)
print(mc.count_weekday_in_year(2000, 6))



