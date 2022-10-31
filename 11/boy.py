from pico2d import *
import game_framework

class IDLE:
    @staticmethod
    def enter(self, event):
        self.timer = 100;
        if event == RD:
            self.dir += 1
        elif(event == LD):
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1;
        pass

    @staticmethod
    def exit(self):
        print('EXIT IDLE');
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8;
        self.timer -= 1;
        print(self.timer);
        if self.timer <= 0:
            self.add_event(TIMER);
            self.timer == 0;
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            Boy.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            Boy.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

class RUN:
    def enter(self, event):
        if event == RD:
            self.dir += 1
        elif(event == LD):
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1;
        pass

    def exit(self):
        self.face_dir = self.dir;
        print('EXIT RUN');
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8;
        self.x += self.dir;
        pass

    def draw(self):
        if self.dir == -1:
            Boy.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            Boy.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class SLEEP:
    def enter(self, event):
        print("ENTER SLEEP");
        self.frame = 0;
        pass;
    
    def exit(self):
        pass;
    
    def do(self):
        self.frame = (self.frame + 1) % 8;
        pass;
    
    def draw(self):
        print("DRAW SLEEP");
        if(self.face_dir == -1):
            self.image.clip_composite_draw(self.frame*100, 200, 100, 100, -3.141592/2, '', self.x + 25, self.y - 25, 100, 100);
        else:
            self.image.clip_composite_draw(self.frame*100, 300, 100, 100, 3.141592/2, '', self.x - 25, self.y - 25, 100, 100);

class AUTORUN:
    def enter(self, event):
        print("ENTER AUTORUN");
        self.frame = 0;
        self.dir = 1;
        pass;
    
    def exit(self):
        print('EXIT AUTORUN');
        pass;
    
    def do(self):
        self.frame = (self.frame + 1) % 8;
        self.x += self.dir;
        if(self.x <= 0 or self.x > 800):
            self.dir *= -1;
        pass;
    
    def draw(self):
        print("DRAW AUTORUN");
        if self.dir == -1:
            Boy.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            Boy.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

RD, LD, RU, LU, TIMER, AK = range(6);
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYDOWN, SDLK_a) : AK
}

table = {
    "SLEEP" : {"HIT": "WAKE"},
    "WAKE" : {"TIMER10": "SLEEP"},
}

next_state = {
    IDLE:{RU:RUN, LU:RUN, RD:RUN, LD:RUN, TIMER:SLEEP, AK:AUTORUN},
    RUN:{RU:IDLE, LU:IDLE, LD:IDLE, RD:IDLE, AK:AUTORUN},
    SLEEP:{RU:RUN, LU:RUN, LD:RUN, RD:RUN, AK:AUTORUN},
    AUTORUN:{RU:RUN, LU:RUN, LD:RUN, RD:RUN, AK:IDLE}
}

class Boy:
    image = None;
    def __init__(self):
        self.timer = 0;
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        if(Boy.image == None):
            Boy.image = load_image('animation_sheet.png');
        
        self.event_que = [];
        self.cur_state = IDLE;
        self.cur_state.enter(self, None);

    def update(self):
        '''self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        self.x = clamp(0, self.x, 800)'''
        self.cur_state.do(self);

        if(self.event_que):
            event = self.event_que.pop();
            self.cur_state.exit(self);
            self.cur_state = next_state[self.cur_state][event];
            self.cur_state.enter(self, event);

    def draw(self):
        self.cur_state.draw(self);
        '''if self.dir == -1:
            Boy.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            Boy.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            if self.face_dir == 1:
                Boy.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                Boy.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)'''
    
    def add_event(self, event):
        self.event_que.insert(0, event);
        pass

    def handle_events(self, event):
        if(event.type, event.key) in key_event_table :
            key_event = key_event_table[(event.type, event.key)];
            self.add_event(key_event);
        
        
        