"""Functions recursivity"""
print("Welcome to recursive Functions")

'''Factorial number is the most common case to use these kind of functions'''
def facFunction(facNumber):
    if facNumber == 1: return 1
    else: return facNumber * facFunction(facNumber-1) #5-4, 4-3, 3-2, 2-1---->return 1----2*1=2, 3*2=6, 4*6=24, 5*24=120

print(facFunction(5))

'''Adding Example'''
def addingRecursive(number1):
    if number1 == 20:
        return 6
    else:
        return number1 + addingRecursive(number1+4) # 5+8, 8+11, 11+14, 14+17, 17+20---->return 6 --->17+6=23, 14+23=37, 11+37=48, 8+48=56, 56+5=61 
print(addingRecursive(4))

'''Subtraction Example'''
def SubtractionRecursive(n):
    if n <= 1:
        return 2
    else:
        return n-SubtractionRecursive(n-1)# 4-3, 3-2, 2-1 ---->return 2---> 2-2=-0, 3-0=3, 4-3=1
print(SubtractionRecursive(4))
