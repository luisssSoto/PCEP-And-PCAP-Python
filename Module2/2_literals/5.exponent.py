'''Exponent'''
print("Welcome to Exponent")
print("This is one way: " , 2 * 10 ** 8)
print("This is the shorter way: ", 2e8, "or this way  is rigth too", 2E8)

#the exponent only can be integer numbers
print(2.5e8)
#print(2e8.5)---->it'll be an error
#print(2.5e2.8)---->it'll be an error

#but you can write down in the traditional way with float number too
print(2*10**8.5)
#print(2e8.5)---->it'll be an error
print(2.5*10**2.8)
#print(2.5e2.8)---->it'll be an error

plank = 6.62607E-34
print("It's allow use negative numbers", plank, "Python translate the shorter version adding an \"E\" at the end \n")
