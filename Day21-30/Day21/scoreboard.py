# Scoreboard class for a game
from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

# Update file path handling
HIGH_SCORE_FILE = os.path.join(os.path.dirname(__file__), "high_score.txt")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
        
    # Ensure high score is saved automatically when the game ends
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_score()
        
    # Update game_over to reset the score and save high score
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        self.reset()
        
    def load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0
            
    # Ensure save_high_score only writes when necessary
    def save_high_score(self):
        if self.high_score > self.load_high_score():  # Only save if the new high score is greater
            try:
                with open(HIGH_SCORE_FILE, "w") as file:
                    file.write(str(self.high_score))
            except Exception as e:
                pass
            
    def update_level(self, level):
        self.level = level
        self.update_score()