"""Final test section 3"""
'''1.'''
import os

try:
    for line in open(file="C:\\pcep-and-pcap-python\\pcap\\module4\\3_working with text and binary files\\london bridge.txt", mode="rt", encoding="utf-8"):
        for character in line:
            if character.capitalize() not in "AEIOU":
                print(character, end="")
except IOError as i:
    print("We couldn't complete your petition", os.strerror(i.errno))
            
'''2.'''
try:
    stream = open(file="c:\\pcep-and-pcap-python\\PCEP.PNG", mode="rb")
    image = bytearray(stream.read())
    print(f"image: {image}")
    stream.close()
except IOError as i:
    print('We couldn\t work with bits map inside image...', os.strerror(i.errno))