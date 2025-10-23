import turtle

t = turtle.Turtle()
t.speed(-30000000)
t.pensize(2)
turtle.bgcolor("navyblue")

colors = ["red", "yellow"]
for i in range(7600):
    t.color(colors[i % 2]) 
    t.circle(100)
    t.right(10)

turtle.done()
