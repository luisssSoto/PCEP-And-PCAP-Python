"""read() method"""
'''What does it
1. with one argument can read 1 character
2. without any argument reads all the file
3. at the end of the file, the head virtual arrives at the end of the file
and returns a '' empty string '''

'''1. reading a file with 1 argument'''

from os import strerror

try:
    count = 0
    stream = open(file='C:/PCEP-And-PCAP-Python/PCAP/Module4/3_Working with Text Files/text.txt', mode='rt', encoding='utf-8') #encoding depends of the SO for example if we don't incluide it the ñ character is not add it
    character = stream.read(1)
    while character != '':
        print(character, end='')
        count += 1
        character = stream.read(1)
    print('The amount of characters is:', count)
    stream.close()
except IOError as e:
    print('It was an error', strerror(e.errno))
print()

'''2. reading without any argument'''
try:
    stream = open(file='C:/PCEP-And-PCAP-Python/PCAP/Module4/3_Working with Text Files/text.txt', mode='rt', encoding='utf-8')
    text = stream.read()
    count = 0
    for character in text:
        print(character, end='')
        count += 1
    print('The total of characters is:', count)
except IOError as e:
    print('Something was wrong')
    print(f'number of error: {e.errno} \nerror: {strerror(e.errno)}')
