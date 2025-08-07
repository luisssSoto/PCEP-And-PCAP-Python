"""Section Test"""

# 1. 
from turtle import Turtle

# 2. 
import turtle
t = turtle.Turtle()
print(t)

# 3. 
print(dir(turtle))

# 4.
'''file.pyc contains a Python's compile file'''

# 5. 
'''The first time a module is imported is executed implicitly'''

# 6. 
print(__name__)

# 7. 
'''from package_name.module_name import name_entity'''

# 8.
from math import e, pow
print(e, pow(2,4), sep="|")
print(int(e) == pow(2, 4))

# 9. 
from random import randint
print(randint(1, 2))

# 10.
from platform import system, version, machine, python_version_tuple
print(system())
print(version())
print(machine())
print(python_version_tuple())

# 11.
'''__pycache__ contains pyc file'''

# 12. 
'''#! says to Unix system how to execute the file'''

# 13. 
'''pip show <package_name> shows us all the dependencies related
to tha package'''

# 14. 
'''pip list shows us all the packages we already have installed'''

# 15. 
'''pip search is not available anymore'''

# 16.
'''pip install --user <packageName>
pip install <packageName>==<packageVersion>'''

# 17.
'''pip install -U --user <packageName>'''

# 18.
'''pip uninstall <packageName>'''