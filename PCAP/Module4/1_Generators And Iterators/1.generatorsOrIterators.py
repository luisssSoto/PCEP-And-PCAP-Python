"""Generators or Iterators"""
'''It is a piece of code available to produce several values and control the iteration
process'''
'''for example the range() is a function an at the same time is an generator because
gives us several values and is called several times implicitly, so a function produce
one value, and it's called once'''
for i in range(5):
    print(i, end='|')
print('\n')
    
'''An iterator is an object that can work under of protocol iterator wich obey the
context of "for" and "in"
Also, an iterator must to have two methods:
1. __iter__() which return the object and it is neccesary in order Python start 
succesfully the iteration, this method extract the iterator and this can scan all
the components of the iterator, so once the object iterator is extract, gives the
control to the protocol iterator 
2. __next__() which return the next value; is responsible for control the proccess 
of iteration and finish the procces of the iteration, this method is called by 
for/in sentence'''

'''Example with Fib number'''
class Fib:
    def __init__(self, nn):
        print('__init__')
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1
    
    def __iter__(self):
        print('__iter__')
        return self
    
    def __next__(self):
        print('__next__')
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1,2]:
            return 1
        self.__rr = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, self.__rr
        return self.__rr
    
for i in Fib(10):
    print(i)

fib1 = Fib(10)
for i in fib1:
    print(i)