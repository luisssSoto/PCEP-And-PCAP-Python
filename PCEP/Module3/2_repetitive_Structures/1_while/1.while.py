"""While loop"""
print("Welcome to While")
snake=input('Guess the kind of snake that I\'m thinking right now:')
secretSnake='cascabel'
while snake != secretSnake:
    snake=input('Sorry, but you didn\'t guess, try again:')
print('Congrats you did it!!!')