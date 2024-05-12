""" Introduction to Hierarcy """
''' Hierarcy in POO...
It is the behavior that pass attributes and methods from a SuperClass to its
Subclass, so that, it's very useful, because you won't work since the 
begining, otherwise, you already have several elements to use in order to 
update or adding new features to the futures objects that you could need
after'''

''' Hierarcy of Classes has a relation transitive, for instance: 
Vehicle is Superclass of LandVehicle and TrackedVehicle, LandVehicle is a
Subclass of Vehicle and a Superclass of TrackedVehicle, and TrackeVehicle
is a Subclas of both (Vehicle and LandVehicle) '''

class Vehicle:
    pass
class LandVehicle:
    pass
class TrackedVehicle:
    pass