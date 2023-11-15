from turtle import Turtle

UP = 90
DOWN = 270

BORDER_COR = 250

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(position)

    def up(self):
        if not self.ycor() > BORDER_COR:
            self.setheading(UP)

    
    def down(self):
        if not self.ycor() < -BORDER_COR:
            self.setheading(DOWN)


    def move(self):
        if self.heading() == UP or self.heading() == DOWN:
            self.forward(20)


        if self.ycor() > BORDER_COR:
            self.down()
        elif self.ycor() < -BORDER_COR:
            self.up()