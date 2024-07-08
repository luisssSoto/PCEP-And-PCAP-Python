"""Open Mode 2"""

'''
Modo texto	Modo binario	Descripción
rt	        rb	            lectura
wt	        wb	            escritura
at	        ab	            adjuntar
r+t	        r+b	            lectura y actualización
w+t	        w+b	            escritura y actualización'''

'''
Finally, successfully opening the file will set the current 
position of the file (the virtual read/write head) before 
the first byte of the file if the mode is not a and after 
the last byte of the file if the mode is a.'''