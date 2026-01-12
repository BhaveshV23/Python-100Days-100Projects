from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = list(range(-250, 250, 40))

START_SPEED = 5
SPEED_INCREMENT = 2
BASE_SPAWN_CHANCE = 0.15

LEFT_BOUNDARY = -320
RIGHT_BOUNDARY = 320

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = START_SPEED
        self.spawn_chance = BASE_SPAWN_CHANCE

    def create_car(self):
        if random.random() < self.spawn_chance:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(RIGHT_BOUNDARY, random.choice(LANES))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars[:]:
            car.backward(self.speed)
            if car.xcor() < LEFT_BOUNDARY:
                car.hideturtle()
                self.all_cars.remove(car)

    def detect_collision(self, car, player):
        return (
            abs(car.xcor() - player.xcor()) < 20 and
            abs(car.ycor() - player.ycor()) < 20
        )

    def increase_difficulty(self):
        self.speed += SPEED_INCREMENT
        self.spawn_chance = min(0.4, self.spawn_chance + 0.02)

