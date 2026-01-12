from turtle import Screen
import time

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
FRAME_DELAY = 0.1

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(FRAME_DELAY)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Collision detection (bounding-box based)
    for car in car_manager.all_cars:
        if car_manager.detect_collision(car, player):
            scoreboard.game_over()
            game_is_on = False
            break

    # Successful crossing
    if player.reached_finish():
        player.reset_position()
        car_manager.increase_difficulty()
        scoreboard.increase_level()

screen.exitonclick()

