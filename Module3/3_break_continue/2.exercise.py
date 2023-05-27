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