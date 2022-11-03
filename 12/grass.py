from pico2d import *

class Grass:
    def __init__(self, yyy):
        self.yy = yyy;
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, self.yy);

    def update(self):
        pass;