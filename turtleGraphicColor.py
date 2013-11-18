import turtle

bgColor = input("Please enter a background color:  ")
tessColor = input("Please enter a your tutles color:  ")
penWidth = int(input("How thick would you like the pen to be?  "))

window = turtle.Screen()
window.bgcolor(bgColor)

tess = turtle.Turtle()
tess.color(tessColor)
tess.pensize(penWidth)

tess.forward(50)
tess.left(120)
tess.forward(50)

window.exitonclick()