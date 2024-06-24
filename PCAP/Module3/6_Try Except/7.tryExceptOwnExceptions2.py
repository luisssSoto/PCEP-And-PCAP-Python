"""Your own hierarcy of Exceptions"""
'''2. Exceptions that belongs to most Gene
ral Exceptions Classes'''

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, message, cheese):
        super().__init__(pizza, message)
        self.cheese = cheese

def make_pizza(name_pizza, amount_cheese):
    if name_pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(name_pizza, "this pizza is not in Luigi's Restaurant 🤔")
    if amount_cheese > 100:
        raise TooMuchCheeseError(name_pizza, 'this pizza has too much cheese 🤢', amount_cheese)
    print(f'Your pizza {name_pizza} is ready! 🍕')

for (pizza_name, cheese_total) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pizza_name, cheese_total)
    except TooMuchCheeseError as tmc:
        print(tmc, ':', tmc.cheese)
        print(tmc.args)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
        print(pe.args)

'''Note:
1. the order of the exception matter, if we put the most general
Exception (in this case "PizzaError") first, the secondary Exception
(in this case "TooMuchCheeseError") never will be handle
2. and if we delete the except PizzaError the program will stop'''
