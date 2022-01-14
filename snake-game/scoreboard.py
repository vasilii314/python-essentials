from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.readline())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
