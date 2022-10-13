from pico2d import *
import game_framework
import play_state

running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('add_delete_boy.png')
    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    play_state.update();
    # fill here
    pass

def draw():
    clear_canvas()
    play_state.drawWorlds();
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state();
                case pico2d.SDLK_PLUS:
                    play_state.boy.append(play_state.Boy());
                case pico2d.SDLK_q:
                    play_state.boy.append(play_state.Boy());
                case pico2d.SDLK_MINUS:
                    if(len(play_state.boy) > 1):
                        play_state.boy.pop();
                case pico2d.SDLK_w:
                    if(len(play_state.boy) > 1):
                        play_state.boy.pop();





