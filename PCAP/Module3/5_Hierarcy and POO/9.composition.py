"""Composition"""
''' It means that a class can implement its own behavior by taking whatever objects from
the others classes as a parameters, look the example below'''

import time
class Tracks:
    def change_direction(self, left, on):
        print("pistas: ", left, on)
class Wheels:
    def change_direction(self, left, on):
        print("ruedas: ", left, on)
class Vehicle:
    def __init__(self, controller):
        self.controller = controller
    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
    