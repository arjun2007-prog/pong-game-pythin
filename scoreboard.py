from turtle import Turtle, Screen

screen = Screen()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score1 = 0
        self.score2 = 0
        self.color("white")

    def draw_score(self):
        self.penup()
        self.clear()
        self.goto(-100,200)
        self.write(self.score1, move=False, align="left", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.score2, move=False, align="left", font=("Courier", 50, "normal"))

    def draw_line(self):
        self.setheading(270)
        self.goto(0, 300)
        while self.ycor() != -300:
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)
