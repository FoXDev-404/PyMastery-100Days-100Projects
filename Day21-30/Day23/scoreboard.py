from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 36, "bold")
SMALL_FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.lives = 3
        self.high_score = self.load_high_score()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", font=FONT)
        self.goto(0, 260)
        self.write(f"Lives: {self.lives}", align="center", font=FONT)
        self.goto(280, 260)
        self.write(f"High Score: {self.high_score}", align="right", font=SMALL_FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()
        return self.lives <= 0
    
    def game_over(self):
        # Update high score if current level is higher
        if self.level > self.high_score:
            self.high_score = self.level
            self.save_high_score()
            
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
        self.goto(0, -40)
        self.write(f"You reached level {self.level}", align="center", font=FONT)
        self.goto(0, -80)
        self.write("Press SPACE to play again", align="center", font=SMALL_FONT)
    
    def display_start_screen(self):
        self.clear()
        self.goto(0, 100)
        self.write("TURTLE CROSSING", align="center", font=GAME_OVER_FONT)
        self.goto(0, 50)
        self.write("Help the turtle cross the road!", align="center", font=FONT)
        self.goto(0, 0)
        self.write("Use UP to move forward", align="center", font=SMALL_FONT)
        self.goto(0, -30)
        self.write("Use LEFT/RIGHT to move sideways", align="center", font=SMALL_FONT)
        self.goto(0, -80)
        self.write("Press SPACE to start", align="center", font=SMALL_FONT)
    
    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 1
    
    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))