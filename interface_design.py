import turtle
import math

def square(t, length):
    for x in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, sides):
    if sides < 3:
        print('Not a polygon')
    else:
        for x in range(sides):
            t.fd(length)
            t.lt(360/sides)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference/3)+1
    length = circumference/n
    polygon(t, length, n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n= int(arc_length/3)+1
    step_length = arc_length / n
    step_angle = angle /n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    """draws n line segments with the given length and angle (in degrees) between them. t is a turtle
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# polyline(jack, 4, 100, 80)
# polyline()
# arc(jack, 100, 180)

def shape0(t, r):
    arc(t, r, 360)
    t.lt(60)
    for x in range(6):
        arc(t,r,60)
        t.lt(120)
        arc(t,r,60)
        t.lt(60)
        t.penup()
        arc(t,r,60)
        t.pendown()
        t.lt(60)

def shape1(t, r):
    arc(t,r,360)
    t.penup()
    arc(t,r/2,180)
    t.pendown()
    arc(t,r/2,180)
    t.penup()
    arc(t,r,180)
    arc(t,r/2,180)
    t.pendown()
    arc(t,r/2,180)
    t.penup()
    t.fd(r/4)
    t.lt(90)
    t.fd(r/2)
    t.pendown()
    arc(t,r/4,360)
    t.penup()
    t.fd(r)
    t.pendown()
    arc(t,r/4,360)

jack = turtle.Turtle()
shape0(jack, 50)
jack.lt(120)
shape1(jack,50)




turtle.mainloop()
