from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280
TOP_BOUNDARY = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move_up(self):
        if self.ycor() < TOP_BOUNDARY:
            self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(START_POSITION)

    def reached_finish(self):
        return self.ycor() >= FINISH_LINE_Y

