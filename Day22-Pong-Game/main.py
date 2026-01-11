from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision (safe & accurate)
    if (
        330 < ball.xcor() < 350
        and ball.distance(r_paddle) < 50
    ):
        ball.bounce_x(r_paddle.ycor())

    if (
        -350 < ball.xcor() < -330
        and ball.distance(l_paddle) < 50
    ):
        ball.bounce_x(l_paddle.ycor())

    # Right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Win condition
    if scoreboard.l_score == 5:
        scoreboard.game_over("Left Player")
        game_is_on = False

    if scoreboard.r_score == 5:
        scoreboard.game_over("Right Player")
        game_is_on = False

screen.exitonclick()
