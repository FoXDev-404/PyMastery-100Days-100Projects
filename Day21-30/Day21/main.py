# === Snake Game: Part 2 - Animation and Coordinates ===
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Add difficulty selection here
difficulty = screen.textinput("Difficulty", "Choose difficulty (easy/medium/hard):").lower()

# Set speed based on difficulty
if difficulty == "hard":
    game_speed = 0.06
elif difficulty == "medium":
    game_speed = 0.1
else:  # default to easy
    game_speed = 0.15

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
game_is_paused = False
level = 1

def toggle_pause():
    global game_is_paused
    game_is_paused = not game_is_paused
    if game_is_paused:
        scoreboard.goto(0, 0)
        scoreboard.write("PAUSED", align="center", font=("Courier", 24, "normal"))
    else:
        scoreboard.clear()
        scoreboard.goto(0, 260)  # Reset position to top
        scoreboard.update_score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(toggle_pause, "space")
screen.onkey(toggle_pause, "p")

while game_is_on:
    screen.update()
    if not game_is_paused:
        time.sleep(game_speed)
        snake.move()
        
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

            # Level up every 5 points
            if scoreboard.score > level * 5:
                level += 1
                game_speed *= 0.9  # Increase speed by 10%
                scoreboard.update_level(level)

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.game_over()
            game_is_on = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

screen.exitonclick()