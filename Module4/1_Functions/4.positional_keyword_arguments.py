"""Functions positional argument passing"""
print("Welcome to positional argument passing")

def bigToSmall(largest, larger, large):
    print(largest, 'is greater than:', larger, 'and', larger, 'is greater than:', large)

bigToSmall(10, 5, 2.5)

'''keyword argument passing'''
print("Welcome to keyword argument passing")
def concatenate(begin, end):
    print(begin+end)

concatenate(begin='Coco', end='drile')
concatenate(end='tamus', begin='Hipopo')

'''Mix they both each other'''
def adding(a,b,c):
    return a+b+c

result=adding(2,b=3,c=1)
print(result)
result=adding(2,3,c=1)
print(result)

#The only rule is put all of the positional arguments first and then keyword arguments
#If you don't follow this rule you'll get a sintax error, look at this:

#result=adding(a=3,7,2)#---->SyntaxError











