from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# def turn_left_or_up():
#     s1.goto(s2.xcor(), s2.ycor())
#     s2.goto(s3.xcor(), s3.ycor())
#     s3.forward(20)
#     s3.left(90)

snake = Snake()
food = Food()
is_game_on = snake.check_game_status()

screen.listen()
screen.onkeypress(snake.turn_up, 'w')
screen.onkeypress(snake.turn_down, "s")
screen.onkeypress(snake.turn_left, "a")
screen.onkeypress(snake.turn_right, "d")

while is_game_on:
    screen.update()
    time.sleep(0.4)
    snake.move()
    is_game_on = snake.check_game_status()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()


screen.exitonclick()
