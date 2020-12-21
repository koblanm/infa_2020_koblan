import turtle as tr
tr.speed(1000)
tr.shape('turtle')
n = 10
tr.left(90)
def circle(y, x):
    N = 100
    for i in range(N):
        tr.forward(2.5 + x/2)
        tr.left((360 / N) * (-1)**y)
for k in range(n):
    circle(0, k)
    circle(1, k)
    
