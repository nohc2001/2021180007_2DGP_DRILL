import math
import pico2d

pico2d.open_canvas(800, 600);
pico2d.clear_canvas_now()

def runCircle(x, y, radius):
    img = pico2d.load_image("image.png");
    i = 0;
    while(i < 360):
        degree = i * math.pi / 180;
        #pico2d.clear_canvas_now();
        img.draw_now(x + radius * math.cos(degree), y + radius * math.sin(degree), 10, 10); 
        i += 1;
        pico2d.delay(0.003);
    return;

def runRectangle(x, y, radius):
    img = pico2d.load_image("image.png");
    i = 0;
    while(i < 2*radius):
        #pico2d.clear_canvas_now();
        img.draw_now(x-radius + i, y-radius, 10, 10);
        img.draw_now(x-radius, y+radius-i, 10, 10);
        img.draw_now(x+radius, y-radius+i, 10, 10);
        img.draw_now(x+radius - i, y+radius, 10, 10);
        pico2d.delay(0.01);
        i += 1;
    return;

x = 0;
y = 300;
rad = 20;
while(x < 1000):
    x += 100;
    rad += 20;
    runCircle(x, y, rad);
    runRectangle(x, y, rad);

pico2d.close_canvas()