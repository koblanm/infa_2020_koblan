import turtle
turtle.shape('turtle')
turtle.color('green')
turtle.speed(1000)

A0 = -20
A = 20
for x in range(10):
    for i in range(4):
        turtle.forward(A)
        turtle.left(90)
    turtle.penup()
    turtle.forward(A0/2)
    turtle.left(90)
    turtle.forward(A0/2)
    turtle.right(90)
    A -= A0
    turtle.pendown()

