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
