from turtle import *

current_diameter = 40
max_diameter = 100
speed(3)


def draw_balloon():
    color('red')
    dot(current_diameter)


def inflate_balloon():
    global current_diameter

    if current_diameter + 10 >= max_diameter:
        clear()
        current_diameter = 40
        write('POP!')
    else:
        current_diameter += 10
        draw_balloon()


draw_balloon()
onkey(inflate_balloon, 'Up')
listen()
done()