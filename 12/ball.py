from pico2d import *
import game_world

class Ball:
    image = None;

    def __init__(self, x=800, y=300, velocity=1) -> None:
        if(Ball.image == None):
            Ball.image = load_image('ball21x21.png');
        self.x, self.y, self.velocity = x, y, velocity;
        pass

    def draw(self):
        Ball.image.draw(self.x, self.y);
    
    def update(self):
        self.x += self.velocity;
        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self);