from turtle import *
from random import *

move_distance = 10

bgcolor('#D2691E')
color('blue')
speed(0)

width = window_width()
height = window_height()
tide = 250


def draw_ocean():
    penup()
    w = width/2
    h = height/2
    goto(w-tide, h)
    pendown()
    begin_fill()
    goto(w-tide, -h)
    goto(w, -h)
    goto(w, h)
    goto(w-tide, h)
    end_fill()


def init_turtle():
    penup()
    goto(-200, 0)
    pendown()
    color('green')
    shape('turtle')


def check_goal():
    if xcor() > width / 2 - tide:
        hideturtle()
        color('white')
        write('You absolute winner!')
        disable_player_control()


def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()


def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()


def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()


def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()


def enable_player_control():
    onkey(move_up, "Up")
    onkey(move_down, "Down")
    onkey(move_right, "Right")
    onkey(move_left, "Left")


def disable_player_control():
    onkey(None, "Up")
    onkey(None, "Down")
    onkey(None, "Right")
    onkey(None, "Left")


def initialize_game():
    draw_ocean()
    init_turtle()
    penup()
    enable_player_control()


initialize_game()
listen()
done()
