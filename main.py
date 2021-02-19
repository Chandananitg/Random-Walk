from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.title("Random Walk")
tim.pensize(15)
angle_list = [0, 90, 270]
tim.hideturtle()
def random_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    colour = (red, green, blue)
    return colour


while True:
    tim.speed(10)
    angle = random.choice(angle_list)
    colour= random_colour()
    tim.pencolor(colour)
    tim.forward(30)
    tim.right(angle)

screen.exitonclick()
