from turtle import Turtle
import random

INITIAL_SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_position()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self, paddle_y):
        self.x_move *= -1
        # Change angle depending on where it hits the paddle
        self.y_move = (self.ycor() - paddle_y) / 10
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = INITIAL_SPEED
        self.x_move = random.choice([-10, 10])
        self.y_move = random.choice([-8, 8])
