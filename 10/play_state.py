from pico2d import *
import game_framework
import logo_state
import item_state
import adboy_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1 # 오른쪽
        self.image = load_image('animation_sheet.png')
        self.ball_image = load_image('ball21x21.png');
        self.big_ball_image = load_image('ball41x41.png');
        self.item = None;

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2
        if self.x > 800:
            self.x = 800
            self.dir = -1 #왼쪽
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        
        if(self.item == 'ball'):
            self.ball_image.draw(self.x+10, self.y+50);
        elif(self.item == 'bigball'):
            self.big_ball_image.draw(self.x+10, self.y+50);




def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit();
            if(event.key == SDLK_i):
                game_framework.push_state(item_state);
            if(event.key == SDLK_b):
                game_framework.push_state(adboy_state);

boy = [] # c로 따지믄 NULL
grass = None
running = True

# 초기화
def enter():
    global boy, grass, running
    boy.append(Boy())
    grass = Grass()
    running = True

# finalization code
def exit():
    global boy, grass
    index = 0;
    while(index < len(boy)):
        del boy[index];
        index += 1;
    pass
    del boy;
    del grass

def update():
    index = 0;
    while(index < len(boy)):
        boy[index].update();
        index += 1;

def draw():
    clear_canvas()
    drawWorlds();
    update_canvas()

def drawWorlds():
    grass.draw()
    index = 0;
    while(index < len(boy)):
        boy[index].draw();
        index += 1;
    pass

def pause():
    pass;

def resume():
    pass;




