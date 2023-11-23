import turtle
import time

t = turtle.Turtle()

for c in ['blue', 'green', 'blue', 'red']:
    t.begin_fill()
    t.color(c)
    t.circle(50)
    t.end_fill()
    t.color('white')
    t.forward(100)