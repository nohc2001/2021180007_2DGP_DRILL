import turtle;

turtle.reset()

index = 0;
while (index < 6):
    turtle.penup();
    turtle.goto(-200 + index * 100, -200);
    turtle.pendown();
    turtle.goto(-200 + index * 100, 300);
    index += 1;

index = 0;
while (index < 6):
    turtle.penup();
    turtle.goto(-200, -200 + index * 100);
    turtle.pendown();
    turtle.goto(300, -200 + index * 100);
    index += 1;

turtle.exitonclick()
