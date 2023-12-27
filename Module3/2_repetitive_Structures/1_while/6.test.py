'''while test'''

'''1. while with a count'''
count=0
while count <= 10: 
    if count % 2 != 0: print(count)
    count += 1
    
'''2. while with a break'''
while True:
    print(True)
    break

'''3. while with an else'''
while False:
    print(False)
else:
    print(False, 'because of else')
    
'''4. while with a break an else'''
while True:
    print(True)
    break
else:print('Won\'t execute')

'''5. while inside another one'''
while False:
    print('external while')
    while True:
        print('internal while')
        break
    break
else:print('this else will execute if the first condition is False')

'''6. while exercise'''
count=3
while count > 0:
    print(count+1, end="\t")
    count-=1
else:
    print('There is nothing breaks here so that this part will be execute')
    
