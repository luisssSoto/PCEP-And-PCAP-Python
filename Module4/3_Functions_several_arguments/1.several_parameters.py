"""Functions -several parameters"""
print("Welcome to Functions with several parameters")

'''two parameters'''
def imc(weight, height):
    form=weight/height**2
    return form
patientImc=imc(78,1.81)
print(patientImc)

'''three parameters'''
def areaTriangle(base, height, con=2):
    area=base*height/con
    print('The triangle\'s area is:',area)

areaTriangle(5,2)