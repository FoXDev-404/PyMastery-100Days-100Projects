from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turns off the screen updates

# Paddle
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
while game_is_on:
    time.sleep(ball.move_speed)  # Use ball's move_speed instead of hardcoded value
    screen.update()  # Update the screen
    ball.move()  # Move the ball
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() # Bounce the ball off the top and bottom walls
        
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.bounce_x()
    
    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.bounce_x()
    
    
screen.exitonclick()