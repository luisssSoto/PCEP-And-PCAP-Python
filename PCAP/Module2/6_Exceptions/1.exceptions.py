"""Exceptions"""

try:
    print("try to do this: ")
    print(1/0)
except ZeroDivisionError:
    print("but if you can't do it, don't worry I'm here to help you")

'''1. Some code could lose'''
try:
    l = [x for x in range(3)]
    print(l[4])
    print("Hey I'm here!") #this instruction will lose
except IndexError:
    print('That element does not exist')

'''2. Wherever it's possible you must be specific about the exceptions'''
# bad practice
try:
    floatNumber = float(input('give a number: '))
    print(2/0)
except:
    print('Something happend :(')


'''3. good practice'''
# Note: only one exception will be execute
# Note: the most general exception must be at the end
# Note: If there are any match between the exception and the specified except the most general except will be executed
# Note: only can exist one general except (at the end)
try:
    number = int(input('give a number again: '))
    l = [x for x in range(3)]
    print(l[number])
except ValueError:
    print('That it is not a valid value')
except IndexError:
    print('Ups your number needs to be shorter')
except:
    print('maybe is a KeyBoardInterrupt')