
#Ball Physics, but a little more customization

from turtle import *
from random import *

print("\n\n\n")

s_mode = "null"
b_mode = "null"
p_mode = "null"

main_mode = "null"

while main_mode != "d" and main_mode != "c":
    main_mode = input("[d]\n[c]\nSelect overall settings: ")
    if main_mode != "d" and main_mode != "c":
        print("\n- Invalid answer -\n")

if main_mode == "c":
    while s_mode != "random" and s_mode != "set":
        s_mode = input("\n[random]\n[set]\nSelect a starting mode: ")
        if s_mode != "random" and s_mode != "set":
            print("\n- Invalid answer -\n")

    if s_mode == "set":
        strt_yco = float(input("[ Y-Coordinate ] strt_yco = "))
        strt_xco = float(input("[ X-Coordinate ] strt_xco = "))
        strt_dy = float(input("[ Y-Speed ] strt_dy = "))
        strt_dx = float(input("[ X-Speed ] strt_dx = "))

    while b_mode != "window" and b_mode != "box":
        b_mode = input("\n[window]\n[box]\nSelect a border mode: ")
        if b_mode != "window" and b_mode != "box":
            print("\n- Invalid answer -\n")

    if b_mode == "box":
        box_height = int(input("box_height = "))
        box_width = int(input("box_width = "))

    while p_mode != "default" and p_mode != "custom":
        p_mode = input("\n[default]\n[custom]\nSelect a physics mode: ")
        if p_mode != "default" and p_mode != "custom":
            print("\n- Invalid answer -\n")

    if p_mode == "custom":
        g = float(input("\n[ Gravity Value ] < Default : 0.3 >\ng = "))
        ekeep = float(input("\n[ Energy kept from bouncing ] < Default : -0.8 >\nekeep = "))
        efade = float(input("\n[ X-axis energy kept from soft-bounces/rolling ] < Default : 0.9 >\nefade = "))

elif main_mode == "d":
    s_mode = "random"
    b_mode = "window"
    p_mode = "default"

if p_mode == "default":
    g = 0.3 #Gravity Value
    ekeep = -0.8 #Energy loss and inversing from hard collision
    efade = 0.9 #Energy loss from constant soft collision

loop = 0

wn = Screen()
wn = title("Customizable Ball Physics Simulator")
wn = bgcolor("black")

if b_mode == "box":
    box = Turtle()
    box = color("green")
    box = setheading(0)
    box = speed(0)
    box = penup()
    box = goto(box_width/2,box_height/2)
    box = goto(box_width/2,box_height/-2)
    box = goto(box_width/-2,box_height/-2)
    box = goto(box_width/-2,box_height/2)
    box = goto(box_width/2,box_height/2)

ball = Turtle()
ball = shape("circle")
ball = color("white")
ball = width(10)
ball = setheading(0)
ball = speed(0)
ball = penup()
ball = showturtle()
ball = pensize(1)

while True:

    #Set Border Values
    if b_mode == "window":
        wn = Screen()
        floor = round(wn.window_height() / -2)
        walls = round(wn.window_width() / 2)
        
    if b_mode == "box":
        floor = box_height / -2
        walls = box_width / 2

    #Set Ball Starting Values
    if s_mode == "set":
        yco = strt_yco
        xco = strt_xco
        dy = strt_dy
        dx = strt_dx

    if s_mode == "random":
        yco = randrange(floor,floor*-1)
        xco = randrange(walls*-1,walls)
        dy = randrange(-20,20)
        dx = randrange(-40,40)
        
    ball = penup()

    if b_mode == "box":
        box = penup()
        box = goto(box_width/2,box_height/2)
        box = goto(box_width/2,box_height/-2)
        box = goto(box_width/-2,box_height/-2)
        box = goto(box_width/-2,box_height/2)
        box = goto(box_width/2,box_height/2)
    
    for loop in range(500):

        wn = Screen()

        #Window Calculations
        if b_mode == "window":
            floor = round(wn.window_height() / -2)
            walls = round(wn.window_width() / 2)
        
        #Ball Collision Detection + Calculation

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

        #Ball Position Calculations
        dy = round(dy,2)
        dx = round(dx,2)
        
        yco = yco + dy
        dy = dy - g
        xco = xco + dx
        dx = dx / 1.001

        #Ball Draw Position
        dyco = yco
        dxco = xco
        
        if floor - 21.4 <= yco <= floor + 21.4:
            dyco = floor + 20
            
        ball = goto(dxco, dyco)


