from turtle import Turtle, Screen

screen = Screen()

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(pos)
        self.shapesize(5,1)

    def up(self):
       y = self.ycor() + 40
       self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() +- 40
        self.goto(self.xcor(), y)