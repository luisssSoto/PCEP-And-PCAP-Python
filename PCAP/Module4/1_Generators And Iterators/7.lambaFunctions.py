"""Lambda Functions"""
'''Anonym functions'''
two = lambda: 2
sqr = lambda x : x * x
pwr = lambda x, y : x ** y

for i in range(-2, 3):
    print(sqr(i), end=' -> ')
    print(pwr(i, two()))

'''As you can see even though they are anonym functions you can assign them to
any variable, as a good practice lambda functions shouldn't be called like this
approach, instead is high recommendaly use them at the exact spot you're going
to need them.... '''
