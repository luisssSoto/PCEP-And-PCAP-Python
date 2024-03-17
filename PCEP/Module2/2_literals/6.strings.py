'''Strings '''
snake='I\'m a little and cute snake'
print(snake)

"""Esc with \""""
print('Welcome to "Esc button"') 
print("I like \"One punch man\"")
print('I like "One punch man"')
stringEmpty = " "
print("This string is empty: ", stringEmpty, "\n")

print(type(stringEmpty))

"""Concat + and Multiply with strings"""
name = 'Guido'
lastName = 'Van Rossum '
print("My name is",name + " " + lastName)

fullName=name  + ' ' + lastName
threeTimes=fullName * 3
print(threeTimes)

#You just need to remember when you use "+" with strings it won't be any spaces between the words:
print('Coco'+'drile',' is a dangerous a wild'+' animal')