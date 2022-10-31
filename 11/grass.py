from pico2d import *

class Grass:
    image = None;
    def __init__(self):
        Grass.image = load_image('grass.png')

    def draw(self):
        Grass.image.draw(400, 30)