"""Method's List"""
print("Welcome to the method's list")

list1=[1,2,3,4,5]

'''.append()'''
list1.append(6)
print(list1)

'''.insert()'''
list1.insert(0,'zero')
print(list1)

""".sort()"""
vowels=['i','u','a','o','e']
print(vowels)
vowels.sort()
print(vowels)

'''Note: you can't assign a sort() method to any variable 'cause you'll get a None'''
sortVowels=[]
sortVowels=vowels.sort()
print(sortVowels)

""".pop()"""
popIt=vowels.pop()
print(vowels)
print(popIt)
