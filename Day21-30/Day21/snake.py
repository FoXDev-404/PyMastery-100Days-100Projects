from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto.position()
        self.segments.append(new_segment)
    
    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)
        self.move()
        self.segments[-1].goto(self.segments[-2].position())
        self.segments[-1].setheading(self.segments[-2].heading())
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != 270:  # Prevent reversing direction
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:  # Prevent reversing direction
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:  # Prevent reversing direction
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:  # Prevent reversing direction
            self.head.setheading(0)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]