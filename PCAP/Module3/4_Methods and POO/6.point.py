"Points on a Plane "
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
        self.__pointA = self.__x - x
        self.__pointB = self.__y - y
        return math.hypot((self.__pointA), (self.__pointB))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())
        

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
print()
pointA = Point(5,2)
pointB = Point(-2,-4)
pointC = Point(5,2)
pointD = Point(-3,-1)
print(pointA.distance_from_point(pointB))
print()


# Expected Output    
# 1.4142135623730951
# 1.4142135623730951

''' Best Solution '''
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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
print()

pointA = Point(5,2)
pointB = Point(-2,-4)
print(pointA.distance_from_point(pointB))