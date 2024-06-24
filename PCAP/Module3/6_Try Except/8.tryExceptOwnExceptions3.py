"""Your own hierarcy of Exceptions"""
'''Now we can improve the last code, if we decide to build the
classes with their parameters with values'''
class PizzaError(Exception):
    def __init__(self, pizza = 'unknown', message = '', another='another message'):
        Exception.__init__(self, message, another)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza = 'unknown', message = '', cheese = '>0'):
        super().__init__(pizza, message)
        self.cheese = cheese

def make_pizza(name_pizza, amount_cheese):
    if name_pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if amount_cheese > 100:
        raise TooMuchCheeseError
    print(f'Your pizza: {name_pizza} is ready!')

for (name_of_pizza, total_cheese ) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(name_of_pizza, total_cheese)
    except TooMuchCheeseError as tmc:
        print(tmc, tmc.cheese)
        print(tmc.args)
    except PizzaError as pe:
        print(pe, pe.pizza)
        print(pe.args[0])

'''Note: the attribute args will print a tuple with the arguments
that are in the constructor of their superclass and their own
constructor '''