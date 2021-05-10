from turtle import Turtle, Screen
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = -10
        self.sleep = 0.1

    def move(self):
        y = self.ycor() + self.y_move
        x = self.xcor() + self.x_move

        self.goto(x, y)

    def bounce_surface(self):
       self.y_move *= -1
       print(self.y_move)

    def bounce_paddle(self):
        self.x_move *= -1
        self.sleep *= 0.9 #here the 0.1 is getting decreased

    def reset(self):
        self.goto(0,0)
        self.x_move *= -1