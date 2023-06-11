"""Functions None"""
print("Welcome \"None\"")

#Reasons to use None
#1. Assign None to any variable
isNone=None
if isNone == None:
    print('The value inside of the variable isNone is:', isNone)


#2.A wrong function
def wrongFunction(value):
    if value % 2 == 0:
        print("It's an even number",end=" ")
        return True

#1st case
wrongFunction(6)
print()

#2nd case
print(wrongFunction(6))

#3th case
result=wrongFunction(6)
print(result)

#4th case 
result=wrongFunction(5)
print(result)

#Another example
def nothingInside():
    pass
none=nothingInside()
print(none)