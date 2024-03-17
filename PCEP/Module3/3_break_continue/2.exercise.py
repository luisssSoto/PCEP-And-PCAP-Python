"""Excercise Vowel's Monster"""

word = input("Introduce any word you want:")
word=word.upper()
newWord=""
for letter in word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        newWord += letter
print(newWord)

'''You can do the last with a brand new code like this'''
word=input('Introduce whatever word you want: ')
word=word.upper()
newWord=''
for letter in word:
    match letter:
        case "A":
            continue
        case "E":
            continue
        case "I":
            continue
        case "O":
            continue
        case "U":
            continue
        case _:
            newWord+=letter
print(f'The word {word} without vowels is {newWord}')