from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 260)
        self.color("black")
        self.score_num = -1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.score_num += 1
        self.write(arg=f"Score: {self.score_num}", move=False, align="center",
                       font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=FONT)



