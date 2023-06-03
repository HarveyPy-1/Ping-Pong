from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
l_scoreboard = Scoreboard((-35, 230))
r_scoreboard = Scoreboard((35, 230))

turtle = Turtle()
turtle.penup()
turtle.color("white")
turtle.goto(0, 300)
turtle.pensize(5)
turtle.pendown()
turtle.right(90)
for i in range(30):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)


screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # My method of keeping xcor the same and ycor -ve didn't work because, when it hits 280, it'll
        # trigger once and come down, next time it wont be at 280, then it'll move() again (go up), then
        # it'll get to 280 again and repeat, so not getting the desired result.
        # Her method changes the ycor permanently to -ve, so when it moves(), it goes the opposite way forever

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect when right paddle misses ball
    if ball.xcor() > 380:
        l_scoreboard.reset_position()
        ball.goto(0, 0)
        ball.move_left()

    # Detect when left paddle misses ball
    elif ball.xcor() < -380:
        r_scoreboard.reset_position()
        ball.goto(0, 0)
        ball.move_right()



screen.exitonclick()