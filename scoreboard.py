from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.level, align="center",
                   font=FONT)

    def update_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-25, 0)
        self.write(f"GAME OVER")
