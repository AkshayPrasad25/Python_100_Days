import turtle
from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
turtle.colormode(255)


def rancolor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor

def draw(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tim.speed("fastest")
        tim.color(rancolor())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw(5)

screen = Screen()
screen.exitonclick()