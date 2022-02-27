
from turtle import Turtle, colormode, done

bob: Turtle = Turtle()
bob.pencolor("pink")
bob.penup()
bob.goto(-150, -150)
bob.pendown()
bob.speed(200)
side_length: int = 300
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i += 1

jason: Turtle = Turtle()
jason.pencolor("red")
jason.penup()
jason.goto(-150, -150)
jason.pendown()
jason.speed(1000)
x: int = 0
while (x < 100):
    side_length = side_length * 0.98
    i: int = 0
    while (i < 3):
        jason.forward(side_length)
        jason.left(122)
        i += 1
    x += 1
done()


