import math
import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    # fill here
    x1, y1 = p1;
    x2, y2 = p2;

    draw_big_point(p1);
    draw_big_point(p2);

    a = (y2-y1) / (x2-x1);
    b = y1 - a * x1;

    minx = 0;
    maxx = 0;
    if(x1 > x2):
        minx = x2;
        maxx = x1;
    else:
        minx = x1;
        maxx = x2;

    for x in range(minx, maxx+1, 5):
        y = a*x+b;
        draw_point((x, y));
    pass


def get_distance(p1, p2):
    x1, y1 = p1;
    x2, y2 = p2;
    dx = x2-x1;
    dy = y2-y1;
    return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2));

def draw_line(p1, p2):
    x1, y1 = p1;
    x2, y2 = p2;
    flow = 0;

    draw_big_point(p1);
    draw_big_point(p2);

    len = get_distance(p1, p2);
    lenint = int(len);
    margin = 10;

    while(lenint != 0 and flow < lenint/margin):
        rate = float(flow) / float(lenint/margin);
        x = (1.0-rate)*x1 + rate*x2;
        y = (1.0-rate)*y1 + rate*y2;
        draw_point((x, y));
        flow += 1;
    # fill here
    pass

def draw_line_strip(*arg):
    arglen = len(arg);
    index = 0;
    while(index < arglen-1):
        pos1 = arg[index];
        pos2 = arg[index+1];
        draw_line(pos1, pos2);
        index+=1;

def draw_line_loop(*arg):
    arglen = len(arg);
    index = 0;
    while(index < arglen-1):
        pos1 = arg[index];
        pos2 = arg[index+1];
        draw_line(pos1, pos2);
        index += 1;

    pos1 = arg[index];
    pos2 = arg[0];
    draw_line(pos1, pos2);

prepare_turtle_canvas()

# fill here
draw_line_loop((100, 200), (-50, -120), (20, 100), (-300, -100), (200, -300), (300, 200));

turtle.done()