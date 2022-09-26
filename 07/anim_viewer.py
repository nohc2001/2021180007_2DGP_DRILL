#0, 0, 50, 60 - 4
#50, 0, 50, 60 - 4
#110, 0, 60, 50 - 5
#162, 0, 43, 43 - 5
#218, 0, 38, 48 - 4
#276, 0, 48, 36 - 2
#276, 70, 48, 48 - 3
#344, 0, 32, 60 - 5
#385, 0, 50, 43 - 5

import pico2d;
import math;

pico2d.open_canvas(500, 500);
pico2d.clear_canvas();

sheetposList = [[0, 55, 50, 56, 4], [50, 55, 50, 55, 4], [110, 0, 50, 47, 5], [162, 64, 43, 43, 5], [218, 64, 38, 58, 4], [276, 65, 48, 48, 3],
    [344, 0, 40, 57, 5], [385, 65, 50, 43, 5]];
sheetup = 0;
frameup = 0;
img = pico2d.load_image("spriteSheet.png");
ftime = 0;
while(True):
    ftime += 1;
    frameup += 1;
    frameup = frameup % sheetposList[sheetup][4];
    pico2d.clear_canvas();
    img.clip_draw(sheetposList[sheetup][0], sheetposList[sheetup][1] + sheetposList[sheetup][3]*(frameup), sheetposList[sheetup][2], sheetposList[sheetup][3],
        200, 200, 300, 300);
    pico2d.update_canvas();
    pico2d.delay(0.3);
    if(ftime > 10):
        sheetup += 1;
        sheetup = sheetup % 7;
        frameup = 0;
        ftime = 0;
    pico2d.get_events();

pico2d.close_canvas();