"""Functions...parameters and arguments"""
print("Welcome to parameters and arguments")

def addition(parameter1, parameter2):
    result=parameter1+parameter2
    print(result)

argument1=5
argument2=4
addition(argument1, argument2)

def multiplication(parameter1, parameter2):
    result = parameter1 * parameter2
    return(result)

print(multiplication(3,7))

'''It's possible to declare variables with the same name that the function's parameter:'''
parameter1=10
addition(3,2)
print('parameter 1:', parameter1)

'''If you do a function with n parameter you need to call it 
with the same amount of parameters'''
#it will be an error
try:
    addition(argument1)
except TypeError:
    print("Miss one argument in this case")


