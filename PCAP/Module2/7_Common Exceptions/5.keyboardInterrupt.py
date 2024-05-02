""" Keyboard Interrupt """
'''Tree:
BaseException <- KeyboardInterrupt'''

from time import sleep
count = 0
condition = True
while condition:
    try:
        print(count)
        sleep(1)
        count += 1
    except KeyboardInterrupt as e:
        print('Keyboard Interrupt: ', e)
        # Note: you need to add a end condition otherwise the code will continue running
        condition = False