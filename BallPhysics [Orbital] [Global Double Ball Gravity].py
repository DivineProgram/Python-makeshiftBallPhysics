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
wn.title("Orbital Ball Physics Simulator [ Global Double Ball Gravity ]")
wn.bgcolor("black")

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
orbit.color("white")
orbit.turtlesize(1)
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
    ycoA = randrange(floor,floor*-1)
    xcoA = randrange(walls*-1,walls)
    dyA = randrange(-10,10)
    dxA = randrange(-10,10)

    #Orbit Placement Safe Zone
    orbitFloor = round((wn.window_height() / -2) + (wn.window_height() * 0.2))
    orbitWalls = round((wn.window_width() / 2) - (wn.window_width() * 0.2))

    #Orbit Placement
    ycoB = randrange(floor,floor*-1)
    xcoB = randrange(walls*-1,walls)
    dyB = randrange(-10,10)
    dxB = randrange(-10,10)
    orbitdistanceXA = 0
    orbitdistanceYA = 0

    orbit.goto(xcoB,ycoB)

    ball.penup() #Ball Line Decider

    for loop in range(750):

        #Window Limitations
        floor = round(wn.window_height() / -2)
        walls = round(wn.window_width() / 2)

        if ycoA <= floor + 15: #Floor
            ycoA = floor + 20
            dyA = dyA * ekeep

        if ycoA >= floor * -1 - 15: #Ceiling
            ycoA = floor * -1 - 20
            dyA = dyA * ekeep

        if xcoA >= walls - 15: #Right Wall
            xcoA = walls - 20
            dxA = dxA * ekeep

        if walls * -1 + 15 >= xcoA: #Left Wall
            xcoA = walls * -1 + 20
            dxA = dxA * ekeep

        if ycoB <= floor + 15: #Floor
            ycoB = floor + 20
            dyB = dyB * ekeep

        if ycoB >= floor * -1 - 15: #Ceiling
            ycoB = floor * -1 - 20
            dyB = dyB * ekeep

        if xcoB >= walls - 15: #Right Wall
            xcoB = walls - 20
            dxB = dxB * ekeep

        if walls * -1 + 15 >= xcoB: #Left Wall
            xcoB = walls * -1 + 20
            dxB = dxB * ekeep

        #Calculate Orbital Forces and Ball Position
        orbitdistanceXA = xcoA - xcoB
        orbitdistanceYA = ycoA - ycoB
        orbitdistanceXB = xcoB - xcoA
        orbitdistanceYB = ycoB - ycoA

        if orbitdistanceXA <= 0:
            orbitdistanceXpos = orbitdistanceXA * -1
        else:
            orbitdistanceXpos = orbitdistanceXA

        if orbitdistanceYA <= 0:
            orbitdistanceYpos = orbitdistanceYA * -1
        else:
            orbitdistanceYpos = orbitdistanceYA

        relXgA = orbitdistanceXA / (orbitdistanceXpos + orbitdistanceYpos) * g
        relYgA = orbitdistanceYA / (orbitdistanceXpos + orbitdistanceYpos) * g

        relXgB = orbitdistanceXB / (orbitdistanceXpos + orbitdistanceYpos) * g
        relYgB = orbitdistanceYB / (orbitdistanceXpos + orbitdistanceYpos) * g

        dyA = dyA - relYgA
        dxA = dxA - relXgA
        ycoA = ycoA + dyA
        xcoA = xcoA + dxA

        dyB = dyB - relYgB
        dxB = dxB - relXgB
        ycoB = ycoB + dyB
        xcoB = xcoB + dxB

        #Draw Ball Position
        dycoA = ycoA
        dxcoA = xcoA
        dycoB = ycoB
        dxcoB = xcoB

        ball.goto(dxcoA, dycoA)
        orbit.goto(dxcoB,dycoB)

        if loop == 0:
            ball.clear()


    
