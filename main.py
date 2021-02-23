########## INDIAN FLAG #############

import turtle
a=turtle.Turtle()

a.speed(100)


# For Ashoka chakra
for i in range(24):  #Range is  24 for as there is 24 lines in Ashoka chakra
    a.forward(50)
    a.penup()
    a.setposition(0,0)
    a.pendown()
    a.left(15)


a.setposition(0,-51)
a.circle(52)
a.penup()





# For the orange part of flag
a.setposition(-500, 150)
a.pendown()
a.fillcolor("orange")
a.begin_fill()
a.forward(1000)
a.left(90)
a.forward(300)
a.left(90)
a.forward(1000)
a.left(90)
a.forward(300)
a.end_fill()
a.penup()


#For Green part of flag

a.setposition(-500,-150)
a.pendown()
a.fillcolor("green")
a.begin_fill()
a.right(270)
a.forward(1000)
a.right(90)
a.forward(300)
a.right(90)
a.forward(1000)
a.right(90)
a.forward(300)
a.end_fill()

turtle.done()