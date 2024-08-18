"""uname() and name()"""
import os, platform

#Unix
# print(os.uname())

#Windows
print(platform.uname())

obj = platform.uname()
print(f'SO: {obj.system}')
print(f'node: {obj.node}')
print(f'release: {obj.release}')
print(f'version: {obj.version}')
print(f'machine: {obj.machine}')
print()

# SO 
'''
posix: Unix, 
nt: Windows 
java: code written in Jython'''
print(os.name)