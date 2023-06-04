"""Functions"""
print("Welcome Functions()")

#Integrated functions ----> print()
print("I'm a print()")
print()

#Module's functions
import math
print('The value of "PI" is:', math.pi)

#Own functions
bePolite="Hi nice to meet you I'm Luis Soto"
gitHub="https://github.com/luisssSoto"
def introduceMe():
    return bePolite, "and this is my GitHub:", gitHub

#calling own's functions
print("\n", introduceMe())
    
