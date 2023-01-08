from turtle import Turtle


class Snake:
    def __init__(self, segment=[]):
        self.segment = []
        self.create()
    def create(self):

        pos = 0
        for i in range(3):
            Turt = Turtle(shape="square")
            Turt.penup()
            self.segment.append(Turt)
            self.segment[i].goto(pos, 0)
            self.segment[i].color("white")
            pos -= 20

    def move(self):
        for j in range(len(self.segment) - 1, 0, -1):
            x = self.segment[j - 1].xcor()
            y = self.segment[j - 1].ycor()
            self.segment[j].setpos(x, y)
        self.segment[0].forward(20)



    def up(self):
        if self.segment[0].heading() == 180 or self.segment[0].heading() == 0:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() == 180 or self.segment[0].heading() == 0:
            self.segment[0].setheading(270)


    def right(self):
        if self.segment[0].heading() == 90 or self.segment[0].heading() == 270:
            self.segment[0].setheading(0)

    def left(self):
        if self.segment[0].heading() == 90 or self.segment[0].heading() == 270:
            self.segment[0].setheading(180)

    def Increase_Length(self):
        TimmyII = Turtle("square")
        TimmyII.color("white")
        TimmyII.hideturtle()
        TimmyII.penup()
        self.segment.append(TimmyII)
        self.segment[-1].setpos(self.segment[-2].pos())
        self.segment[-1].showturtle()
    def reset(self):
        for i in self.segment:
            i.hideturtle()
        self.segment.clear()
        self.create()
    def GameNotOver(self):
        if self.segment[0].xcor() > 280 or self.segment[0].xcor() < -280 or self.segment[0].ycor() > 280 or self.segment[0].ycor() < -280:
            return False
        for j in self.segment[2:]:
            if self.segment[0].distance(j) < 10:
                return False
        return True