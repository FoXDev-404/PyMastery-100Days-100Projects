from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([8, -8])
        self.move_speed = 0.1
        self.speed_factor = 1.0

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
            self.speed_factor += 0.05

    def reset_position(self):
        self.goto(0, 0)
        self.speed_factor = 1.0
        self.move_speed = 0.1
        # Randomize both x and y direction
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([8, -8])
