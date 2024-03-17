'''Scope test'''
#1
value = 1
def f():
    global value
    value = 2
    print(value)
value=3
f()
print(value)

#2
value = 1
def f():
    value = 2
    print(value)
value=3
f()
print(value)

#3
value = 1
def f(value):
    print(value)
value=3
f(value)
print(value)

#4
value = 1
def f():
    print(value)
f()
print(value)