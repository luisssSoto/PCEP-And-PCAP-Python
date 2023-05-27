"""continue and break"""
print("Welcome to continue and break")
print('"break"')
for i in range(5):
    if i == 2:
        break;
    print(i)

print('\n"continue"')
for j in range(5):
    if j == 2:
        continue
    print(j)

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









