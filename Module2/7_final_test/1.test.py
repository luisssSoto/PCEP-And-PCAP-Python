
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