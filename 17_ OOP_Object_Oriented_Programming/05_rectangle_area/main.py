""" create a Rectangle class whose __init__ method should take a self, width, and height parameter. 
The rectangle should have an area method that calculates and returns the area of the rectangle."""


"""Write a method that calculates the distance from the center of the rectangle to a given point. To implement that, you need to complete these steps:
1. Add an x and y parameter to __init__ and create their corresponding self.x and self.y attributes. These are to represent the coordinates of the center of the rectangle.
2. Add a distance_to_point method to Rectangle. The method should have an x and y parameter. These are to represent the coordinates of an imaginary point. The distance_to_point method should calculate the distance from the center of the rectangle to the point given the two x, y pairs.
3. To calculate the distance you can use the formula ((self.x - x)**2 + (self.y - y)**2) ** 0.5 which is the equivalent of √((x_2-x_1)²+(y_2-y_1)²)"""


"""Time
Let us calculate the time it takes the center of the rectangle to reach a given point. To implement this, you need to complete the steps below:
1. Add a time_to_point method to Rectangle. The method should have an x and y parameter. These are to represent the coordinates of the point.
2. The time_to_point method should also have a speed parameter.
3. The time_to_point method should calculate and return the time it takes the rectangle to go to a given point.
Note that you can call the existing distance_to_point method inside your time_to_point method."""


"""Add Perimeter
Add a perimeter method to Rectangle. The method should calculate and return the perimeter of a rectangle."""

class Rectangle:    
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height
    
    def distance_to_point(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2) ** 0.5
    
    def time_to_point(self, x, y, speed):
        distance = self.distance_to_point(x, y)
        return distance / speed if speed != 0 else float('inf')

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 5, 0, 0)
print(f"Area: {rect.area()}")  # Output: Area: 50
print(f"Distance to point (3, 4): {rect.distance_to_point(3, 4)}")  # Output: Distance to point (3, 4): 5.0
print(f"Time to point (3, 4) at speed 2: {rect.time_to_point(3, 4, 2)}")
print(f"Perimeter: {rect.perimeter()}")  