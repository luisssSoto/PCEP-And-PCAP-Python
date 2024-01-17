'''Be careful with details: '''
print('hi' + 'my name is','Alejandro', sep=' ')
print('hi', 'my name is', 'Alejandro', sep=' ')
print('hi', 'my name is', 'Alejandro', sep=' ', end='||||')
print('hi', 'my name is', 'Alejandro', end='||||', sep=' ')

print('first positional arguments, and then keywords arguments: ')
#print(sep=' ','hi', 'my name is', 'Alejandro', end='||||')

'''Type pow'''
var_pow=20.12*10**8
shorter=20.12E8
print(var_pow, shorter, sep='°|°')


'''% behavior'''
shorter=2
greater=5
module=greater%shorter
print(f'case 1: {module}')
module=shorter%greater
print('case 2:', module)

'''At the moment to initializing a couple of variable of the same type
the way is below is easier'''

x=y=z=1
print(x,y,z,sep='|')
print(id(x), id(y), id(z), sep='|')

'''But if you want to unpack a kind of array or the same number of values to the same
number of variables you can use this one: '''
x, y, z = 9, 10, 11
print(x,y,z,sep='|')
