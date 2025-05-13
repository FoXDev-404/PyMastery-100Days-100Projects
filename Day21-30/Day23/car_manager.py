from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_road_markings()

    def create_car(self):
        # Adjust car creation chance based on level difficulty
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            # Randomly vary car sizes for visual interest
            size_multiplier = random.choice([0.9, 1.0, 1.1])
            new_car.shapesize(stretch_wid=1 * size_multiplier, stretch_len=2 * size_multiplier)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 240)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            # Remove cars that have gone off screen
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        
    def create_road_markings(self):
        # Create road borders
        for y_pos in [-250, 250]:
            border = Turtle()
            border.penup()
            border.hideturtle()
            border.color("black")
            border.pensize(3)
            border.goto(-300, y_pos)
            border.pendown()
            border.goto(300, y_pos)
        
        # Create dashed center line
        center_line = Turtle()
        center_line.penup()
        center_line.hideturtle()
        center_line.color("black")
        center_line.pensize(2)
        center_line.goto(-300, 0)
        
        for i in range(-300, 301, 30):
            center_line.penup()
            center_line.goto(i, 0)
            center_line.pendown()
            center_line.forward(15)
    
    def reset(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE