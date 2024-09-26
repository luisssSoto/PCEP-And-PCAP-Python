"""from turtle import Turtle, Screen

gary = Turtle()
screen = Screen()

def move_forward():
    gary.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()"""

#Challenge Etch-A-Sketch
from turtle import Turtle, Screen

def move_forwards():
    gary.forward(10)

def move_backwards():
    gary.backward(10)

def counter_clockwise():
    gary.left(30)

def clockwise():
    gary.right(30)

def clear_drawing():
    gary.clear()
    gary.penup()
    gary.home()
    gary.pendown()

gary = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
