from turtle import Turtle

ALIGNMENT = 'left'
FONT = ('Arial', 25, "normal")
SCORE_POSITION = (-250, 250)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(SCORE_POSITION)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f'LEVEL: {self.level}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 250)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)