""" Count Stack Test """

class Stack:
    def __init__(self):
        self.__stack_list = []
    def push(self, value):
        self.__stack_list.append(value)
    def pop(self):
        last_value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return last_value

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0
    def get_counter(self):
        return self.__count
    def pop(self):
        self.__count += 1
        return Stack.pop(self)
    
countingStack1 = CountingStack()
for i in range(100):
    # Although this method (push) isn't explicitly in the CountingStack, is hierancy for its superclass Stack
    countingStack1.push(i) 
    print(countingStack1.pop())
print()
print(countingStack1.get_counter())


