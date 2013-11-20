import turtle

#turtle and size of line
def drawSquare(t, sz):
    """Make turtle t draw a square of the side sz."""

	for i in range(4):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()		#Set the window and it's attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()  	#creat alex
drawSquare(alex, 50)

wn.exitonclick()