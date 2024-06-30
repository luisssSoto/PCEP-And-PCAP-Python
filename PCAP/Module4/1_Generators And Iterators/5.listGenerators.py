"""List and Generators"""
'''1. comprension list'''
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
list_of_powers_2 = [x for x in powers_of_2(10)]
print(list_of_powers_2)

'''2. list() function'''
def powers_of_two(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
list_of_powers = list(powers_of_two(10))
print(list_of_powers)        

'''3. in operator'''
for k in range(20):
    if k in powers_of_two(4):
        print(k)
        
'''4. fibonacci generator try to combine all we've learned'''

def fibonacci(n):
    value1 = value2 = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            current_number = value1 + value2
            value1, value2 = value2, current_number
            yield current_number

list_fibonacci = [x for x in fibonacci(10)]
print(list_fibonacci)