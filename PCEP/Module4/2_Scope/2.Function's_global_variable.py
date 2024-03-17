"""Functions global variable"""
print("Welcome global variable")

def scope1():
    global var1
    var1=1
    return var1

var1='one'
print(var1)
print(scope1())
print(var1)

'''Note: This is possible because Python doesn't create a
new variable, it take the variable outside of the function
to with the same name'''