# Turtle Racing Game

from turtle import Turtle, Screen
import random

# Set up screen
screen = Screen()
screen.title("Turtle Racing Game 🐢✨")
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]

# Ask for user's bet
user_bet = screen.textinput(title="Make your bet 🎀", prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple):")
if user_bet:
    user_bet = user_bet.strip().lower()
else:
    user_bet = ""

# Draw finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(230, -150)
finish_line.pendown()
finish_line.left(90)
finish_line.forward(300)

all_turtles = []

# Create turtles and place them at starting line
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Check if the bet is valid
is_race_on = False
if user_bet in colors:
    is_race_on = True
else:
    print("Oopsie~ That's not a valid color, Psycho! Choose from red, orange, yellow, green, blue, or purple 💕")

# Start race
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet:
                print(f"Yayyy Psycho~ You've WON!! 🎉 The {winning_color} turtle is the winner! 💖🐢")
            else:
                print(f"Aww no~ You've lost, Psycho 💔 The {winning_color} turtle won the race instead!")
            break

screen.exitonclick()
