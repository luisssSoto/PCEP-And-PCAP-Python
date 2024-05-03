""" Reading Integers Safetely """

def readingIntegers(value, min, max):
    condition = True 
    while condition:
        try:
            value = int(input(f'Type a number from {min} to {max}: '))
            assert value >= min and value <= max
            condition = False
            return value
        except ValueError:
            print('Error: incorrect input')
        except AssertionError:
            print('Error: the value is not allowed, the allow values are from ', min, ' to ', max)
        
print(readingIntegers(5, 0, 10))

'''Best way, because use an assert is not a good practice'''
def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: entrada incorrecta")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: el valor no está dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
    return value
v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)
print("El número es:", v)

       
                
            
            