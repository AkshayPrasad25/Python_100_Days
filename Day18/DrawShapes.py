from turtle import Turtle, Screen
from random import choice

tim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]


def shapedraw(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


for shape in range(3, 11):
    tim.color(choice(colors))
    shapedraw(shape)
