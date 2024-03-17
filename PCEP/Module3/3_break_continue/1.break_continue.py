"""continue and break"""
print("Welcome to continue and break")
print('"break"')
for i in range(5):
    if i == 2:
        break;
    print(i)

print('\n"continue"')
for j in range(5):
    if j == 2:
        continue
    print(j)

'''3. Note: when you work with continue the flow control is going through the 
immediately last selective structure where the continue was executed, try to 
debug the next code'''

value1=1
while value1 >= 1:
    print('once')
    while value1 <= 2:
        print('twice')
        value1+=1
        continue
        print('something')
    value1-=2

'''4. Note: when you work with continue the flow control is going through the 
immediately next line of code below where the break was executed, try to 
debug the next code'''

value1=1
while value1 >= 1:
    print('once')
    while value1 <= 2:
        print('twice')
        value1+=1
        break
        print('something')
    value1-=2