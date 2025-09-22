from turtle import Turtle, Screen
import pandas as pd

# Create a blank template for you to implement the US States Game

# TODO: Set up the screen with the US map background

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "25_US_States_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)  


# TODO: Load the states data from CSV

pd_data = pd.read_csv("25_US_States_Game/50_states.csv")
all_states = pd_data.state.to_list()


# TODO: Set up the game logic
guessed_states = []
state_writer = Turtle()
state_writer.hideturtle()
state_writer.penup()


# TODO: Create a loop for the game

while len(guessed_states) < 50:
    title_text = f"{len(guessed_states)}/50 States Correct"
    answer_state = screen.textinput(title=title_text, prompt="What's another state's name?").title()
    if answer_state is None or answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(missed_states, columns=["Missed States"]).to_csv("/25_US/states_to_learn.csv", index=False)
        break
    
    
    # Correct answer
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        
        
        # Get the coordinates of the guessed state and write it on the map
        state_data = pd_data[pd_data.state == answer_state]
        x_coord = int(state_data.x.iloc[0])
        y_coord = int(state_data.y.iloc[0])

        # Write state name at the coordinates / on the map
        state_writer.goto(x_coord, y_coord)
        state_writer.write(answer_state, align="center", font=("Arial", 8, "normal"))
        
        
    # if the player guessed all 50 states, the loop will end automatically and will send a message to congratulate them
    if len(guessed_states) == 50:
        screen.title("Congratulations! You've guessed all 50 states!")
        turtle.bye()

# TODO: Save missed states to a CSV file when user exits

turtle.mainloop()