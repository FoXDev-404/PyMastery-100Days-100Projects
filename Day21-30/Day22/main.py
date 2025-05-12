from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create center line
center_line = Turtle()
center_line.color("white")
center_line.penup()
center_line.goto(0, 300)
center_line.setheading(270)
center_line.hideturtle()
center_line.pensize(5)
for _ in range(30):
    center_line.pendown()
    center_line.forward(10)
    center_line.penup()
    center_line.forward(10)

# Create game objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Set up controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game state variables
game_is_on = True
paused = False

# Pause and restart functionality
def toggle_pause():
    global paused
    paused = not paused

def restart_game():
    global game_is_on
    if not game_is_on:
        game_is_on = True
        scoreboard.reset_game()
        ball.reset_position()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)

screen.onkey(toggle_pause, "space")
screen.onkey(restart_game, "r")

# Main game loop
while True:
    if not game_is_on:
        screen.update()
        time.sleep(0.1)
        continue
        
    if paused:
        screen.update()
        time.sleep(0.1)
        continue
        
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Improved collision detection with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.xcor() < 350) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.xcor() > -350):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        if scoreboard.is_game_over():
            game_is_on = False
            scoreboard.game_over()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        if scoreboard.is_game_over():
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()