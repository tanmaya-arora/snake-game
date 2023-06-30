import time
from turtle import Turtle

class Snake:
    def create_snake(self):
        s = Turtle(shape="square")
        return s

    def __init__(self):
        self.snakesegment = []
        self.gotopositions = [(-280, 0), (-260, 0), (-240, 0)]
        for i in range(3):
            self.snakesegment.append(self.create_snake())
            self.snakesegment[i].color("white")
            self.snakesegment[i].penup()
            self.snakesegment[i].goto(self.gotopositions[i])
        self.movement = 2
        # self.snakesegment[0].color("white")
        # self.snakesegment[1].color("white")
        # self.snakesegment[2].color("white")
        # self.snakesegment[0].penup()
        # self.snakesegment[1].penup()
        # self.snakesegment[2].penup()
        # self.snakesegment[0].goto(-20, 0)
        # self.snakesegment[2].goto(20, 0)
        self.head = self.snakesegment[2]

    def move(self):
        for segment_id in range(0, len(self.snakesegment)-1):
            newx = self.snakesegment[segment_id + 1].xcor()
            newy = self.snakesegment[segment_id + 1].ycor()
            self.snakesegment[segment_id].goto(newx, newy)
        self.head.forward(20)

    def check_game_status(self):
        if int(self.head.xcor()) == 300 or int(self.head.xcor() == -300) or \
                int(self.head.ycor()) == 280 or int(self.head.ycor()) == -280:
            return False
        else:
            for i in range(len(self.snakesegment) - 1):
                if int(self.head.distance(self.snakesegment[i])) < 20:
                    return False
        return True

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_segment(self):
        self.snakesegment.append(self.create_snake())
        self.head = self.snakesegment[len(self.snakesegment) - 1]

        for i in range(len(self.snakesegment) - 1):
            self.snakesegment[i].goto(self.gotopositions[i])

        self.gotopositions.append((self.gotopositions[-1][0]+20, self.gotopositions[-1][1]))

        for i in range(len(self.snakesegment)):
            self.snakesegment[i].color("white")
            self.snakesegment[i].penup()
            self.snakesegment[i].goto(self.gotopositions[i])
