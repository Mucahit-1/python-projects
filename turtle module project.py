import turtle
import random

color = ["red" , "blue" , "green" , "yellow" , "purple"]
turtle.colormode(255)

def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    random_color = (r , g , b)
    return random_color

painter = turtle.Turtle()
painter.speed("fastest")


for x in range(72):
    painter.color(random_color())
    current_heading = painter.heading()
    painter.circle(100)
    painter.setheading(current_heading + 5)


def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    random_color = (r , g , b)
    return random_color



screen = turtle.Screen()
screen.exitonclick()