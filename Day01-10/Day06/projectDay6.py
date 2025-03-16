# Maze Solver Algorithm for Reeborg's World
# This code follows the "right-hand rule" to solve the maze
# The robot always sticks to the right wall while moving
# Try it out here: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    # Since there's no built-in right turn, we turn left three times
    turn_left()
    turn_left()
    turn_left()

# Move forward if there's a clear path before starting the main loop
while front_is_clear():
    move()
turn_left()

# Keep going until the robot reaches the goal
while not at_goal():
    # Step 1: If there's space on the right, turn and move
    if right_is_clear():
        turn_right()
        move()
    # Step 2: If no right turn but forward is clear, just move ahead
    elif front_is_clear():
        move()
    # Step 3: If both front and right are blocked, turn left to find a new path
    else:
        turn_left()
