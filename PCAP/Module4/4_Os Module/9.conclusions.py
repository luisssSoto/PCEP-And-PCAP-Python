#Conclusions

'''1. Uname'''
from platform import uname
print(uname())
obj = uname()
print(f'System Operative: {obj.system}')
print(f'Node: {obj.node}')
print(f'Release: {obj.release}')
print(f'Version: {obj.version}')
print(f'Machine: {obj.machine}')
print(f'Proccesor: {obj.processor}')
print(f'Fields: {obj._fields}' + '\n')

'''2. Name'''
from os import name
match name:
    case 'nt':
        print('It is Windows')
    case 'posix':
        print('It is Linux')
    case 'java':
        print('It is Jython')
    case _:
        print('Unknown Operative System')
print()

'''3. mkdir'''
from os import mkdir
mkdir('./relativePath')

'''4. makedirs'''
from os import makedirs
makedirs('./anotherPath./anotherDirectory')

'''5. listdir'''
from os import listdir
print(listdir(path='./anotherPath'))
print()

'''6. chdir'''
from os import chdir
chdir('./anotherPath')
print(listdir())
print()

'''7. getcwd'''
from os import getcwd
print(getcwd(), '\n')

'''8. rmdir'''
from os import rmdir
chdir('../')
print(getcwd())
if 'relativePath' in listdir():
    print(f'this directory is in the current directory')
    rmdir('./relativePath')
    print(f'the file was deleted successfully')
else:
    print('The directory doesn\'t exist')
print()

'''9. removedirs'''
from os import removedirs
if 'anotherPath' in listdir():
    print('this directory is in the current directory')
    removedirs('./anotherPath/anotherDirectory')
    print('The directories were deleted successfully')
else:
    print('The directory doesn\'t exist')
print()

'''10. system'''
from os import system
system('ping 8.8.8.8')