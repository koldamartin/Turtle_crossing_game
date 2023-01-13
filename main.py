import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.15)

    #create car with a chance 1/6
    random_number = random.randint(1, 6)
    if random_number == 1:
        car.create_car()
    car.move_turtles()
    screen.update()

    #detect collision with a car
    for passing_car in car.car_list:
        if player.distance(passing_car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect if the player crosses the finish line
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.update_scoreboard()
        car.increase_speed()

screen.exitonclick()