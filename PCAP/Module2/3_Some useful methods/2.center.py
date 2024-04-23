'''.center()'''
print('{' + 'python'.center(12) + '}')
print('[' + 'four'.center(2) + ']') # Nothing happend because the argument is not greater than the len of the string
print('[' + 'four'.center(4) + ']') # here neither
print('[' + 'four'.center(5) + ']')

# .center() with two parameters
print('[' + 'PCAP'.center(6,'¡') + ']')
