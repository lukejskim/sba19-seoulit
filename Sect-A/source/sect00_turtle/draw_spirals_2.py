# draw_spirals_2
import turtle

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")

side=20
myPen.penup()
myPen.goto(0,0) #position cursor at the bootom right of the screen
myPen.pendown()

for i in range (1,50):
  myPen.forward(side)
  myPen.left(92)
  side=side+7


myPen.penup()
myPen.goto(500,500)

#Start Spiral
#for i in range (1,20):
#  for j in range (0,4):
#      myPen.forward(side)
#      myPen.left(90)
#  myPen.left(20)
#  side=side+5

turtle.done()