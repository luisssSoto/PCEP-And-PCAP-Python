"""Calling the Iterator from extern approach"""
class Fib:
    def __init__(self, nn):
        print('__init__ from Fib')
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1
    def __iter__(self):
        print('__iter__ from Fib')
        return self
    def __next__(self):
        print('__next__ from Fib')
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        self.__ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, self.__ret
        return self.__ret

class Class:
    def __init__(self, n):
        print('__init__ from Class')
        self.__iter = Fib(n)
    def __iter__(self):
        print('__iter__ from Class')
        return self.__iter

object1 = Class(8)

for i in object1:
    print(i)
        