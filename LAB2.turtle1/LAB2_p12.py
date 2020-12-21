import turtle as tr
tr.shape('turtle')
tr.speed(1000)
tr.penup()
tr.forward(-300)
tr.left(90)
tr.pendown()
N = 50
k = 0
R1 = 250
R2 = 50
def duga(R):
    for i in range(N):
        tr.forward(R / (2*N))
        tr.right(180 / N)
while k < 6:
    duga(R1)
    duga(R2)
    k += 1
    
        
