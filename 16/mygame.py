import os
import sys
import game_framework
import pico2d

os.chdir('C:\\Users\\nohc2\\Dev\\2021180007_2DGP_DRILL\\16');
sys.path.append(r'C:\\Users\\nohc2\\Dev\\2021180007_2DGP_DRILL\\16');

import play_state

# pico2d.open_canvas(400, 300)
pico2d.open_canvas(1000, 1000)
game_framework.run(play_state)
pico2d.close_canvas()