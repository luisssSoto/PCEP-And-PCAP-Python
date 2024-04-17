"""Characters and how the computers save them"""

'''American Standard Code for Information Interchange (ASCII) is one of the most well-known
standard to save one character like a number, each character has its own number 
("point of code") which is associated with, ASCII has 256 characters the first 128 are 
latin characters, and each character needs 8 bits in memory to be saved them'''

'''The Internationalization (I18N) is a standard that all the programs needs to follow,
if they want to all the people with different language can understand their program'''

'''Suddenly, ASCII was not enough to cover all the other languages of the world, so 
was implemented another idea, each character has its own "point of code" but according
to the "page of code", the game plan was to use the first 128 characters to each different 
language to create diferents pages of code and each of these pages of code were called 
by the ISO'''

'''After that came "Unicode" which save more than one million of characters in order to
meet the demands of I18N, the first 128 characters are the same like ASCII and the first
256 characters are the same like tha page of code ISO/IEC 8859-1, but this is only a
standard more, so it was neccesary know how to save all those characters in all the 
technological devices... '''

''' Universal Character Set (UCS-4) is a standard to save each character in the computers
with 32 bits, one more thing is that the files that follow this standard, at the beginning
of the file can start, with a Byte-Mark-Order (BOM) that says the computer which standard
is following the file (UCS-4 or UTF-8)'''

''' Unicode Transformation Format (UTF-8) is a standard which does the same of UCS-4, 
sometimes it can has a BOM too but nor always, the main difference is that this one is 
not careleness whit the space, because it saves each character depending of its type:
latin characters and standard ASCII: 8 bits
non latin characters: 16 bits
CJK (China-Japan-Korea) ideographs occupy 24 bits
'''