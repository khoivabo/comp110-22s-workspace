"""House and the sun :)."""

__author__ = "730277137"

from turtle import Turtle, colormode, done
from typing import final


def draw_house(a_turtle: Turtle, x: float, y: float, width: float, length: float):
    """Draw a rectangle with a given width and length at a given coordinate."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 2:
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.forward(length)
        a_turtle.right(90)
        i += 1
    return


def draw_roof(a_turtle: Turtle, x: float, y: float, length: float):
    """Draw a triangle with a given length at a given coordinate."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0 
    while i < 3:
        a_turtle.forward(length)
        a_turtle.left(120)
        i += 1
    return


def draw_sun(a_turtle: Turtle, x: float, y: float, length: float):
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


def draw_window(a_turtle: Turtle, x: float, y: float, size: float):
    """Draw windows and filling in the color at."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.color("gray")
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(size)
        a_turtle.right(90)
        i += 1
    return


def main() -> None:
    """The entrypoint of my scene."""
    """I'm drawing a house and the sun."""
    picasso_turtle: Turtle = Turtle()
    house_length: float = 300
    house_width: float = 200
    draw_house(picasso_turtle, 0, 0, house_length, house_width)
    draw_roof(picasso_turtle, 0, 0, house_length)
    draw_window(picasso_turtle, house_length * 0.10, house_width * -0.25, float(house_length * 0.25))
    draw_window(picasso_turtle, house_length * 0.25, house_width * -0.25, float(house_length * 0.25))
    draw_sun(picasso_turtle, -300, 300, 70)

    
if __name__ == "__main__":
    main()