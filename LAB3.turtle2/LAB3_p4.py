from random import randint
import turtle as tr
#system variables
Number_of_particles = 5
dt = 0.05
t = 0
TimeMAX = 100
n = 0
Border_right = 300
Border_left = -300
Border_up = 300
Border_down = -300
Vmax = 70
ax = 0
ay = 0

#Shorter names of var:
N = Number_of_particles
BR = Border_right
BL = Border_left
BU = Border_up
BD = Border_down


#Speed and Position massives
SpX = [0] * N
SpY = [0] * N

PoX = [0] * N
PoY = [0] * N

#Drawing borders
tr.penup()
tr.speed(1000)
tr.goto(BL, BD)
tr.pendown()
tr.goto(BL, BU)
tr.goto(BR, BU)
tr.goto(BR, BD)
tr.goto(BL, BD)
tr.penup()

#Particles creation
pool = [tr.Turtle(shape='circle')  for i in range(N)]
for unit in pool:
    unit.speed(10000)
    unit.color('white')
    unit.shapesize(0.5)
    SpX[n] = randint((-1)*Vmax, Vmax)
    SpY[n] = randint((-1)*Vmax, Vmax)
    unit.right(randint(-180,180))
    unit.penup()
    x = randint(BL, BR)
    y = randint(BD, BU)
    unit.goto(int(x), int(y))
    PoX[n] = x
    PoY[n] = y
    n += 1
for unit in pool:
    unit.color('black')
n = 0

#Process
while t < TimeMAX:
    for unit in pool:
        #Move
        PoX[n] += SpX[n] * dt
        PoY[n] += SpY[n] * dt
        unit.goto(int(PoX[n]), int(PoY[n]))
        
        #Borders
        if PoX[n] > BR:
            SpX[n] *= -1
        if PoY[n] > BU:
            SpY[n] *= -1
        if PoX[n] < BL:
            SpX[n] *= -1
        if PoY[n] < BD:
            SpY[n] *= -1

       

        n += 1
        
    n = 0
    t += dt 


