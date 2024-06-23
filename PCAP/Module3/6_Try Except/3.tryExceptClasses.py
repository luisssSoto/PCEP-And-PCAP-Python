"""Try Except Classes"""
'''The Exceptions are classes and when an exception is generated,
an instance of the Exception Class born and this object pass 
through all the try-except block until it finds the block
"except" that handles that exception'''

try:
    i = int('Hola!')
except BaseException as e:
    print(e)
    print(e.__str__())

'''The code above has a few new words:
1. as: which put an alias
2. e: which is the new name of the object wich has been generated
the .__str__() method give us information above of the object
Note: this object only lives inside the block Exception'''

'''Interesting thing is if you don't handle the try-except block
Python will handle the error and show us the same message
stopping the program:'''

i = int('Hola!')
