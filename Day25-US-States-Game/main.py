import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = set()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None:
        continue

    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.add(answer_state)
        state_data = data[data.state == answer_state]
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(answer_state)

screen.exitonclick()
