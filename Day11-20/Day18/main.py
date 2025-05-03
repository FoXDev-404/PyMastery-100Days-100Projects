# Wroking with Turtle Graphics module
# Turtle Graphics Doc: https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen

# tim = Turtle()
# tim.shape("turtle")
# tim.color("tomato3")

# # Draw a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# # Draw a Dashed Line
# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
    
    
# Drawing a tringle(120 deg), square(90 deg), pentagon(72 deg), hexagon(60 deg),
# heptagon(51.42857142857143 deg), octagon(45 deg), nonagon(40) and decagon(36)
import random

tim = Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'pink', 'cyan', 'magenta', 'brown']
tim.pensize(2)

# Reset turtle position to center
tim.penup()
tim.goto(50, 150)
tim.pendown()

# Drawing different shapes with different random colors
for sides in range(3, 11):  # From triangle (3 sides) to hendecagon (11 sides)
    angle = 360 / sides
    tim.color(random.choice(colors))  # Select a new random color for each shape
        
    for _ in range(sides):
        tim.right(angle)
        tim.forward(100)
  
  
         
screen = Screen()
screen.exitonclick()