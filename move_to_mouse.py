from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
IDLE_character = load_image('Woodcutter_idle.png')
MOVE_character = load_image('Woodcutter_run.png')
Arrow_cursur = load_image('hand_arrow')

running = True
moving = False
xdir = 0
ydir = 0
def handle_events():
    global running,moving
    global xdir, ydir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: # 창 닫기가 없긴 없다. ESC로 닫자
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

runframe = 0
idleframe = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    update_canvas()
    handle_events()

close_canvas()