from random import random

'''random() is a function belongs to random module, create a number between 0.0 and <1.0'''
for i in range(5):
    print(random())
    
'''seed is another function without arguments, set the value according to the time
and seed with an argument set the value according to the int argument given,
In nutshills, seed is a function which set the random() function to change its behavior'''
from random import seed

#This is definetely predectible
seed(0)
for i in range(5):
    print(random())

#This is not predectible
seed()
for i in range(5):
    print(random())
    
'''randrange() and randint()'''
from random import randrange, randint

'''randrange() there is an exclusion in the last number'''
print(randrange(5), end='\t')
print(randrange(3,5), end='\t')
print(randrange(0,5,2))

'''randint() there is nothing exclusion in the last number, 
I mean, the last number is included'''
print(randint(0, 5))

#Note: but unfortanetely these both functions can repeat the same number
for i in range(5):
    print(randrange(0,6), end="\t")
    if i == 4:
        print()
    
for i in range(5):
    print(randint(0,3), end='\t')

print()

'''There are other functions with can handle with the weakness of the both functions
above metioned: choice() and sample()'''
from random import choice, sample

myList=[i for i in range(11) if i % 2 == 0]

'''choice() takes as argument a list and choice only one element from it'''
print(choice(myList))

'''sample() takes as argument a list too, but you can choice as a second argument
the numbers you want to choice'''
print(sample(myList, 1))
print(sample(myList, 6))

#Note: but, be careful, because if you type as a second argument, more numbers that
#the total of numbers of the list, will be an error

try:
    print(sample(myList, 7))
except ValueError as larger:
    print('''The second argument is larger than the list in the first argument
          This is the error: ''', larger)
