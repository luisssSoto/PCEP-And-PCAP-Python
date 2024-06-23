"""Hierarcy of Try-Except"""
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
print()

'''The .__subclasses__() method search the subclasses which belongs to the superclass
and the .__name__ property show us the name of the class'''

for subclass in BaseException.__subclasses__():
    print(subclass.__name__)