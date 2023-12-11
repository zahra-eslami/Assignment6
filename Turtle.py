from turtle import *

color=["red","purple","blue","green","yellow"]
n = 3
size = 100

shape("turtle")
speed(.5)
pensize(2)
penup()
goto(-50, 100)
pendown()

for i in range(5):
    degree = 360 / n
    for _ in range(n):
        pencolor(color[i])
        forward(size)
        right(degree)
    
    penup()  
    left(111)  
    forward(30)  
    right(111)  
    pendown()
    
    n += 1
    size += 19

done()
