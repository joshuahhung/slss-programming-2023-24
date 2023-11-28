# Functions and Turtle
# Author: Josh
# 28 Nov. 2023

import turtle

burt = turtle.Turtle()

burt.color("lightblue")

def squared(num: float) -> float:
    """Takes a number and squares it."""
    
    return num**2

def draw_square(side_length: int) -> None:
    """Draw a square of a given length"""
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)

burt.speed(0)
draw_square(5)
draw_square(10)

# Draw squares that grow exponentially
for i in range(20):
    draw_square(squared(i))

turtle.done()