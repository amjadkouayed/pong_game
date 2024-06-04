'''
let's create the pong game.
steps:

1-create the screen (done)
2-create and move a paddle (done)
3-create another paddle (done)
4-create the ball and make it move (done)
5-detect collision with wall and bounce (done)
6-detect collision with paddle (doneoooo)
7-detect when paddle misseso

'''

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard



screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.moveup, "w")
screen.onkey(l_paddle.movedown, "s")
screen.onkey(r_paddle.moveup, "o")
screen.onkey(r_paddle.movedown, "l")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.shoot()
    score = 0

    #detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        score += 1

    #detect collision with right side
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()

    #detect collision with left side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
