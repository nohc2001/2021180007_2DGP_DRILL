import game_framework
import pico2d
import os;
import sys;

os.chdir('C:\\Users\\nohc2\\Dev\\2021180007_2DGP_DRILL\\12');
sys.path.append(r'C:\\Users\\nohc2\\Dev\\2021180007_2DGP_DRILL\\12');

import play_state

pico2d.open_canvas() 
game_framework.run(play_state)
pico2d.close_canvas()