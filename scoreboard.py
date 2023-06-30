from turtle import Turtle

FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.f = open("score.txt")
        self.highscore = int(self.f.read())
        self.show_score()
        self.f.close()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()
        if self.score > self.highscore:
            self.highscore = self.score
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.goto(100, 230)
        self.write(f"High Score: {self.highscore}", align="center", font=FONT)

    def update_highscore(self):
        self.f = open("score.txt", "w")
        self.f.write(str(self.highscore))
        self.f.close()

