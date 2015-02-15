__author__ = 'Lunding'

import turtle

def draw_square(some_turtle):
    for x in range(0, 4):
        some_turtle.backward(100)
        some_turtle.left(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    jolie = turtle.Turtle()
    jolie.color("green")
    for x in range(0, 3):
        jolie.forward(100)
        jolie.right(120)

def draw_square_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.speed(100)
    brad.shape("turtle")
    brad.color("yellow")
    grad = 360/2
    for x in range (0, grad):
        draw_square(brad)
        brad.left(360/grad)
    window.exitonclick()

def draw_fractal():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.speed(10)
    brad.shape("turtle")
    brad.color("yellow")
    draw_factal(4, brad)
    window.exitonclick()

def draw_factal(numb, skildpadde):
    dist = numb * 50
    if (numb >= 1):
        skildpadde.right(60)
        skildpadde.forward(dist)
        skildpadde.right(120)
        skildpadde.forward(dist)
        skildpadde.right(120)
        skildpadde.forward(dist)
        skildpadde.right(60)
        numb -= 1
        draw_factal(numb, skildpadde)


draw_fractal()