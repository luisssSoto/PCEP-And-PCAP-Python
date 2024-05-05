""" POO Stack 2: Adding methods """

class Stack:
    def __init__(self):
        self.__stack_list = []
    
    # Adding two methods
    # push method in order to push a new value to the stack
    def push(self, value):
        # self is used to at the same case of the constructor; to represents the object recently created
        self.__stack_list.append(value)
    
    # pop method in order to pop the last value that got in first (LIFO)
    def pop(self):
        last_value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return last_value

# Creating a couple of objects related to the above class:
stack1 = Stack()
stack1.push(1)
stack2 = Stack()
stack2.push(stack1.pop())
stack2.push(stack2.pop()+1)
print(stack2.pop())
    
'''Note: "self" As you can note, you must put a "self" parameter during the 
creation of the method, even if the method doesn't require any
parameter, you must asserunce to put it '''

'''Note: also you can realice that it is possible to access to a
protected attribute (__stack_list) by following the punctuation
rule and the self parameter:
self.__nameOfAttribute ...'''

'''Note: the methods push and pop are public in order to access
from outside the class '''
