import game_framework
import pico2d

import os;
import sys;

os.chdir('C:\\Users\\nohc2\\Dev\\2021180007_2DGP_DRILL\\13');
sys.path.append(r'C:\\Users\\nohc2\\Dev\\2021180007_2DGP_DRILL\\13');

#os.chdir('C:\\Users\\TIP209-32\\Desktop\\2021180007_2DGP_DRILL\\13');
#sys.path.append(r'C:\\Users\\TIP209-32\\Desktop\\2021180007_2DGP_DRILL\\13');

import play_state

pico2d.open_canvas(1600, 600)
game_framework.run(play_state)
pico2d.close_canvas() 