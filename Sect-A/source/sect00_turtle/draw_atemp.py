# import turtle
#
# myPen = turtle.Turtle()
# myPen.speed(1)
# myPen.pensize(5)
# myPen.color("#FF0000")
#
# # print(2*360/5)
# for i in range (1,6):
#    # myPen.left(144)
#    myPen.left(2*360/5)
#    myPen.forward(200)
#
# turtle.done()


# import turtle
#
# myPen = turtle.Turtle()
# myPen.shape("turtle")
# myPen.speed(500090000000)
#
# myPen.color("red")
# myPen.circle(50)
#
# for i in range(1,10):
#     myPen.right(90)
#     myPen.left(45)
#     myPen.penup()
#     myPen.pendown()
#     myPen.goto(0,0)
#     myPen.circle(50)
#
# turtle.done()


import turtle

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")


for j in range (1,100):
  for i in range (1,6):
      myPen.left(144)
      myPen.forward(200)
  myPen.left(5)

turtle.done()


