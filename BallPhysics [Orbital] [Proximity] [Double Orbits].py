"""
Ball physics but it orbits around a point in space
The gravity weakens the further away from the orbit object
"""

from turtle import *
from random import *
import time
import math

g = 0.3 #Gravity Value
relG = g #Relative gravity on the ball depending on how close the ball is to the orbit object
ekeep = -0.6 #Energy loss and inversing from hard collision
maxGravityRange = 500 #How far the gravity stretches out
minGravityFade = 100 #How far the ball has to be from the orbit object for the affect of gravity to start fading

loop = 0

wn = Screen()
wn.title("Orbital Ball Physics Simulator [ Proximity Gravity ] [ Double Orbits ]")
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

orbitA = Turtle()
orbitA.shape("circle")
orbitA.color("blue")
orbitA.turtlesize(0.25)
orbitA.setheading(0)
orbitA.speed(0)
orbitA.penup()
orbitA.showturtle()
orbitA.pensize(1)

orbitB = Turtle()
orbitB.shape("circle")
orbitB.color("blue")
orbitB.turtlesize(0.25)
orbitB.setheading(0)
orbitB.speed(0)
orbitB.penup()
orbitB.showturtle()
orbitB.pensize(1)

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
    orbitFloor = round((wn.window_height() / -2) + (wn.window_height() * 0.2))
    orbitWalls = round((wn.window_width() / 2) - (wn.window_width() * 0.2))

    #Orbit Placement
    orbitAy = randrange(orbitFloor,orbitFloor*-1)
    orbitAx = randrange(orbitWalls*-1,orbitWalls)
    orbitdistanceAX = 0
    orbitdistanceAY = 0
    orbitBy = randrange(orbitFloor,orbitFloor*-1)
    orbitBx = randrange(orbitWalls*-1,orbitWalls)
    orbitdistanceBX = 0
    orbitdistanceBY = 0

    orbitA.goto(orbitAx,orbitAy)
    orbitB.goto(orbitBx,orbitBy)

    ball.penup() #Ball Line Decider

    for loop in range(750):

        #Window Limitations
        floor = round(wn.window_height() / -2)
        walls = round(wn.window_width() / 2)

        if yco <= floor + 15: #Floor
            yco = floor + 20
            dy = dy * ekeep

        if yco >= floor * -1 - 15: #Ceiling
            yco = floor * -1 - 20
            dy = dy * ekeep

        if xco >= walls - 15: #Right Wall
            xco = walls - 20
            dx = dx * ekeep

        if walls * -1 + 15 >= xco: #Left Wall
            xco = walls * -1 + 20
            dx = dx * ekeep

        #Calculate Orbital Forces and Ball Position
        orbitdistanceAX = xco - orbitAx
        orbitdistanceAY = yco - orbitAy
        orbitdistanceBX = xco - orbitBx
        orbitdistanceBY = yco - orbitBy

        # Creating positive versions of the distances
        #A
        if orbitdistanceAX <= 0:
            orbitdistanceAXpos = orbitdistanceAX * -1
        else:
            orbitdistanceAXpos = orbitdistanceAX

        if orbitdistanceAY <= 0:
            orbitdistanceAYpos = orbitdistanceAY * -1
        else:
            orbitdistanceAYpos = orbitdistanceAY
        #B
        if orbitdistanceBX <= 0:
            orbitdistanceBXpos = orbitdistanceBX * -1
        else:
            orbitdistanceBXpos = orbitdistanceBX

        if orbitdistanceBY <= 0:
            orbitdistanceBYpos = orbitdistanceBY * -1
        else:
            orbitdistanceBYpos = orbitdistanceBY

        # The true hypotenuse distance between the ball and orbit object
        truedistanceA = math.sqrt(orbitdistanceAXpos**2 + orbitdistanceAYpos**2)
        truedistanceB = math.sqrt(orbitdistanceBXpos**2 + orbitdistanceBYpos**2)

        #A
        if truedistanceA <= 200: # Calculating how strong the gravitational pull is
            relGA = g
        elif minGravityFade < truedistanceA <= maxGravityRange:
            relGApercent = ((maxGravityRange - minGravityFade) - (truedistanceA - minGravityFade)) / (maxGravityRange - minGravityFade)
            relGA = g * relGApercent
        else:
            relGA = 0
        #B
        if truedistanceB <= 200: # Calculating how strong the gravitational pull is
            relGB = g
        elif minGravityFade < truedistanceB <= maxGravityRange:
            relGBpercent = ((maxGravityRange - minGravityFade) - (truedistanceB - minGravityFade)) / (maxGravityRange - minGravityFade)
            relGB = g * relGBpercent
        else:
            relGB = 0

        relAXg = orbitdistanceAX / (orbitdistanceAXpos + orbitdistanceAYpos) * relGA
        relAYg = orbitdistanceAY / (orbitdistanceAXpos + orbitdistanceAYpos) * relGA

        relBXg = orbitdistanceBX / (orbitdistanceBXpos + orbitdistanceBYpos) * relGB
        relBYg = orbitdistanceBY / (orbitdistanceBXpos + orbitdistanceBYpos) * relGB

        dy = dy - relAYg
        dx = dx - relAXg
        dy = dy - relBYg
        dx = dx - relBXg
        yco = yco + dy
        xco = xco + dx

        #Draw Ball Position
        dyco = yco
        dxco = xco

        ball.goto(dxco, dyco)

        if loop == 0:
            ball.clear()


    
