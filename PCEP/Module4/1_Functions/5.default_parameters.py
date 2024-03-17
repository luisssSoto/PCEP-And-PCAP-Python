"""Functions-predefined parameters"""
print("Welcome to default parameters")

def introduction(firstName, lastName='Snake'):#positional arguments must be at the start
    print('Hi I\'m', firstName, lastName, "nice to meet you")

introduction('Boa')
introduction('Cobra')
introduction('Python', 'Wildfred')

def introduction1(presentation='Hello', firstName='Juan', lastName='Garcia'):
    print(presentation, firstName, lastName, "nice to meet you")

introduction1()
introduction1(presentation='Hi')
introduction1(firstName='Valeria')
introduction1('What\'s up','Guy')
introduction1(presentation='Hey', lastName='Lopez')

#It'll be an SyntaxError 'cause the positional arguments must be before than the keyword arguments:
#introduction1(presentation='Que onda', 'luis', 'soto')
print("This is an error in traduction time")
