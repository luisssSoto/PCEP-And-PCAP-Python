"""close() function """
'''The last operation you should do is close() which means to close the connection
between the object stream and the file'''

'''Most developers believe that the close() function always succeeds and therefore 
there is no need to check whether it has performed its task correctly.

This belief is only partially justified. If the stream was opened for writing and 
then a series of write operations were performed, it may happen that the data sent 
to the stream has not yet been transferred to the physical device (due to caching 
or buffering mechanisms).

Since closing the stream forces the buffers to be flushed, it is possible that 
those flushes will fail and therefore close() will fail as well.'''