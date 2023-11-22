from turtle import *
from random import *

inflations = 0
current_diameter = 40
max_diameter = 1000
speed(3)


def draw_balloon():
    color('red')
    dot(current_diameter)


def inflate_balloon():
    global current_diameter, inflations

    inflations += 1
    rand_inflation = randrange(1, 30)

    if current_diameter + rand_inflation >= max_diameter:
        clear()
        current_diameter = 40
        write('POP!')
        inflations = 0
    else:
        current_diameter += rand_inflation
        draw_balloon()


draw_balloon()
onkey(inflate_balloon, 'Up')
listen()
done()