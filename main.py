from turtle import Turtle, Screen
import Food as F
import time
import movement as m
import Scoreboard
import random as rand
Sc = Screen()
Sc.setup(width=600, height=600)
Sc.title("Snake Game")
Sc.bgcolor("black")
pos = 0
Timmy = m.Snake()
Food = F.Food()
Points = Scoreboard.Scoreboard(0)
Points.Write()
Sc.tracer(0)
Sc.listen()
Sc.onkey(Timmy.up, "w")
Sc.onkey(Timmy.down, "s")
Sc.onkey(Timmy.right, "d")
Sc.onkey(Timmy.left, "a")

while True:
    Sc.update()
    time.sleep(0.1)
    if not Timmy.GameNotOver():
        Points.Update()
        Timmy.reset()
        Points.Write()
    Timmy.move()
    if Timmy.segment[0].distance(Food) < 15:
        Food.refresh()
        Timmy.Increase_Length()
        Points.Score+=1
        Points.Write()

Sc.exitonclick()