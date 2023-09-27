from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
IDLE_character = load_image('Woodcutter_idle.png')
MOVE_character = load_image('Woodcutter_run.png')
Arrow_cursur = load_image('hand_arrow.png')

running = True
moving = False
mouseX = TUK_WIDTH//2
mouseY = TUK_HEIGHT//2
nowX, nowY = 0, 0
x, y = 0, 0
isClicked = False
# handle_events--> keyboard // mouse
def handle_events():
    global running, moving
    global mouseX, mouseY, isClicked
    global nowX,nowY
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == 1:
                isClicked = True
                nowX, nowY = mouseX, mouseY
                mouseX, mouseY = event.x, TUK_HEIGHT - 1 - event.y
                move_character()
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == 1:
                isClicked = False
def move_character():
    global x, y, nowX, nowY, mouseX, mouseY, i
    t = i / 100
    x = (1 - t) * nowX + t * mouseX
    y = (1 - t) * nowY + t * mouseY
    IDLE_character.clip_draw(idleframe * 100, 0, 100, 100, x, y)


idleframe = 0
i = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    Arrow_cursur.draw(mouseX, mouseY)
    if(i < 100):
        move_character()
        i += 1
    elif(i == 100):
        handle_events()
        i = 0
    update_canvas()

    idleframe = (idleframe + 1) % 4
    delay(0.05)
close_canvas()