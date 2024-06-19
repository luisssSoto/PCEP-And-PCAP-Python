"""How to get a right hierarcy of Classes"""

'''Polymorphism'''
class One:
    def do_it(self):
        print('do it from one')
    def doanything(self):
        self.do_it()

class Two(One):
    # virtual method
    def do_it(self):
        print('do it from two')
        
one = One()
two = Two()
one.doanything()
two.doanything()

''' Polymorphism means that a subclass can change the behavior of its superclass, the
example above show us how although the method "doanything" was launched inside the
"One" class the method "do_it" from the "Two" class will be executed, so the overwriten
method of any subclass which change the behavior of its superclass is called "virtual"'''

'''Example how to implement the polymorphism'''
import time

class Vehicle:
    # Abstract method
    def change_direction(left, on):
        pass
    def turn(self,left):
        self.change_direction(left, True)
        time.sleep(1)
        self.change_direction(left, False)

class TrackedVehicle(Vehicle):
    def control_track(self, left, stop):
        print('pistas:', left, stop)

    def change_direction(self, left, on):
        self.control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(self, left, on):
        print('ruedas:', left, on)

    def change_direction(self, left, on):
        self.turn_front_wheels(left, on)
        
tank = TrackedVehicle()
tank.turn(True)

mustang = WheeledVehicle()
mustang.turn(False)

'''Note: The "change_direction()" method declared in Vehicle is called an Abstract method
which later will get costumized by some of its subclasses, one important advantage is 
that the turn() method could change its behavior, then, all its subclasses will change its
behavior as well'''