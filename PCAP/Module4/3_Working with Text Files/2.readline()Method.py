"""readline() method"""
'''It reads a entire line and returns it or if it is the end of the file
returns an empty string "" '''

from os import strerror
try:
    stream = open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_Working with Text Files/text.txt", mode='rt', encoding='utf-8')
    character_counter = line_counter = 0
    line = stream.readline()
    while line != '':
        line_counter += 1
        for character in line:
            print(character, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print(f'\nNumber of characters in text: {character_counter}')
    print(f'Number of lines in text: {line_counter}')
except IOError as ioerror:
    print(f'Number of error: {ioerror.errno}')
    print(f'Description of error: {strerror(ioerror.errno)}')
    print(IOError.__dict__)
    print(issubclass(IOError, OSError))