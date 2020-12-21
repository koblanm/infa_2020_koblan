import turtle as tr
import math as m
tr.shape('turtle')
tr.speed(1000)
def star(N, L):
    if int(N/2) == (N/2):
        A = L * 2 * (m.sin(m.pi/N)**2)
        for i in range(N):
            tr.forward(L)
            tr.forward(A - L)
            tr.right(360/N)
        tr.forward(A)
        tr.left(180)
        for i in range(N):
            tr.forward(L)
            tr.forward(A - L)
            tr.left(360/N)
    else:
        A = L * 2 * (m.sin(m.pi/N)**2) / (1 + m.cos(m.pi/N))
        for i in range(N):
            tr.forward(L)
            tr.forward(A - L)
            tr.right(360/N)
        tr.forward(A)
        tr.left(180)
        for i in range(N):
            tr.forward(L)
            tr.forward(A - L)
            tr.left(360/N)
star(5, 100)
tr.penup()
tr.goto(-200, -35)
tr.pendown()
star(11, 100)
