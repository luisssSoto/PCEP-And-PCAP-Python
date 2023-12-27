'''for test'''
'''1. for with a bad range'''
#The main thing that you need to know is that there won't be any error message 
# in the next code:

i='any message error'
for i in range(5,5):
    print('snake 🐍')
print(i)

for i in range(6,5):
    print('snake 🐍')
print(i)

'''2. for with continue'''
for i in range(10):
    if i % 2 == 0:
        continue
    print(f'this is an odd number: {i}', end="\t")
print()
    
'''3. for with break'''
for i in range(10):
    if i == 3:
        break
    print(i,end=" | ")

'''4. for with else'''
for i in range(5):
    print(i)
else:
    print(i)
    
'''5. for with else and break'''
for i in range(10):
    print(i)
    break
else: print('Nothing to say')
print()

'''6. for with else even if never executes the for part'''
var_range=range(4,3)
i=4
for i in var_range:
    print('it won\'t work')
else: print('it will be')

'''7. the variable i works independiantelly'''
var_range=range(4)
i=4
for i in var_range:
    print('it\'ll work')
else: print('it will be')

'''8. range function can assign in a variable but its value is not an integer'''
var_range=range(3,10,3)
print(var_range)

'''9. look out with a tricky exercises like this:'''
for i in range(5):
    print(i-1)
else:
    print(i)