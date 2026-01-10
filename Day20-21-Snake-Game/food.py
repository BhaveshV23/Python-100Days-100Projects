from turtle import Turtle
import random

BOUNDARY = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-BOUNDARY, BOUNDARY)
        y = random.randint(-BOUNDARY, BOUNDARY)
        self.goto(x, y)

