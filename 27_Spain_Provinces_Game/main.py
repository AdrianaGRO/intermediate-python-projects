from turtle import Screen, Turtle
import pandas as pd
import os


# Set up the screen with the Spain map
screen = Screen()
screen.title("Spain ProvincesGame")
screen.setup(width=800, height=800)
image_path = os.path.join (os.path.dirname(os.path.abspath(__file__)), "pan.gif")
screen.addshape(image_path)

t = Turtle()
t.penup()
t.shape(image_path)

#Create a writer turtle for the province names
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("red")


# Load the provinces data from CSV
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "provinces_correct.csv")
data = pd.read_csv(csv_path)
all_provinces = [p.strip().casefold() for p in data["province"].to_list()] if "province" in data.columns else []
total_provinces = len(all_provinces)
print(f"Loaded provinces ({total_provinces}):", all_provinces)

# Write instructions on the canvas
instruction_writer = Turtle()
instruction_writer.hideturtle()
instruction_writer.penup()
instruction_writer.goto(0, 415)
instruction_writer.color("darkblue")
instruction_writer.write(f"Do you know all {total_provinces} provinces of Spain? Guess them all or write 'Exit' to quit, DO NOT USE ACCENTS!", align="center", font=("Arial", 14, "bold"))

guessed_provinces = []

while len(guessed_provinces) < total_provinces:
    title_text = f"{len(guessed_provinces)}/{total_provinces} Provinces Correct"
    answer_province = screen.textinput(title=title_text, prompt="What's another province's name?")
    if answer_province is None or answer_province.casefold() == "exit":
        missed_provinces = [province for province in all_provinces if province not in guessed_provinces]
        screen.bye()
        break
    answer_province = answer_province.strip().casefold()

    # Handle correct guesses
    if answer_province in all_provinces and answer_province not in guessed_provinces:
        guessed_provinces.append(answer_province)
        # Find the original province name for display and coordinates
        idx = all_provinces.index(answer_province)
        province_name = data["province"].iloc[idx]
        province_data = data[data["province"] == province_name]
        x_coord = int(province_data.x.iloc[0])
        y_coord = int(province_data.y.iloc[0])
        writer.goto(x_coord, y_coord)
        writer.write(province_name, align="center", font=("Arial", 10, "bold"))

    # Handle the win condition
    if len(guessed_provinces) == total_provinces:
        instruction_writer.clear()
        instruction_writer.goto(0, 400)
        instruction_writer.color("darkgreen")
        instruction_writer.write(f"Congratulations! You guessed all {total_provinces} provinces of Spain!", align="center", font=("Arial", 24, "bold"))
        break

# Save missed provinces to a CSV file
try:
    if missed_provinces:
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "provinces_to_learn.csv")
        pd.DataFrame(missed_provinces, columns=["Missed Provinces"]).to_csv(output_path, index=False)
except NameError:
    pass

screen.mainloop()