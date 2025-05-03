# Wroking with Turtle Graphics module
# Turtle Graphics Doc: https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("tomato3")

# # Draw a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a Dashed Line
for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    


















screen = Screen()
screen.exitonclick()