import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_CARS_Y = list(range(-220,220,20))
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.turtlesize(1, 2)
            new_car.setpos(280, random.choice(STARTING_CARS_Y))
            self.car_list.append(new_car)

    def move_turtles(self):
        for car in self.car_list:
           car.back(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT




