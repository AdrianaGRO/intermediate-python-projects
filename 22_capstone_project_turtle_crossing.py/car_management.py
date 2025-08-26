from turtle import Turtle
import random


color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_creation_frequency = 6 # create a car every 6 iterations

    def create_car(self):
        if random.randint(1, self.car_creation_frequency) == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(color_list))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def reset_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE

        
