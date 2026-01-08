from turtle import Turtle, Screen
import random

# -------------------- CONSTANTS --------------------
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
START_X = -230
FINISH_X = 230

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [-70, -40, -10, 20, 50, 80]

# -------------------- SCREEN SETUP --------------------
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

if user_bet:
    user_bet = user_bet.lower()

# -------------------- CREATE TURTLES --------------------
all_turtles = []

for i in range(len(COLORS)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(COLORS[i])
    turtle.goto(x=START_X, y=Y_POSITIONS[i])
    all_turtles.append(turtle)

# -------------------- RACE LOGIC --------------------
is_race_on = user_bet in COLORS

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > FINISH_X:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"🎉 You won! The {winning_color} turtle is the winner!")
            else:
                print(f"❌ You lost! The {winning_color} turtle won the race.")

# -------------------- EXIT --------------------
screen.exitonclick()
