"""The input() saves Strings for default"""
listening3 = input("Introduce any number")
try:
    print(listening3 * 2)
except TypeError:
    print("All inside an input function is a string")

"""Casting input()"""
value1 = input("Introduce any number from keyboard: ")
casting1 = float(value1)
print("This is possible now",  casting1, "*", 2, "=", casting1*2)

'''Easier way...'''
value2 = float(input("Introduce a number one more time: "))
print(value2, "-", 5, "=", value2-5)