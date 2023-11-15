from turtle import Turtle
import random

RIGHT_UP = 45
LEFT_UP = 135
LEFT_DOWN = 225
RIGHT_DOWN = 315

SPEED = 10

destination = (RIGHT_UP, LEFT_UP, RIGHT_DOWN, LEFT_DOWN)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.pu()
        self.setheading(random.choice(destination))
        # self.speed(0)

        self.x_move = SPEED
        self.y_move = SPEED


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def reset(self):
        self.goto(0,0)
        self.x_move *= -1
        self.y_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1