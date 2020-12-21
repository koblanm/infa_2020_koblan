import turtle as tr
import math
tr.color('black')
tr.speed(2)
tr.width(5)

A = 30
B = 15
inp = open('index.txt', 'r')
index = inp.read()
x = -200
y = 0
A1 = 0
A2 = 0
A3 = 0
A4 = 0
A5 = 0
A6 = 0
C = 0
K = 0
R = 0

tr.penup()
tr.goto(x, y)
tr.pendown()

for i in range(len(index)):

    A1 = (x, y)
    A2 = (x, y + A)
    A3 = (x, y + 2*A)
    A4 = (x + A, y + 2*A)
    A5 = (x + A, y + A)
    A6 = (x + A, y)
    C = (x + A + B, y)
    
    n = int(index[i])

    
    if n == 0:
        K = [A6, A4, A3, A1]
    elif n == 1:
        K = [0, A2, 1, A4, A6]
    elif n == 2:
        K = [A6, A1, A5, A4, A3]
    elif n == 3:
        K = [A5, A2, A4, A3]
    elif n == 4:
        K = [0, A6, 1, A4, A5, A2, A3]
    elif n == 5:
        K = [A6, A5, A2, A3, A4]
    elif n == 6:
        K = [A6, A5, A2, A1, A2, A4]
    elif n == 7:
        K = [A2, A4, A3]
    elif n == 8:
        K = [A6, A4, A3, A1, A2, A5]
    elif n == 9:
        K = [A5, A4, A3, A2, A5]
    else:
        print('?')

    for p in range(len(K)):
        if K[p] == 0:
            tr.penup()
        elif K[p] == 1:
            tr.pendown()
        else:
            tr.goto(K[p])
    tr.penup()
    tr.goto(C)
    tr.pendown()
    x += A + B
