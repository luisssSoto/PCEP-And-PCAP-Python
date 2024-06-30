"""Build a new generator"""
'''1.'''
def generator(n):
    for i in range(n):
        yield i

for i in generator(5):
    print(i)
print()

'''2. generator to powers of 2'''
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for j in powers_of_2(5):
    print(j, end=' ') 
    if j == 16:
        print()
