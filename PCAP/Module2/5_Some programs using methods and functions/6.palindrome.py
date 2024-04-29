"""Palindrome"""
def isAPalindrome(word):
    # create a return variable which store the result of the function
    isIt = False
    # delete the spaces between each element in word
    word = word.replace(' ', '')
    # know the length of the word and divide between 2
    halfWord = (len(word)) // 2
    # if there are spaces and also the string is empty
    if halfWord == 0 or word.isspace() == True:
        return isIt
    # divide in two parts
    beginPart = word[:halfWord]
    # if
    if len(word) % 2 != 0:
        endPart = word[halfWord+1:]
    else:
        endPart = word[halfWord:]
    # casting to upper because there is any difference between them
    beginPart.upper()
    endPart.capitalize()
    # sorting the endPart 
    endPartSort = ''
    for i in range(1,len(endPart)+1):
        endPartSort += endPart[-i]
    # is or not a palindrome...
    if beginPart == endPartSort:
        isIt = True
    return isIt

print(isAPalindrome('ff'))