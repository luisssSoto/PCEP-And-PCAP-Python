"""Open Mode of Streams"""
'''Open mode means the way you're going to use to opened file, there are three
common ways
1. Reading: the data recovered from the file can be save into a variable 
(a portion of the memory of the program)
2. Writting: the data inside a variable (a portion of the memory) can be pass to the file
3. Updating: it could use the 2 above approaches

You're going to get an UnsoportedError if you try to use any approach (Reading or
Writting) and if you try to write or read respectively any characters'''

'''Current Posistion of the file'''
'''When you read something from a stream, a virtual head moves over the stream according
 to the number of bytes transferred from the stream.
When you write something to the stream the same head moves along the stream recording 
the data from memory.'''