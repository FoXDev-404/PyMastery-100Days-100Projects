from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    def go_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        # Keep player within screen boundaries
        if new_x > -280:
            self.goto(new_x, self.ycor())
    
    def go_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        # Keep player within screen boundaries
        if new_x < 280:
            self.goto(new_x, self.ycor())
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False