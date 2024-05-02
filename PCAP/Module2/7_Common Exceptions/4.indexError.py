""" Index Error """
'''Tree:
BaseException <- Exception <- LookupError <- IndexError'''

repeatIt = True
count = 0
while repeatIt:
    try:
        face = [['👁️'], ['👃🏻'], ['👁️']]
        print(face[count][0])
        count += 1
    except IndexError:
        print('We are going to get out the loop')
        repeatIt = False