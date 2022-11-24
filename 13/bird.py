from pico2d import *
import game_world
import game_framework
import random

class Bird:
    speed = 183;
    def __init__(self):
        self.flow = [0, 0.07];
        self.x, self.y = random.randint(100, 500), random.randint(300, 500);
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.flow[0] += game_framework.frame_time;
        if(self.flow[0] > self.flow[1]):
            self.frame = (self.frame+1) % 13;
            self.flow[0] -= self.flow[1];
        self.x += self.dir * Bird.speed * game_framework.frame_time;
        #self.x = clamp(25, self.x, 1600-25)

        if(self.x > 1600-25):
            self.dir = -1;
        if(self.x < 25):
            self.dir = 1;
        pass;

    def draw(self):
        wid = int(self.frame % 5);
        hei = int(self.frame / 5);
        if self.dir == -1:
            self.image.clip_composite_draw(wid*183, hei*168, 183, 168, 0, 'h', int(self.x), int(self.y), 100, 100);
            #self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            #0self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
            self.image.clip_composite_draw(wid*183, hei*168, 183, 168, 0, '', int(self.x), int(self.y), 100, 100);
        pass;

    def add_event(self, event):
        pass;

    def handle_event(self, event):
        pass;
