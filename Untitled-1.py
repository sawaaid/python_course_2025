
from turtle import *
colormode(255)
forward(120)
left(90)
color('red')
forward(80)
reset()
a = 0
b = 0
while b < 10:
    b = b + 1
    forward(20)
    left(30)
    color((b*10)%255, (b*60)%255, (b*30)%255)
    a = 0  # Reset a to 0 before the inner loop starts
    while a < 36:
        a = a + 1
        forward(10)
        left(10)
    