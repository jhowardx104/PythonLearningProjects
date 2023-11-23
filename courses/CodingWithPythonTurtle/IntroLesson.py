import turtle
import time

t = turtle.Turtle()

for c in ['red', 'green', 'yellow', 'blue', 'orange', 'pink', 'violet', 'purple']:
    t.color(c)
    t.forward(50)
    t.left(45)

time.sleep(5)