from turtle import Turtle


FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()


        self.score_left = 0
        self.score_right = 0

        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0,250)
        self.update()


    def score_up(self, player):
        if player == "left":
            self.score_left += 1
        elif player == "right":
            self.score_right += 1
            
        self.clear()
        self.update()


    def update(self):
        self.write(f"{self.score_left} : {self.score_right}", align="center", font=FONT)