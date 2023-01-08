from turtle import Turtle
import random as rand

class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.speed('fastest')
        self.shapesize(0.5, 0.5)
        self.penup()
        self.hideturtle()
        self.refresh()
        self.showturtle()

    def refresh(self):
        x = rand.randint(-275, 275)
        y = rand.randint(-275, 275)
        self.setpos(x, y)
