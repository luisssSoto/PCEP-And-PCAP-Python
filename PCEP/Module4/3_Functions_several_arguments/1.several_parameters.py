"""Functions -several parameters"""
print("Welcome to Functions with several parameters")

'''two parameters'''
def imc(weight, height):
    if weight < 0 or weight > 200 and \
        height < 1 or height > 2.5:
            return None
    else:
        form=weight/height**2
        return form
    
patientImc=imc(78,1.81)
print(patientImc)

'''Note: Could you see the "\" symbol on the line 6? you can use it
when the sentence is to large'''

'''three parameters'''
def areaTriangle(base, height, con=2):
    area=base*height/con
    print('The triangle\'s area is:',area)

areaTriangle(5,2)

'''Note if you want to assign only one value to several variables
you can do it, just what it's below:'''
a = b = 1
print(a, b)