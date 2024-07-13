"""bytearray class"""
'''it's a class in Python which allows us to save amorphous data,
(bytes), it creates an object that can save the size of bytes that
you pass as argument:'''

'''1. this creates an object with 10 bytes of size, and all the values
inside of it are zeros 0 in hexadecimal system'''
amorphous_data = bytearray(10)
print(amorphous_data)

'''This object is like a list:'''
'''1. you can assign values'''
amorphous_data[-1] = 43
print(amorphous_data) # The value is going to appears decoded according to ASCII table

'''2. you can do indexation to get any element'''
last_value = amorphous_data[-1]
print(last_value) #but the time you get it will be encoded

'''3. len is allow too'''
print(len(amorphous_data))

'''4. And as you noticed it is mutable'''

'''5. only integer data is allow to add into the bytearray'''
try:
    amorphous_data.append(1.5)
except TypeError as typeError:
    print(typeError.args)
    print('only integers')
    try:
        amorphous_data.insert(-1, 256)
    except ValueError as valueError:
        print(valueError.args)
        print('values since 0 to 255')