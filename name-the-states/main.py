import turtle as t
import pandas

screen = t.Screen()
screen.title("name the states")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim = t.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(answer_state)
    elif answer_state == "Give Up":
        for state in all_states:
            if state not in guessed_states:
                tim = t.Turtle()
                tim.hideturtle()
                tim.penup()
                state_data = data[data.state == state]
                tim.goto(state_data.x.item(), state_data.y.item())
                tim.write(state)
                break
    elif answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states] # list comprehension
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

screen.exitonclick()
