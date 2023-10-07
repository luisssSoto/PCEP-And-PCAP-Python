'''There is a default except that you can use but this one
needs to be at the end of the all exceptions'''


try:
    user_number=int(input('Type a number: '))
    result=1/user_number
    print('The reciprocal of number:', user_number,'is:', result)
except ValueError:
    print('Your data is invalid, you need to put only numbers')
except ZeroDivisionError:
    print('This is impossible, division by zero won\'t be possible')
except:
    print('I am a default except, so if this runs is because\
        the last exceptions couldn\'t deal with this particular issue')