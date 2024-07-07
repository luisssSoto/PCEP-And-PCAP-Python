"""Managing Files"""
'''In order to start working with the file you need to open the file with the 
open() function which analizes the arguments and creates the right object, 
afterwards, working with the file depending of the open mode
you used, and finally, close the connection with close() function wich finalizes
the connections between the object and the file and eliminates the object'''

'''Where that object comes'''
'''the streams could from RawIOBase, BufferedIOBase, TextIOBase, where their 
parent class is IOBase'''
'''1. TextIOBase: the text streams are any character, where the files is written 
or reading line by line or character by character
    2. BufferedIOBase: the binary streams are any sequence of bytes (images,
    videos, executable file and so on)'''