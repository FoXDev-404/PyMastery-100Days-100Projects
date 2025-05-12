from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # Turns off the screen updates

# Create a dashed line in the center
def draw_center_line():
    center_line = Turtle()
    center_line.color("white")
    center_line.penup()
    center_line.goto(0, -300)
    center_line.setheading(90)  # Point upward
    center_line.hideturtle()
    center_line.pensize(5)
    
    # Draw dashed line
    for _ in range(30):  # Adjust number for desired dash density
        center_line.pendown()
        center_line.forward(10)
        center_line.penup()
        center_line.forward(10)

# Draw the center line
draw_center_line()

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
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        time.sleep(0.5)  # Brief pause after scoring
    
    # Detect L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
        time.sleep(0.5)  # Brief pause after scoring
    
    # Check if game is over
    if scoreboard.is_game_over():
        scoreboard.game_over()
        game_is_on = False
    
screen.exitonclick()