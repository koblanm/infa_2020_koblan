import turtle as tr
tr.speed(1000)
tr.shape('turtle')
n = 6
def circle():
    N = 100
    for i in range(N):
        tr.forward(5)
        tr.left(360 / N)
for k in range(n):
    circle()
    tr.left(360 / n)
    
