"""Portability"""
'''In the text files in SO Unix/Linux at the end of the line there is a "LF" (\n)
but in other SO like Windows the end of the line there are "CR" or "LF" they can
be modified like "\r\n"'''
'''So if you write a program wich manage a file written in Windows and you execute it 
in a Linux environment it won't work and viceverse, so that there is not Portability,
or our program won't be portable, so that, the problem was solved just like this:'''

'''1. by the time the stream is open and there is an instruction or not to open 
the file in text mode, the file will be open in text mode
    2. When you write or read any file from Linux nothing happens, but in Windows 
    occurs a "Translate of Characters of New Line" so if you read the file
    translates every "\r\n" characters of "\n" and if you write any "\n", is 
    replaced by "\r\n"
    3. All this proccess is transparent'''