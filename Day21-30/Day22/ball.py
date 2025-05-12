from turtle import Turtle
import random


class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = random.choice([10, -10])  # Increased from 3 to 10 for faster initial speed
        self.y_move = random.choice([8, -8])    # Increased from 2 to 8 for faster initial speed
        self.move_speed = 0.1  # Initial speed as requested
        self.speed_factor = 1.0  # Factor to gradually increase actual ball speed

    def move(self):
        new_x = self.xcor() + (self.x_move * self.speed_factor)
        new_y = self.ycor() + (self.y_move * self.speed_factor)
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        # Only reduce move_speed if it's still above a reasonable minimum
        if self.move_speed > 0.03:
            self.move_speed *= 0.9
        # Cap the speed factor to prevent excessive speed
        if self.speed_factor < 1.5:
            self.speed_factor += 0.05  # Gradually increase ball speed

    def reset_position(self):
        self.goto(0, 0)
        self.speed_factor = 1.0
        self.move_speed = 0.1  # Reset to initial speed
        # Random direction after reset with faster initial speed
        self.x_move = random.choice([10, -10])
        self.bounce_x()
