from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len= 1)
        self.color("white")
        self.penup()
        self.goto(position)

    # def create_paddle(self, position):
    #     self.shape("square")
    #     self.shapesize(stretch_wid=5, stretch_len= 1)
    #     self.color("white")
    #     self.penup()
    #     self.teleport(x=350, y=0)

    def moveup(self):
        y = self.ycor() 
        y += 40
        self.sety(y)  

    def movedown(self):
        y = self.ycor() 
        y -= 40
        self.sety(y)  