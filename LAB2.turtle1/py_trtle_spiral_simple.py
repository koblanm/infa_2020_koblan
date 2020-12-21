import turtle as t
import math as m
t.shape('turtle')
t.speed(100)
Y = 0
dY = m.pi / 180
k = 20
N = 10 #обороты
A = N * (2 * m.pi)
while Y < A:
    y = k * Y * m.sin(Y)
    x = k * Y * m.cos(Y)
    t.goto(x , y)
    Y += dY
