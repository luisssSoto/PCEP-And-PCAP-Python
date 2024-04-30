""" Your Life Path Number"""

# create a variable to store the input of the user related to their birth (AAAADDMM)
yourBirth = input('type your date of birth to the next format: YYYYDDMM: ')
# create a function with a int parameter
def yourLifePathNumber(dateOfBirth):
# create a variable which store the value to return
    strNumber = 0
    yourNumber = 0
# caught the value and separate each value and adding to a list
    dateList = dateOfBirth.replace('', ',').strip(',').split(',')
# create a loop to iterate for each value of the list and cast it to int and add to a variable to return
    for number in dateList:
        strNumber += int(number)
    strNumber = str(strNumber)
    for number in strNumber:
        yourNumber += int(number)
    return yourNumber

print(yourLifePathNumber('20000101'))

''' Better solution '''
date = input("Ingresa tu fecha de cumpleaños (en el siguiente formato: AAAAMMDD o AAAADDMM, 8 dígitos): ")
if len(date) != 8 or not date.isdigit():
    print("Formato de fecha inválida.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Tu Dígito de la Vida es: " + date)
