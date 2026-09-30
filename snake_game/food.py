from turtle import Turtle
from cherry_shape import create_cherry_shape
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()

        cherries = create_cherry_shape()
        self.getscreen().register_shape("cherries", cherries)


        self.getscreen().register_shape("cherries", cherries)
        self.shape("cherries")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 250)
        self.goto(random_x, random_y)