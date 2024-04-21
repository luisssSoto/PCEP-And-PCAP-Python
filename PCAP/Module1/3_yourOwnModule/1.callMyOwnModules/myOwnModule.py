#!/usr/bin/env python3 
#the line above is an instruction that means which program must be executed in order to interprets this text
# "#" this character is well-know as "hashbang", "shebang" etc.

#The line below is a "doc string" which explains the content and purpose of this module
"""myOwnModule.py is an example of a module in Python"""

'''It's important to know, that you can initialize any
variable you want but the user who is going to use your
module is available to modify that variable.
Now, you can specify as good practice, that this variable
is not allowed to modified it, adding __ two under score
character, but this is only a convention, eventhough any
user who can access to your module can modify the variable'''
__counter = 0

'''We're going to add two functions'''
def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

print('I like to be a "module"')

'''__name__variable says the name of the file that is being executed:
for instance; if you run this file just here, the variable name will keep
the value "__main__" but if you import this file like a module and run it
from that file, the value is going to be "nameOfModule" '''
print(__name__)

'''So that if you want to know the context where your code was executed, this is 
a way that you can take:'''
if __name__ == "__main__":
    print("This module is being executed from itself")
    # So, this is a convenient way to use the variable __name__
    # if we are executing this file from here... we can
    # do the tests from here instead run the tests every
    # time that the user imports our module
    my_list = [x + 1 for x in range(5)]
    print(f'Test suml: {suml(my_list) == 15}')
    print(f'Test prodl: {prodl(my_list) == 120}')
else: 
    print("Module is being executed by other file")
