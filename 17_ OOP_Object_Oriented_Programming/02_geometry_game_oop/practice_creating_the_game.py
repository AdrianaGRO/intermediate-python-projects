class Point:

    def __init__(self, x, y):
        print(f"Creating a Point object for ({x}, {y}).")

        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        print(f"Checking if point ({self.x}, {self.y}) falls in rectangle.")
        if rectangle.lower_left[0] < self.x < rectangle.upper_right[0] \
        and rectangle.lower_left[1] < self.y < rectangle.upper_right[1]:
            return True
        else:
            return False

    def distance(self, other):
        print(f"Calculating the distance from point ({self.x}, {self.y}) to point ({other.x}, {other.y}).")
        the_distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        print(f"The distance between the points is {the_distance}.")
        return the_distance
    
class Rectangle:

    def __init__(self, lower_left, upper_right):
        print(f"Creating a Rectangle object with lower left corner at {lower_left} and upper right corner at {upper_right}.")
        self.lower_left = lower_left
        self.upper_right = upper_right




point1 = Point(1, 2)
point1.falls_in_rectangle(Rectangle((5,6), (7,9)))

point_x = Point(6,7)
rectangle_x = Rectangle((5,6), (7,9))
point_x.falls_in_rectangle(rectangle_x)
