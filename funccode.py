def add(a, b):
    return a+b;

print(add(10, 100));
print(add("no", "huncheul"));
print(add((1, 2, 3), (4, 5, 6)));
#print(add({1, 2, 3}, {4, 5, 6}));

def sumAndMul(a, b):
    return a+b, a*b;

x, y = sumAndMul(100, 3);
print((x, y));

x, _ = sumAndMul(100, 3);

import turtle

def draw_circle(x, y, r):
    turtle.penup();
    turtle.goto(x, y - r);
    turtle.pendown();
    turtle.circle(r);
    turtle.penup();
    turtle.goto(x, y);
    turtle.stamp();

turtle.shape("turtle");
draw_circle(0, 0, 50);
draw_circle(200, 200, 100);
draw_circle(100, -100, 50);

turtle.exitonclick();