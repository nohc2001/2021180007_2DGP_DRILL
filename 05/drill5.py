import turtle
import sys
turtle.shape("turtle");

def goup():
    turtle.setheading(90)
    turtle.forward(100)
    turtle.stamp();

def godown():
    turtle.setheading(-90)
    turtle.forward(100)
    turtle.stamp();

def goleft():
    turtle.setheading(180)
    turtle.forward(100)
    turtle.stamp();

def goright():
    turtle.setheading(0)
    turtle.forward(100)
    turtle.stamp();

def excgo():
    sys.exit();

turtle.onkey(goup, 'w')
turtle.onkey(godown, 's')
turtle.onkey(goleft, 'a')
turtle.onkey(goright, 'd')
turtle.onkey(excgo, "Escape")

turtle.stamp();

turtle.listen()
turtle.exitonclick()