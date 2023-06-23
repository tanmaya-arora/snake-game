from turtle import Screen
from snake import Snake
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
is_game_on = snake.check_game_status()

while is_game_on:
    screen.update()
    time.sleep(0.8)
    snake.move()
    is_game_on = snake.check_game_status()



# screen.onkey(snake.turn_down(), "S")
# screen.onkey(snake.turn_left(), "A")
# screen.onkey(snake.turn_right(), "D")
#screen.onkeyrelease(snake.turn_up(), 'W')
#screen.onscreenclick(snake.turn_up())


screen.exitonclick()
