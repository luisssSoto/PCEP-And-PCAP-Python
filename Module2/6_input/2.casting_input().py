"""The input() saves Strings for default"""
listening3 = input("Introduce any number: ")
print(listening3 * 5)
print(listening3 + '5')

#Note: When you put a negative value or 0 to multiply a string the
#result always will be an empty string, take a look at the next line
isEmpty='empty String'*0
print(isEmpty)
print('len of "isEmpty variable:"', len(isEmpty))

#The result above wasn't error but take a look at the next piece of code
try:
    print(listening3-2)
except TypeError:
    print("All inside an input function is a string")


"""Casting input()"""
value1 = input("Introduce any number from keyboard: ")
casting1 = float(value1)
print("This is possible now",  casting1, "*", 2, "=", casting1*2)

'''Easier way...'''
value2 = float(input("Introduce a number one more time: "))
print(value2, "-", 5, "=", value2-5)