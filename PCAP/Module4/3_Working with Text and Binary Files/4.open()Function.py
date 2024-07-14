"""open() function"""
'''open() function returns an iterable object and
1. only works with open mode 't'
2. the __next__ method returns the next line of the file
3. you don't need to close the stream close()'''

import os
try:
    characters_counter = lines_counter = 0
    for line in open(file="C:/pcep-and-pcap-python/pcap/module4/3_working with text files/text.txt", mode='rt', encoding='utf-8'):
        lines_counter +=1
        for character in line:
            characters_counter += 1
            print(character, end='')
    print(f'\nNumber of lines: {lines_counter}')
    print(f'Number of characters: {characters_counter}')
except IOError as e:
    print(f'Something happened: {os.strerror(e.errno)}')