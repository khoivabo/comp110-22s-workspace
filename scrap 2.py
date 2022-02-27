"""House and the sun :)."""

__author__ = "730277137"

from turtle import Turtle, colormode, done


def draw_sun(a_turtle: Turtle,x: float, y: float, length: float):
    """Draw a square with a given length at a given coordinate."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color("yellow")
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(length)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()
    return
picasso_turtle: Turtle = Turtle()
draw_sun(picasso_turtle, 0, 0, 50)
done()