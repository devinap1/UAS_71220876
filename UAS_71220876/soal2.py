import turtle
s = turtle.Screen()

t = turtle.Turtle()
s.bgcolor( "pink" )

#drawring gambar
t.fillcolor("yellow")
t.begin_fill()
for i in range (6):
    t.left(90)
t.forward(180)
t.right(45)
t.forward(30)
t.right(45)
t.forward(180)
t.right(45)
t.forward(30)
t.right(45)
t.forward(180)
t.right(45)
t.forward(30)
t.right(45)
t.forward(180)
t.right(45)
t.forward(30)
t.end_fill()
t.right(90)
t.penup()
t.forward(120)
t.pendown()
t.right(90)
t.circle(-45,360)

turtle.done()