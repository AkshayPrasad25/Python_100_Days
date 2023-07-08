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


# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(270):
    tim.color(rancolor())
    tim.forward(30)
    tim.setheading(choice(directions))