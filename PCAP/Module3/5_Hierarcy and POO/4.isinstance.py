""" isinstance() function """
''' It works with 2 arguments like issubclass() function but it works with
the object (firs parameter) and with the class (second parameter) and solve
the doubt if that object is an object of that class or other SuperClass,
because remember that an object if it is an instance of the ClassB and 
ClassB is a subclass of ClassA it means, that object is an instance as well
of ClassA '''

class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass

vehicle = Vehicle()
land_vehicle = LandVehicle()
tracked_vehicle = TrackedVehicle()

for object1 in [vehicle, land_vehicle, tracked_vehicle]:
    for class1 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(object1, class1), end = '\t')
    print()