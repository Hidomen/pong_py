from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time
# hi
UP = 90
DOWN = 270

WIDTH = 1200
HEIGHT = 600 # 800

directions = (UP, DOWN)

PADDLE_COR = 500

BORDER_COR = 280

def game():
    screen = Screen()
    ball = Ball()
    scoreboard = Scoreboard()

    time_speed = 0.1

    screen.bgcolor("black")
    screen.title("PONG")
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)

    paddle_right = Paddle((PADDLE_COR, 0))
    paddle_right.up()

    paddle_left = Paddle((-PADDLE_COR, 0))
    paddle_left.up()

    # LINE DRAWING
    line_drawer = Turtle()
    line_drawer.color("white")
    line_drawer.pu()
    line_drawer.pensize(5)
    line_drawer.goto(0,600)
    line_drawer.setheading(270)

    for i in range(40):
        line_drawer.pu()
        line_drawer.forward(15)
        line_drawer.pd()
        line_drawer.forward(15)




    screen.listen()

    # if puddle not too high
    screen.onkey(paddle_right.up, "Up")
    # if puddle not too low
    screen.onkey(paddle_right.down, "Down")

    # same issues
    screen.onkey(paddle_left.up, "w")
    screen.onkey(paddle_left.down, "s")


    game_over = False

    while not game_over:
        screen.update()
        time.sleep(time_speed)

        paddle_right.move()
        paddle_left.move()

        ball.move()

        # collisions

        # hit the ball
        if ball.distance(paddle_left) < 50 and ball.xcor() < -(PADDLE_COR - 20) or ball.distance(paddle_right) < 50 and ball.xcor() > PADDLE_COR - 20:
            ball.bounce_x()
            time_speed *= 0.9


        # miss the ball
        if ball.xcor() > PADDLE_COR + 50:
            scoreboard.score_up("left")
            ball.reset()
            time_speed = 0.1

            print(time_speed)

        if ball.xcor() < -(PADDLE_COR + 50):
            scoreboard.score_up("right")
            ball.reset()
            time_speed = 0.1

            print(time_speed)

        # bounce the ball from wall
        if ball.ycor() >= HEIGHT/2 or ball.ycor() <= -HEIGHT/2:
            ball.bounce_y()

    # end in 3?

    screen.exitonclick()

game()