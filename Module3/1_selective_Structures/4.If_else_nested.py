"Nested if-else Make a decisions"
plan1 = "plan 1"
plan1A = "plan 1 A"
plan1B = "plan 1 B"

plan2 = "plan 2"
plan2A = "plan 2A"

condition1 = False
condition1A = True
condition2 = False


if condition1:
    print(plan1)
    if condition1A:
        print(plan1A)
    else:
        print(plan1B)
else:
    if condition2:
        print(plan2)
    else:
        print(plan2A)
    
'''Another example'''

chooseNumber=int(input('Choose any number between 0 to 100: '))
if chooseNumber > 0 and chooseNumber <= 50:
    if chooseNumber <= 25:
        print('Your number is between 0 to 25')
    else:
        print('Your number is between 26 to 50 ')
else:
    if chooseNumber <= 75:
        print('Your number is between 51 to 75')
    else:
        print('Your number is between 76 to 100')