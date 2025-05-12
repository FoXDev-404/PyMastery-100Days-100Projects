from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.winning_score = 5  # Set winning score
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        if self.l_score >= self.winning_score:
            winner = "Left Player"
        else:
            winner = "Right Player"
        self.write(f"GAME OVER! {winner} wins!", align="center", font=("Courier", 24, "normal"))
        
    def reset_game(self):
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def is_game_over(self):
        return self.l_score >= self.winning_score or self.r_score >= self.winning_score