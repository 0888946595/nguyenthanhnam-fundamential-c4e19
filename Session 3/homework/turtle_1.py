from turtle import *

shape ("turtle")

color = ["red", "blue", "brown", "yellow", "silver"]
speed (-1)
i = 2
for i in range (0, len(color[i])):
    for j in range (2):
        fillcolor (color[i])
        begin_fill ()
        forward (60)
        left (90)
        forward (80)
        left (90)
        end_fill ()
    forward (60)
mainloop ()
