import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



open_canvas(TUK_WIDTH, TUK_HEIGHT)

# fill here
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
handArrow = load_image('hand_arrow.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

handArrowPos = (0, 0);
prevPos = (0, 0);
def reset_world():
    global handArrowPos;
    global prevPos;
    handArrowPos = (random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT));
    prevPos = (random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT));

def get_distance(p1, p2):
    x1, y1 = p1;
    x2, y2 = p2;
    dx = x2-x1;
    dy = y2-y1;
    return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2));

def draw_line(p1, p2, flow):
    x1, y1 = p1;
    x2, y2 = p2;

    len = get_distance(p1, p2);
    lenint = int(len);
    margin = 1;

    if(lenint != 0 and flow < lenint/margin):
        rate = float(flow) / float(lenint/margin);
        x = (1.0-rate)*x1 + rate*x2;
        y = (1.0-rate)*y1 + rate*y2;
        return (x, y, 1);
        flow += 1;
    else:
        return (0, 0, 0);
    # fill here
    pass

playerx = 0;
playery = 0;
flow = 0;
dirx = 1;
def update_world():
    global dirx;
    global playery;
    global playerx;
    global flow;
    global handArrowPos;
    global prevPos;
    pos = draw_line(prevPos, handArrowPos, flow);
    flow += 1;
    if (pos == (0, 0, 0)):
        prevPos = handArrowPos;
        handArrowPos = (random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT));
        flow = 0;
    else:
        px, py, _ = pos;
        if(playerx - px > 0):
            dirx = 1;
        else:
            dirx = -1;
        playerx = px;

        playery = py;


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    update_world();

    hx, hy = handArrowPos;
    handArrow.draw(hx, hy, 100, 100);

    if(dirx == 1):
        character.clip_draw(frame * 100, 0, 100, 100, playerx, playery)
    else:
        character.clip_draw(frame * 100, 100*1, 100, 100, playerx, playery)
    update_canvas()

    frame = (frame + 1) % 8
    handle_events()

close_canvas()




