import turtle

turtle.reset()
turtle.speed(1000);
index = 0
while (index < 101):
    turtle.penup()
    turtle.goto(-200 + index * 5, -200)
    turtle.pendown()
    turtle.goto(-200 + index * 5, 300)
    index += 1

index = 0
while (index < 101):
    turtle.penup()
    turtle.goto(-200, -200 + index * 5)
    turtle.pendown()
    turtle.goto(300, -200 + index * 5)
    index += 1

turtle.exitonclick()
