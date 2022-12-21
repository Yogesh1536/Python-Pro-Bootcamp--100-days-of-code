import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(800, 800)
image = 'blank_india_map.gif'
screen.addshape(image)
turtle.shape(image)

guessed_states = []


data = pd.read_csv('28_states.csv')
all_state = data.state.to_list()


while len(guessed_states) <= 28:

    answer = screen.textinput(title=f"{len(guessed_states)}/28 Guess the State", prompt="Enter a State name.").title()

    if answer == 'Exit':
        missing_state = [state for state in all_state if state not in guessed_states]
        mis_state_df = pd.DataFrame(missing_state)
        mis_state_df.to_csv('remaining_states.csv')
        break
    if answer in all_state:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        current_state = data[data.state == answer]
        t.setpos(int(current_state.x), int(current_state.y))
        cur_state = current_state.state.item()
        t.write(cur_state)
        guessed_states.append(cur_state)

