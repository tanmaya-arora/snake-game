import time
from turtle import Turtle

class Snake:
    def create_snake(self):
        s1 = Turtle(shape="square")
        s2 = Turtle(shape="square")
        s3 = Turtle(shape="square")
        return [s1, s2, s3]

    def __init__(self):
        self.snakesegment = self.create_snake()
        self.movement = 2
        self.snakesegment[0].color("white")
        self.snakesegment[1].color("white")
        self.snakesegment[2].color("white")
        self.snakesegment[0].penup()
        self.snakesegment[1].penup()
        self.snakesegment[2].penup()
        self.snakesegment[0].goto(-20, 0)
        self.snakesegment[2].goto(20, 0)
        self.head = self.snakesegment[2]

    def move(self):
        for segment_id in range(0, len(self.snakesegment)-1):
            newx = self.snakesegment[segment_id + 1].xcor()
            newy = self.snakesegment[segment_id + 1].ycor()
            self.snakesegment[segment_id].goto(newx, newy)
        self.head.forward(20)

    def check_game_status(self):
        if int(self.head.xcor()) == 300 or int(self.head.xcor() == -300):
            return False
        return True

    def turn_up(self):
        if self.head.heading() != 180:
            self.head.setheading(90)

    def turn_down(self):
        self.head.setheading(270)

    def turn_left(self):
        self.head.setheading(180)

    def turn_right(self):
        self.head.setheading(0)
