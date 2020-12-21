import turtle as tr
tr.shape('turtle')
tr.speed(1000)
n = 12
R = 80
k = 0
while k < n:
    tr.forward(R)
    tr.stamp()
    tr.right(180)
    tr.forward(R)
    tr.left(180 - 360/n)
    k += 1
    
