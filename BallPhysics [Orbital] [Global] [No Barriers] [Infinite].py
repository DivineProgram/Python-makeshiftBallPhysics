"""
Ball physics but it orbits around a point in space
"""

from turtle import *
from random import *
import time
import math

g = 0.3 #Gravity Value
ekeep = -0.6 #Energy loss and inversing from hard collision

loop = 0

wn = Screen()
wn.title("Orbital Ball Physics Simulator [ Global Gravity ] [ No Barriers ]")
wn.bgcolor("black")
wn.tracer(0,0)

ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.turtlesize(1)
ball.setheading(0)
ball.speed(0)
ball.penup()
ball.showturtle()
ball.pensize(1)

orbit = Turtle()
orbit.shape("circle")
orbit.color("blue")
orbit.turtlesize(0.25)
orbit.setheading(0)
orbit.speed(0)
orbit.penup()
orbit.showturtle()
orbit.pensize(1)

while True:

    #Window Limitations
    floor = round(wn.window_height() / -2) #Y co-ord of bottom
    walls = round(wn.window_width() / 2) #X co-ord of right

    #Choose Ball Start
    yco = randrange(floor,floor*-1)
    xco = randrange(walls*-1,walls)
    dy = randrange(-10,10)
    dx = randrange(-10,10)

    #Orbit Placement Safe Zone
    orbitFloor = round((wn.window_height() / -2) + (wn.window_height() * 0.4))
    orbitWalls = round((wn.window_width() / 2) - (wn.window_width() * 0.4))

    #Orbit Placement
    orbity = 0
    orbitx = 0
    orbitdistanceX = 0
    orbitdistanceY = 0

    orbit.goto(orbitx,orbity)

    ball.pendown() #Ball Line Decider

    for loop in range(9999999999999999999999999999999999999999999999999):

        #Window Limitations
        floor = round(wn.window_height() / -2)
        walls = round(wn.window_width() / 2)

        #Calculate Orbital Forces and Ball Position
        orbitdistanceX = xco - orbitx
        orbitdistanceY = yco - orbity

        if orbitdistanceX <= 0:
            orbitdistanceXpos = orbitdistanceX * -1
        else:
            orbitdistanceXpos = orbitdistanceX

        if orbitdistanceY <= 0:
            orbitdistanceYpos = orbitdistanceY * -1
        else:
            orbitdistanceYpos = orbitdistanceY

        relXg = orbitdistanceX / (orbitdistanceXpos + orbitdistanceYpos) * g
        relYg = orbitdistanceY / (orbitdistanceXpos + orbitdistanceYpos) * g

        dy = dy - relYg
        dx = dx - relXg
        yco = yco + dy
        xco = xco + dx

        #Draw Ball Position
        dyco = yco
        dxco = xco

        ball.goto(dxco, dyco)

        if loop == 0:
            ball.clear()

        if loop % 10000 == 0:
            wn.tracer(1,0)
            wn.tracer(0,0)


    
