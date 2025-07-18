'''platform module'''

'''platform is used to know what is exactly below of python code'''
from platform import platform

#aliased is used to know if there is an alias to that platform
#terse is used to show a shorter name
print(platform(aliased=1, terse=1))
print(platform(0, 0))
print(platform())

'''machine() shows the processor'''
from platform import machine

print(machine())

'''processor() gives us the real name of the processor'''
import platform 

print(platform.processor())

'''system() shows us the SO'''
import platform

print(platform.system())

'''version() gives the version of SO'''

from platform import version

print(version())

'''python_implementation() and python_version_tuple() show us information about
the python details; first one gives us the implementation of python, for instance
CPyhton, and the last one, shows us the version of python'''
from platform import python_implementation, python_version_tuple

print(python_implementation())

for element in python_version_tuple():
    print(element, end='\t')
