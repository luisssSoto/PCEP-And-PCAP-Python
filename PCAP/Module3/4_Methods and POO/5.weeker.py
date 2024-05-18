""" Weeker """
class WeekDayError(Exception):
    adivice = 'format invalid try again, but, this time with one of these ones: \
            Lun, Mar, Mie, Jue, Vie, Sab, Dom'

class Weeker:
    __week = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']
    __daysOfWeek = len(__week)

    def __init__(self, day):
        self.__day = day
        if self.__day not in Weeker.__week:
            raise WeekDayError
 
    def __str__(self):
        return self.__day

    def add_days(self, n):
        self.__position = Weeker.__week.index(self.__day)
        self.__amount_days = n % Weeker.__daysOfWeek
        self.__distance = 6 - self.__position
        if self.__amount_days > self.__distance:
            self.__new_position = self.__amount_days - self.__distance - 1
            self.__day = Weeker.__week[self.__new_position]
        else:
            self.__day = Weeker.__week[self.__position + self.__amount_days]

    def substract_days(self, n):
        self.__position = Weeker.__week.index(self.__day)
        self.__amount_days = n % self.__daysOfWeek
        self.__distance = self.__position
        if self.__amount_days > self.__distance:
            self.__new_position = self.__amount_days - self.__distance
            self.__day = Weeker.__week[-self.__new_position]
        else:
            self.__day = Weeker.__week[self.__amount_days - 1]

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(3)
    print(weekday)
    weekday.substract_days(12)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
print()

''' Best solution '''
class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(3)
    print(weekday)
    weekday.subtract_days(12)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
