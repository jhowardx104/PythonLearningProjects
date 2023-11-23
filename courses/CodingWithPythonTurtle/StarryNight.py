from turtle import *
from random import *

bgcolor('black')
color('white')
speed(0)

width = window_width()
height = window_height()


def draw_a_star(side_size):
    color('yellow')
    begin_fill()
    for i in range(5):
        left(55)
        forward(side_size)
        right(270)
    end_fill()


def get_rand_position():
    x = width / 2
    y = height / 2
    return randrange(-x, x), randrange(-y, y)


def get_rand_size():
    return randrange(5, 25)


def draw_star(size, star_position):
    penup()
    goto(star_position[0], star_position[1])
    pendown()
    draw_a_star(size)


def generate_star():
    star_position = get_rand_position()
    size = get_rand_size()
    draw_star(size, star_position)


for i in range(100):
    generate_star()


done()
