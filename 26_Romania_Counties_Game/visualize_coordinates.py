"""
Visualize all county coordinates as X marks on the map
"""
import os
import pandas as pd
from turtle import Turtle, Screen

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "Romania_location_map.gif")
csv_path = os.path.join(script_dir, "42_counties_romania.csv")

screen = Screen()
screen.title("Romania County Coordinates Visualizer")
screen.setup(width=800, height=800)
screen.addshape(image_path)

map_turtle = Turtle()
map_turtle.penup()
map_turtle.shape(image_path)
map_turtle.goto(0, 0)

# Read coordinates from CSV
counties = pd.read_csv(csv_path)

# Draw X at each coordinate
for _, row in counties.iterrows():
    x, y = int(row['x']), int(row['y'])
    marker = Turtle()
    marker.hideturtle()
    marker.penup()
    marker.goto(x, y)
    marker.pendown()
    marker.pensize(2)
    marker.color("red")
    # Draw X
    marker.setheading(45)
    marker.forward(10)
    marker.backward(20)
    marker.forward(10)
    marker.setheading(-45)
    marker.forward(10)
    marker.backward(20)
    marker.forward(10)
    marker.penup()
    # Optionally, show county name
    marker.goto(x, y-15)
    marker.write(row['county'], align="center", font=("Arial", 8, "normal"))

screen.mainloop()
