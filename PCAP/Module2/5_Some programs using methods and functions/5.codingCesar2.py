"""Coding Cesar 2.0"""
def codingCesar2(code, jumps):
    # create a str variable to return
    codeCesar = ''
    # iterate for the code
    for character in code:
    # cast to upper each character
        if character.isalpha():
            pointCharacter = ord(character) + jumps
        # conditional if ord(character) > ord('Z')
            if pointCharacter > ord('Z') and character.isupper():
                toZ = ord('Z') - ord(character)
                correctSteps = jumps - toZ
                codeCesar += chr(correctSteps + ord('A')-1)
            elif pointCharacter > ord('z') and character.islower():
                to_z = ord('z') - ord(character)
                correct_steps = jumps - to_z
                codeCesar += chr(correct_steps + ord('a')-1)
            else:
                codeCesar += chr(pointCharacter)
        else:
            codeCesar += character
    return codeCesar

print(codingCesar2('The die is cast', 25))



