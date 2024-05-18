"""Triangle"""

'''Point Class'''
from math import hypot

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX (self):
        return self.__x
    def getY (self):
        return self.__y
    def distanceFromXToY(self, x, y):
        return hypot(abs(self.__x - x), abs(self.__y - y))
    def distanceFromPoint(self, point):
        return self.distanceFromXToY(point.getX(), point.getY())
    
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distanceFromPoint(point2))
print(point2.distanceFromXToY(2, 0))

'''Triangle class'''

class Triangle():
    def __init__(self, pointA, pointB, pointC):
        self.__triangleList = [pointA, pointB, pointC]
    def perimeter(self):
        self.__sideA = self.__triangleList[0].distanceFromPoint(self.__triangleList[1])
        self.__sideB = self.__triangleList[1].distanceFromPoint(self.__triangleList[2]) 
        self.__sideC = self.__triangleList[2].distanceFromPoint(self.__triangleList[0])
        print(self.__sideA, self.__sideB, self.__sideC, sep='|')
        return ((self.__triangleList[0].distanceFromPoint(self.__triangleList[1])) + (self.__triangleList[1].distanceFromPoint(self.__triangleList[2])) + (self.__triangleList[2].distanceFromPoint(self.__triangleList[0])))
    
pointA = Point(0, 0)
pointB = Point(1, 1)
pointC = Point(2, 0) 

triangle1 = Triangle(pointA, pointB, pointC)  
print(triangle1.perimeter())
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
print()
    
'''Best Solution'''
import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]
    def perimeter(self):
        per = 0
        for i in range(3):
            per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3]) # It's clever 🧠
        return per

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    