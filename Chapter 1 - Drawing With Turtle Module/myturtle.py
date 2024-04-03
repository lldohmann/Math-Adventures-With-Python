from turtle import *

t = Turtle()
t.shape('turtle')
t.screen.title('Chapter 1: Drawing Polygons With Turtle Module')

def square(sidelength=100):
    for i in range(4):
        t.forward(sidelength)
        t.right(90)
def triangle(sidelength=100):
    for i in range(3):
        t.forward(sidelength)
        t.left(120)
def polygon(sides, sidelength=100):
    for i in range(sides):
        t.forward(sidelength)
        t.left(360/sides)
def turtleSpiral():
    length = 5
    for i in range(60):
        square(length)
        t.right(5)
        length = length + 5
def star(sidelength):
    for i in range(5):
        t.forward(sidelength)
        t.right(144)
def starSpiral():
    length = 5
    for i in range(60):
        star(length)
        t.right(5)
        t.length = length + 5
def starSpiralColor():
    length = 5
    for i in range(20):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            star(length)
            t.right(5)
            length = length + 5
        
starSpiralColor()
 
