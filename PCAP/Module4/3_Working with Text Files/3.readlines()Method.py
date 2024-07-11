"""readlines() Method"""
'''without any argument tries to read all the content of the file and returns
a list of strings which each string element is a line of the file'''

stream = open(file="C:\\PCEP-And-PCAP-Python\\PCAP\\module4\\3_working with Text Files\\text.txt", mode="rt", encoding='utf-8')
print(stream.readlines())
stream.close()
print()

'''with argument tries to read only the amount of bytes that you pass as argument'''
'''if the head virtual is at the end of the file, the method returns an empty list'''

stream = open(file="C:\\PCEP-And-PCAP-Python\\PCAP\\module4\\3_working with Text Files\\text.txt", mode="rt", encoding='utf-8')
print(stream.readlines(1))
stream.close()
print()


from os import strerror

try:
    characters_counter = lines_counter = 0
    stream = open(file="C:\\PCEP-And-PCAP-Python\\PCAP\\module4\\3_working with Text Files\\text.txt", mode="rt", encoding='utf-8')
    lines = stream.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lines_counter += 1
            for character in line:
                print(character, end="")
                characters_counter += 1
        lines = stream.readlines(10)
    stream.close()
    print(f'The number of lines are: {lines_counter}')
    print(f'The number of characters are: {characters_counter}')
except IOError as ioError:
    print(f'Number of Error: {ioError.errno}')
    print(f'Description of error: {strerror[ioError.errno]}')
