'''绘制太阳花案例'''
import turtle

turtle.color("red","yellow")
turtle.speed(10)

i = 1
turtle.begin_fill()
while i<=50:
    turtle.fd(200)
    turtle.right(170)
    i=i+1
turtle.end_fill()

turtle.done()