from random import randint
from time import sleep
from design_game import draw_rectangle_turtle




class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        print(f"Checking if point ({self.x}, {self.y}) falls in rectangle....")
        sleep(1)  
        if rectangle.lower_left.x < self.x < rectangle.upper_right.x \
        and rectangle.lower_left.y < self.y < rectangle.upper_right.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def area(self):
        width = self.upper_right.x - self.lower_left.x
        height = self.upper_right.y - self.lower_left.y
        return width * height

    def perimeter(self):
        width = self.upper_right.x - self.lower_left.x
        height = self.upper_right.y - self.lower_left.y
        return 2 * (width + height)


rectangle = Rectangle(
    Point(randint(0, 10), randint(0, 10)),
    Point(randint(10, 19), randint(10, 19))
)

print(
    f"Rectangle coordinates: ({rectangle.lower_left.x}, {rectangle.lower_left.y}) "
    f"to ({rectangle.upper_right.x}, {rectangle.upper_right.y})"
)


user_point = Point(float(input("Please enter x-coordinate of your point: ")), float(input("Please enter y-coordinate of your point: ")))
is_inside = user_point.falls_in_rectangle(rectangle)


if is_inside:
    print(f"Great! The point ({user_point.x}, {user_point.y}) falls within the rectangle.")
else:
    print(f"Unfortunately, the point ({user_point.x}, {user_point.y}) is outside the rectangle.")


user_area = input("Can you guess the area of the rectangle? ")
if user_area.isdigit():
    if int(user_area) == rectangle.area():
        print("Congratulations! You guessed the area correctly.")
    else:
        print("Sorry, that's not correct.")
        print(f"It looks like your calculation might need a quick review! You were off by {abs(int(user_area) - rectangle.area())}.")
        print(f"The correct area of the rectangle is {rectangle.area()} units.")


user_perimeter = input("Can you guess the perimeter of the rectangle? ")

if user_perimeter.isdigit():
    if int(user_perimeter) == rectangle.perimeter():
        print("Congratulations! You guessed the perimeter correctly.")
    else:
        print("Sorry, that's not correct.")
        print(f"It looks like your calculation might need a quick review! You were off by {abs(int(user_perimeter) - rectangle.perimeter())}.")
        print(f"The correct perimeter of the rectangle is {rectangle.perimeter()} units.")

draw_rectangle_turtle(rectangle, user_point, is_inside)