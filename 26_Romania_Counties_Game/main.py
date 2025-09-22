# Romania Counties Game Project
# TODO: Create a game where players guess all 42 Romanian counties (județe)
# Use turtle graphics to display a map of Romania and mark correct guesses
# Save missed counties to a CSV file when the player exits

from turtle import Turtle, Screen
import pandas as pd
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# TODO: Set up the screen with the Romania map background
# Hint1: You'll need a romania_map.gif image file
# Hint2: Use screen.addshape() and turtle.shape() methods

screen = Screen()
screen.title("Romania Counties Game")
screen.setup(width=800, height=800)  # Set screen size to match your adjusted image size
image_path = os.path.join(script_dir, "Romania_location_map.gif")  # Use absolute path
screen.addshape(image_path)

t = Turtle()
t.penup()
t.shape(image_path)

# Create a writer turtle for the county names
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("blue")


# Write instructions on the canvas
instruction_writer = Turtle()
instruction_writer.hideturtle()
instruction_writer.penup()
instruction_writer.goto(0, 370)
instruction_writer.color("darkgreen")
instruction_writer.write(
    "Instructions: Guess all 42 counties of Romania or write 'Exit' to quit",
    align="center", font=("Arial", 14, "bold")
)


# TODO: Load the counties data from CSV
# Hint1: Create a CSV file with columns: county, x, y (coordinates)
# Hint2: Use pandas.read_csv() to load the data
# Hint3: Convert county names to a list with .to_list() method

csv_path = os.path.join(script_dir, "42_counties_romania.csv")  # Use absolute path
data = pd.read_csv(csv_path)
all_counties = data["county"].to_list() if "county" in data.columns else []




# TODO: Set up the game components
# Hint1: Create a list to track guessed counties
# Hint2: Create a turtle object to write county names on screen
# Hint3: Use hideturtle() and penup() for the writing turtle

guessed_counties = []
# Writer is already defined in the setup section



# TODO: Create the main game loop
# Hint1: Loop while guessed counties < 42
# Hint2: Use screen.textinput() to get user input
# Hint3: Handle exit condition (None or "Exit")
# Hint4: Check if guess is correct and not already guessed

while len(guessed_counties) < 42:
    title_text = f"{len(guessed_counties)}/42 Counties Correct"
    answer_county = screen.textinput(title=title_text, prompt="What's another county's name?").title()
    if answer_county is None or answer_county == "Exit":
        missed_counties = [county for county in all_counties if county not in guessed_counties]
        t.bye()
        break
    
    answer_county = answer_county.title()
    
            
# TODO: Handle correct guesses
# Hint1: Add correct guess to guessed_counties list
# Hint2: Find the county data using pandas filtering
# Hint3: Get x and y coordinates from the filtered data
# Hint4: Use turtle.goto() and turtle.write() to display county name

    if answer_county in all_counties and answer_county not in guessed_counties:
            guessed_counties.append(answer_county)
            county_data = data[data.county == answer_county]
            x_coord = int(county_data.x.iloc[0])
            y_coord = int(county_data.y.iloc[0])
            writer.goto(x_coord, y_coord)
            writer.write(answer_county, align="center", font=("Arial", 8, "normal"))

# TODO: Handle game completion
# Hint1: Check if all 42 counties are guessed
# Hint2: Display congratulations message
# Hint3: End the game appropriately
    if len(guessed_counties) == 42:
        screen.title("Congratulations! You've guessed all 42 counties!")
        t.bye()

# TODO: Save missed counties to CSV when exiting
# Hint1: Create list of missed counties using list comprehension
# Hint2: Use pd.DataFrame() to create dataframe from missed counties
# Hint3: Use .to_csv() to save the file

if 'missed_counties' in locals():
    output_path = os.path.join(script_dir, "counties_to_learn.csv")  # Use absolute path
    pd.DataFrame(missed_counties, columns=["Missed Counties"]).to_csv(output_path, index=False)




