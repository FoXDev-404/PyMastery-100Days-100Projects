import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.bgcolor("light green")

# Initialize game components
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Game states
MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"
PAUSED = "paused"

game_state = MENU
scoreboard.display_start_screen()

# Key bindings
screen.listen()

def start_game():
    global game_state
    if game_state in [MENU, GAME_OVER]:
        reset_game()
        game_state = PLAYING

def reset_game():
    player.go_to_start()
    car_manager.reset()
    scoreboard.level = 1
    scoreboard.lives = 3
    scoreboard.update_scoreboard()

def toggle_pause():
    global game_state
    if game_state == PLAYING:
        game_state = PAUSED
    elif game_state == PAUSED:
        game_state = PLAYING

# Set up key bindings
screen.onkey(start_game, "space")
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
screen.onkey(toggle_pause, "p")

# Main game loop
while True:
    if game_state == PLAYING:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()
        
        # Detect collision with cars
        for car in car_manager.all_cars:
            if player.distance(car) < 20:
                if scoreboard.lose_life():
                    game_state = GAME_OVER
                    scoreboard.game_over()
                else:
                    # Just lost a life but still have more
                    player.go_to_start()
            
        # Detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()
    
    elif game_state in [MENU, GAME_OVER, PAUSED]:
        screen.update()
        time.sleep(0.1)
        
        if game_state == PAUSED:
            # Display pause message if game is paused
            pause_message = Turtle()
            pause_message.hideturtle()
            pause_message.penup()
            pause_message.color("black")
            pause_message.goto(0, 0)
            pause_message.write("PAUSED - Press P to continue", align="center", font=("Courier", 20, "normal"))
            time.sleep(0.5)  # Show pause message briefly
            pause_message.clear()

screen.exitonclick()