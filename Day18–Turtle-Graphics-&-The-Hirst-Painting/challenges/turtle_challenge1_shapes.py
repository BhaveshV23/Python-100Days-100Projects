from turtle import Turtle,Screen
from random import choice
tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]

def draw_shapes(num_sides):
    for _ in range(num_sides):
        angle = 360/num_sides
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(choice(colours))
    draw_shapes(shape_side_n)

screen = Screen()
screen.exitonclick()
