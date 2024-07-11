"""stderr stream"""
'''Remember; you don't need to open the file because this is already open'''

import sys

sys.stderr.write('Error message')
print()
sys.stdout.write('Standard Output')

input_user = sys.stdin.read(5)

sys.stdout.write(input_user)
for character in input_user:
    print(character)