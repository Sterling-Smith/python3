import turtle
wn = turtle.Screen()
wn.bgcolor("blue")

leo = turtle.Turtle()
leo.color("black")
leo.fillcolor("white")
leo.pensize(3) 

#bottom circle
numberSides = 50
radius = 100
armlength = 100
circumference = 2 * 3.14 * radius 
sideLength = circumference/numberSides
totalAngle = 360
turnAngle = totalAngle/numberSides
leo.begin_fill()
for i in range (numberSides):
    leo.forward(sideLength)
    leo.right(turnAngle)
leo.end_fill()

#middle circle
radius = 70
armstart = radius
diameter = 2 * radius
circumference = 2 * 3.14 * radius 
sideLength = circumference/numberSides
leo.begin_fill()
for i in range (numberSides):
    leo.forward(sideLength)
    leo.left(turnAngle)
leo.end_fill()
leo.up()

#go to center of the middle circle
leo.left(95)
leo.forward(radius)
leo.right(95)
leo.forward(armstart)
leo.down()

#draw hand
leo.forward(armlength)
leo.up()
leo.forward(5)

#back to center of circle
leftstart = armlength + armstart + armstart
leo.left(180)
leo.forward(leftstart-5)
leo.down()

leo.forward(armlength)
leo.up()
leo.right(180)
leo.forward(armlength+ armstart)
leo.left(95)
leo.forward(radius)
leo.right(90)
leo.down()

#top circle
radius = 40
circumference = 2 * 3.14 * radius 
sideLength = circumference/numberSides
leo.begin_fill()
for i in range (numberSides):
    leo.forward(sideLength)
    leo.left(turnAngle)
leo.end_fill()
leo.left(90)
leo.up()

#go to top part of the top circle 
leo.forward(radius+11)
leo.left(90)
leo.forward(2)
leo.down()

#draw the eyes and nose
leo.forward(3)
leo.up()
leo.backward(15)
leo.down()
leo.forward(3)
leo.up()
leo.left(90)
leo.forward(10)
leo.down()
leo.left(45)
leo.down()
leo.forward(12)
leo.forward(3)
leo.right(120)
leo.forward(10)
leo.up()
leo.forward(100)
wn.exitonclick()