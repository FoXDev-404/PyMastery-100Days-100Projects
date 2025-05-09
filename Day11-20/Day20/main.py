# === Snake Game: Part 1 - Animation and Coordinates ===

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


starting_position = [(0,0), (-20,0), (-40,0)]

for positon in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(positon)













screen.exitonclick()