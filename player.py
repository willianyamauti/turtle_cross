from turtle import Turtle

SPEED = 10
STARTING_POSITION = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.shape('turtle')
        self.color('black')

    def move_forward(self):
        self.forward(SPEED)

    def reset_position(self):
        self.goto(STARTING_POSITION)

