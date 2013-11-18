import turtle

def drawMulticolorSquare(t, sz):
	"""Make turtle t draw a multi-color square of sz."""

	for i in['red', 'purple', 'hotpink', 'blue']:
		t.color(i)
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

size = 20						#size of the smallest square
for i in range(15):
	drawMulticolorSquare(tess, size)
	size = size + 10			#increase the size for next time
	tess.forward(10)			#move tess along a little
	tess.right(18)				#give her some extra turn

wn.exitonclick()