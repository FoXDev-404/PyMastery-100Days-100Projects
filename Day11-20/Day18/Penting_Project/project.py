# TODO: Recreating the Hirst spot painting

import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

# Use absolute path to be certain of image location
# TODO: Extract color from image
# image_path = os.path.join(os.path.dirname(__file__), "image.png")
# colors = colorgram.extract(image_path, 20)

# rgb_colors = []


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# Color List
color_list = [(155, 97, 26), (18, 35, 56), (44, 106, 149), (239, 118, 35), (224, 212, 2), (238, 80, 94), (237, 95, 36), (130, 215, 206), (149, 184, 220), (211, 154, 163), (165, 46, 135), (85, 182, 5), (51, 91, 85), (133, 217, 220), (231, 209, 65), (216, 131, 23)]

tom = Turtle()
tom.speed("fastest")
tom.penup()

# Init: Dot Size and Spacing
dot_size = 20
spacing = 50

# Starting position (bottom left corner)
tom.setheading(225)  # Turtle direction to the left
tom.forward(300)     # Move towards left
tom.setheading(0)    # Turtle direction to the right

# 10x10 grid
for y in range(10):
    for x in range(10):
        tom.dot(dot_size, random.choice(color_list))  # Random color ka dot banao
        if x < 9:
            tom.forward(spacing)                      # Aage badho

    # Next row pe jaane ke liye upar jao aur left se start karo
    tom.left(90)
    tom.forward(spacing)
    tom.left(90)
    tom.forward(spacing * 9)
    tom.right(180)  # Face right direction for next row

screen = Screen()
screen.exitonclick()  # Keep screen open until click on it