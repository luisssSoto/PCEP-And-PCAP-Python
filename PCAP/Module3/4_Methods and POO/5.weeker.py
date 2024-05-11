""" Weeker """
class WeekDayError(Exception):
    adivice = 'format invalid try again, but, this time with one of these ones: \
            Lun, Mar, Mie, Jue, Vie, Sab, Dom'

class Weeker:
    __week = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']
    #
    # Escribir código aquí.
    #

    def __init__(self, day):
        self.__day = day
        if self.__day not in Weeker.__week:
            raise WeekDayError

    def __str__(self):
        pass
        #
        # Escribir código aquí.
        #

    def add_days(self, n):
        pass
        #
        # Escribir código aquí.
        #

    def subtract_days(self, n):
        pass
        #
        # Escribir código aquí.
        #

try:
    day = Weeker('Lu')
except WeekDayError:
    print(WeekDayError.adivice)
    print('continue')


# try:
#     weekday = Weeker('Lun')
#     print(weekday)
#     weekday.add_days(15)
#     print(weekday)
#     weekday.subtract_days(23)
#     print(weekday)
#     weekday = Weeker('Lunes')
# except WeekDayError:
#     print("Lo siento, no puedo atender tu solicitud.")
    