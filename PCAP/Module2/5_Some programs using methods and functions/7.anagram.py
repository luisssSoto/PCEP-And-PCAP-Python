""" Anagram """
# ask the user for the first and second parameter and save the input in to variables
# userWordA = input('type your first word: '.capitalize())
# userWordB = input('type your second word: '.capitalize())
# create a functions with 2 parameters
def isAnAnagram(wordA, wordB):
# create a variable to save the final result
    veredict = 'They aren\'t anagrams'
# if 1 or 2 variable are in blank the result will be False
    if len(wordA) < 1 or len(wordB) < 1 or wordA.isspace() == True or wordB.isspace() == True:
        return veredict
# set both variables in lower or upper case
    wordA = wordA.lower()
    wordB = wordB.lower()
# delete all the blank spaces
    wordA = wordA.replace(' ', '')
    wordB = wordB.replace(' ', '')
# create a variable in order count the matches
    countMatches = 0
# loop for to pass through the 1 or 2 variable
    for character in wordA:
        if character in wordB:
            countMatches += 1
        else:
            return veredict
        if countMatches == len(wordB):
            veredict = "Anagrams"
    return veredict
userWordA='si   Len T'
userWordB='lis  T E N '
print(isAnAnagram(userWordA, userWordB))

''' Better solution'''
str_1 = input("Ingresa la primera cadena: ")
str_2 = input("Ingresa la segunda cadena: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagramas")
else:
	print("No son anagramas")
	