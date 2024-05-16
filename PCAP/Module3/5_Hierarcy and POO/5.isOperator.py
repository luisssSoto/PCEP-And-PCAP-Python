""" is Operator """
''' It checks if one object is the same than the second one
Note: the objects pass its memory idetifier during the assignation to any
variable NOT the object, take a look of the next to discover it yourself: '''

class Sample:
    def __init__(self, var):
        self.var = var

object1 = Sample(0)
object2 = Sample(2)
object3 = object1
object3.var += 1
print(object1 is object2)
print(object2 is object3)
print(object3 is object1)
print(object1.var, object2.var, object3.var)

'''Compare the above result with the next below: '''
string1 = 'Maria had'
string2 = 'Maria had a little sheep'
string1 += ' a little sheep'
print(string1 == string2, string1 is string2, sep='|')