import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for i in range(500): # this "for" loop will repeat these functions 500 times
    turtle.pencolor(colors[i % 6])
    turtle.width(i / 100 + 1)
    turtle.forward(i)
    turtle.left(91)

turtle.done()
