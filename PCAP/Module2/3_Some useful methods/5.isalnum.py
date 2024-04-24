'''.isalnum() method'''
#Note: it doesn't matter if there is only a space or other value
# different to a word to alphabet or number the result will be a False:
print('onlyLetters'.isalnum())
print('012'.isalnum())
print('m1xTh3m'.isalnum())

print('one space'.isalnum())
print('anotherDifferentCharacter!'.isalnum())