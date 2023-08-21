"""Function's Scope"""
print("Welcome Function's Scope")

'''1.You can't see a variable inside a function'''
def scope1():
    var1=1

try:
    print(var1)
except NameError:
    print('The code doesn\'t reach to look the var1')

'''2.But a function can see a variable outside the function'''
var2=2
def scope2():
    return var2

print(scope2())

'''3.BUT if exists a variable inside a function with the same name,this is the result:'''
var3=3
def scope3():
    var3="three"
    return var3

print(var3)
print(scope3())
print(var3)

'''This is possible because, we can say that the variable inside any function
has more hierarchy than the others'''