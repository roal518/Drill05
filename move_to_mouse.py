from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
IDLE_character = load_image('Woodcutter_idle.png')
MOVE_character = load_image('Woodcutter_run.png')
Arrow_cursur = load_image('hand_arrow.png')

running = True
moving = False
mouseX = 0
mouseY = 0
isClicked = False
# handle_events--> keyboard // mouse
def handle_events():
    global running,moving
    global mouseX, mouseY, isClicked
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: # 창 닫기가 없긴 없다. ESC로 닫자
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == 1:
                isClicked = True
                move_character()
                mouseX,mouseY = event.x,TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button ==1:
                isClicked = False
def move_character():
    pass
idleframe = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    update_canvas()
    handle_events()
    delay(0.05)
close_canvas()