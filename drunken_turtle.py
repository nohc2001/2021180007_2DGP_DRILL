import turtle
from random import *

turtle.reset();
turtle.speed(1);
turtle.shape("turtle");

def hit():
    turtle.speed(1000);
    turtle.left(randint(-100, 100));
    turtle.forward(50);
    turtle.speed(1);

movecount = 0;
turtle.onkey(hit, " ");
while(movecount < 100000000):
    turtle.listen();
    turtle.left(randint(-100, 100));
    turtle.forward(randint(0, 20));
    r = randint(0, 100);
    if(r < 10) :
        turtle.stamp(); 
    movecount += 1;

turtle.exitonclick();