""" issubclass() function """
''' it is a function which takes two arguments; first one
is a the class which you want to know if it is a subclass
of the second argument which is the name of other class: '''

''' Example of two levels Hierarcy'''

class Vehicle:
	pass

class LandVehicle(Vehicle):
	pass

class TrackedVehicle(LandVehicle):
	pass

for class1 in [Vehicle, LandVehicle, TrackedVehicle]:
	for class2 in [Vehicle, LandVehicle, TrackedVehicle]:
		print(issubclass(class1, class2), end='\t')
	print()
