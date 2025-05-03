# importing module
import turtle

tim = turtle.Turtle()


# Using From import 
from turtle import Turtle

tom = Turtle()
terry = Turtle()


# Aliasing Modules 
import turtle as t # t alias name

timm = t.Turtle()


# installing modules, python packages
import heroes  # using "pip install heroes"

print(heroes.gen())