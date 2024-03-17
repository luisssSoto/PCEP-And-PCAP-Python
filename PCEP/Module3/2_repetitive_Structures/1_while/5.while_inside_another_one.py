'''You can add a while inside another one and works this way
external while runs first and then the inside while, when the inside while finished
then the external while runs again'''
secretNumber=13
while secretNumber % 2 != 0:
    while secretNumber > 3:#you can modify the var to odd number and never go out to loop
        print(secretNumber)
        secretNumber-=1
    print('I\'m still inside of the loop')
else:print('It\'s cool isn\'it?')