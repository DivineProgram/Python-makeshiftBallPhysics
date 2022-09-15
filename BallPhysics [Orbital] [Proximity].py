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
wn.title("Orbital Ball Physics Simulator [ Proximity Gravity ]")
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
    orbitFloor = round((wn.window_height() / -2) + (wn.window_height() * 0.2))
    orbitWalls = round((wn.window_width() / 2) - (wn.window_width() * 0.2))

    #Orbit Placement
    orbity = randrange(orbitFloor,orbitFloor*-1)
    orbitx = randrange(orbitWalls*-1,orbitWalls)
    orbitdistanceX = 0
    orbitdistanceY = 0

    orbit.goto(orbitx,orbity)

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
        orbitdistanceX = xco - orbitx
        orbitdistanceY = yco - orbity


        # Creating positive versions of the distances
        #A
        if orbitdistanceX <= 0:
            orbitdistanceXpos = orbitdistanceX * -1
        else:
            orbitdistanceXpos = orbitdistanceX

        if orbitdistanceY <= 0:
            orbitdistanceYpos = orbitdistanceY * -1
        else:
            orbitdistanceYpos = orbitdistanceY

        # The true hypotenuse distance between the ball and orbit object
        truedistance = math.sqrt(orbitdistanceXpos**2 + orbitdistanceYpos**2)

        #A
        if truedistance <= 200: # Calculating how strong the gravitational pull is
            relG = g
        elif minGravityFade < truedistance <= maxGravityRange:
            relGpercent = ((maxGravityRange - minGravityFade) - (truedistance - minGravityFade)) / (maxGravityRange - minGravityFade)
            relG = g * relGpercent
        else:
            relG = 0

        relXg = orbitdistanceX / (orbitdistanceXpos + orbitdistanceYpos) * relG
        relYg = orbitdistanceY / (orbitdistanceXpos + orbitdistanceYpos) * relG

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


    
