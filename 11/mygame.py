import game_framework
from pico2d import *

os.chdir('C:\\Users\\nohc2\\Dev\\2021180007_2DGP_DRILL\\11');
sys.path.append(r'C:\\Users\\nohc2\\Dev\\2021180007_2DGP_DRILL\\11');

import play_state

pico2d.open_canvas()
game_framework.run(play_state)
pico2d.close_canvas();