from turtle import Turtle
import random

COLORS = ['yellow', 'blue', 'red', 'purple', 'green']
MAX_CARS = 23
MIN_DISTANCE = 150
SPEED = 10


class Car:

    def __init__(self):
        super().__init__()
        # self.penup()
        # self.hideturtle()
        self.movement_multiplier = 0.1
        self.car_speed = int(SPEED * (1+self.movement_multiplier))
        self._last_y_cor = 0
        self._last_x_cor = 0
        self.limit = MAX_CARS
        self.all_cars = []

    def create_car(self):
        _car = Turtle()
        _car.penup()
        _car.shape('square')
        _car.shapesize(stretch_wid=1, stretch_len=2)
        _car.color(random.choice(COLORS))
        self.update_position(_car)
        # print(self._last_x_cor, self._last_y_cor)
        self.all_cars.append(_car)

    def movement(self):

        for car in self.all_cars:
            car.backward(self.car_speed)

    def update_position(self, car):
        _rand_y = random.randint(-240, 240)
        _rand_x = random.randint(280, 1000)
        # avoid cars spawning too close to each other(not working properly)
        while self._last_y_cor - MIN_DISTANCE <= _rand_y <= self._last_y_cor + MIN_DISTANCE:
            _rand_y = random.randint(-240, 240)
        self._last_y_cor = _rand_y
        car.goto(_rand_x, _rand_y)

    def increase_speed(self):
        self.movement_multiplier *= 0.9

