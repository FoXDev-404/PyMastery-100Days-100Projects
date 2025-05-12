# PONG Game
from turtle import Screen, Turtle


screen = Screen()
screen.title("PONG Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turns off the screen updates

# Paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    y = paddle.ycor()
    y += 20
    paddle.sety(y)

def go_down():
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen

screen.exitonclick()