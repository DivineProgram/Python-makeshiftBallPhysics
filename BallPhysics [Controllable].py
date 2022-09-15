
# Classic ball physics

from turtle import *
from random import *

g = 0.3 #Gravity Value
ekeep = -0.8 #Energy loss and inversing from hard collision
efade = 0.9 #Energy loss from constant soft collision

loop = 0

wn = Screen()
wn.title("Ball Physics Simulator")
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

while True:
    
    #Window Limitations
    floor = round(wn.window_height() / -2) #Y co-ord of bottom
    walls = round(wn.window_width() / 2) #X co-ord of right

    #Choose Ball Start
    yco = randrange(floor,floor*-1)
    xco = randrange(walls*-1,walls)
    dy = randrange(-30,30)
    dx = randrange(-30,30)

    ball.penup() #Ball Line Decider

    for loop in range(100000000000):

        #Window Limitations
        floor = round(wn.window_height() / -2)
        walls = round(wn.window_width() / 2)
        
        if yco <= floor + 20: #Floor
            yco = floor + 20
            dy = dy * ekeep
            dx = dx * efade

        if yco >= floor * -1 - 20: #Ceiling
            yco = floor * -1 - 20
            dy = dy * ekeep
            dx = dx * efade

        if xco >= walls - 20: #Right Wall
            xco = walls - 20
            dx = dx * ekeep

        if walls * -1 + 20 >= xco: #Left Wall
            xco = walls * -1 + 20
            dx = dx * ekeep

        dy = round(dy,2)
        dx = round(dx,2)

        #Ball Calculations

        def up():
            global dy
            dy += 3

        def down():
            global dy
            dy -= 3

        def right():
            global dx
            dx += 3

        def left():
            global dx
            dx -= 3

        onkeypress(up,"Up")
        onkeypress(down,"Down")
        onkeypress(right,"Right")
        onkeypress(left,"Left")
        listen()
        
        yco = yco + dy
        dy = dy - g
        xco = xco + dx
        dx = dx / 1.001

        dyco = yco
        dxco = xco

        if floor - 21.4 <= yco <= floor + 21.4:
            dyco = floor + 20

        ball.goto(dxco, dyco)

        if loop == 0:
            ball.clear()    
