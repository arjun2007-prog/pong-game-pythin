from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((300,0))
paddle_opp = Paddle((-300,0))
ball = Ball()
score = Score()

game_is_on = True
screen.listen()

screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")

screen.onkey(paddle_opp.up, "w")
screen.onkey(paddle_opp.down, "s")

score.draw_line()

def start():
  while game_is_on == True:
    print(f"sleep is {ball.sleep}")
    score.draw_score()
    time.sleep(ball.sleep)
    screen.update()
    ball.move()
    print(ball.y_move)

    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_surface()
        ball.move()
        print(ball.heading())

    if ball.distance(paddle) < 50 and ball.xcor() > 230 or ball.distance(paddle_opp) < 50 and ball.xcor() < -230:
        ball.bounce_paddle()
        ball.move()

    if ball.xcor() > 300:
        ball.reset()
        score.score1 += 1
        ball.sleep = 0.1

    if ball.xcor() < -300:
        ball.reset()
        score.score2 += 1
        ball.sleep = 0.1

screen.onkey(start, "space")

screen.exitonclick()

