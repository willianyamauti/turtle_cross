from turtle import Screen
from player import Player
from scoreboard import Score
from car import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle Cross')

screen.tracer(0)

score = Score()
turtle = Player()
screen.listen()


""" Movements """
# right paddle
screen.onkey(key='Up', fun=turtle.move_forward)
cars = Car()

# creates a list with the maximum amount of cars allowed
for n in range(cars.limit):
    cars.create_car()

game_is_on = True

while game_is_on:
    time.sleep(cars.movement_multiplier)
    screen.update()
    cars.movement()

    # detect if turtle reached the end
    if turtle.ycor() > 290:
        score.update_score()
        cars.increase_speed()
        turtle.reset_position()

    # detect collision with car
    for car in cars.all_cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            score.game_over()

    # detect if car reached the end of the line:
    for car in cars.all_cars:
        if car.xcor() < -320:
            cars.update_position(car)

screen.exitonclick()
