"""Conclusions"""
'''1. 
Any file needs to be open first before work with, in order to work with we need to create
a stream object wich will be associated with the file wich is in any phisic medio (device)
There are 3 open mode ways to open the file:
a) reading
b) writing
c) updating
''' 

'''2. 
There are two classes in order to work with files:
a) BufferedIOBase: can deal with any type of file
b) TextIOBase: only can deal with text type file
'''

'''3.
Sintaxis to open a file:
stream = open(file=name_file, mode=open_mode, encoding=text_encoding)
'''

'''4. 
There are 3 streams which don't need to be opened and closes, because they're already
be open by the time the program start:
a) stdin (standartd input)
b) stdout (standard output)
c) sterr (standard error)
'''

'''5.
You can handle the errors with errno property and errno module to know what type of error
is, and also with function strerror() and its module os, this method receives a number
error and returns the a description error'''