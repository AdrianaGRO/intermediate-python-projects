from turtle import Turtle, Screen
import random
import colorgram
import turtle

# Extract colors from an image using colorgram
# colors = colorgram.extract("/Users/adricati/Personal Development/intermediate-python-projects/18_Graphical_User_Interface/damien_hirst.jpeg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

turtle = turtle.colormode(255)

color_list = [(198, 165, 116), (144, 79, 55), (221, 201, 138), 
(58, 93, 121), (167, 153, 48), (132, 34, 23), (137, 162, 181), (69, 40, 34), (51, 117, 87), (195, 93, 75), (146, 178, 150), (18, 93, 72), 
(231, 176, 165), (162, 143, 158), (35, 60, 75), (105, 73, 77), (180, 204, 177), (148, 19, 23), (83, 147, 127), (70, 37, 40), (18, 70, 60),
(27, 82, 88), (40, 66, 89), (190, 86, 89), (68, 64, 58), (223, 176, 180)]

t = Turtle()
screen = Screen()
screen.title("Hirst Painting")

t.penup()
t.hideturtle()
t.speed("fastest")
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



















screen.exitonclick()

