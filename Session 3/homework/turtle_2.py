from turtle import *

shape ("turtle")

speed (-1)

color = ["red", "blue", "brown", "yellow", "green"]

i = 3

for i in range (3, 7):

    for j in range (i):
        fillcolor (color[i-3])
        begin_fill()
        forward (100)
        left (360/i)
        end_fill()


    
    

mainloop()