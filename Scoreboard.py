from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,Score):
        with open("HighScore.txt","r") as HS:
            Content = HS.read()
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 260)
        self.Score = Score
        self.HighScore = int(Content[-1])
    def Write(self):
        self.clear()
        self.write(f"Score : {self.Score}\t High Score : {self.HighScore}", False, "center",font=('Ariel',16,'normal'))
    def Update(self):
        if self.Score > self.HighScore:
            self.HighScore = self.Score
            with open("HighScore.txt","w") as HS:
                HS.write(f"High Score : {self.Score}")
        self.Score = 0
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over\nFinal Score : {self.Score}",False,"center",font=('Ariel',16,'normal'))



