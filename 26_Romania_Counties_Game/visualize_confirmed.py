"""
Visualize only confirmed county coordinates as X marks on the map
"""
import os
import pandas as pd
from turtle import Turtle, Screen

# List of confirmed coordinates (county, x, y)
confirmed_coords = [
    ("Bucuresti", 88, -167),
    ("Ilfov", 89, -138),
    ("Ialomita", 169, -141),
    ("Calarasi", 160, -180),
    ("Constanta", 267, -188),
    ("Tulcea", 290, -98),
    ("Braila", 222, -97),
    ("Buzau", 132, -82),
    ("Prahova", 95, -96),
    ("Giurgiu", 73, -198),
    ("Dambovita", 41, -121),
    ("Teleorman", 20, -183),
    ("Bistrita-Nasaud", -44, 181),
    ("Suceava", 44, 232),
    ("Neamt", 81, 170),
    ("Iasi", 170, 200),
    ("Botosani", 153, 260),
    ("Satu Mare", -176, 192),
    ("Maramures", -120, 189),
    ("Salaj", -149, 137),
    ("Bihor", -212, 123),
    ("Arad", -261, 48),
    ("Dolj", -121, -218)
]
print(f"Total confirmed counties: {len(confirmed_coords)}")
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "Romania_location_map.gif")

screen = Screen()
screen.title("Romania Confirmed County Coordinates Visualizer")
screen.setup(width=800, height=800)
screen.addshape(image_path)

map_turtle = Turtle()
map_turtle.penup()
map_turtle.shape(image_path)
map_turtle.goto(0, 0)

# Draw X at each confirmed coordinate
for county, x, y in confirmed_coords:
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
    # Show county name
    marker.goto(x, y-15)
    marker.write(county, align="center", font=("Arial", 8, "normal"))

screen.mainloop()
