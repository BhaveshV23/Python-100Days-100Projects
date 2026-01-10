from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_SIZE = 600
WALL_LIMIT = 280
SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Collision with wall
    if (
        snake.head.xcor() > WALL_LIMIT
        or snake.head.xcor() < -WALL_LIMIT
        or snake.head.ycor() > WALL_LIMIT
        or snake.head.ycor() < -WALL_LIMIT
    ):
        scoreboard.game_over()
        game_is_on = False

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()

