from pico2d import *
import random
TUK_WIDTH, TUK_HEIGHT = 1280,1024
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
x, y = mouseX, mouseY
isClicked = False
# handle_events--> keyboard // mouse
def keyboard_events():
    global running
    keyevents = get_events()
    for keyevent in get_events():
        if keyevent.type == SDL_KEYDOWN:
            if keyevent.key == SDLK_ESCAPE:
                running = False



def move_character():
    global x, y, nowX, nowY, mouseX, mouseY, i
    global moving
    if(x == mouseX and y == mouseY):
        nowX, nowY = mouseX, mouseY
        moving = False
    elif (x != mouseX and y != mouseY):
        moving = True
        t = i / 100
        x = (1 - t) * nowX + t * mouseX
        y = (1 - t) * nowY + t * mouseY
        if(nowX<mouseX):
            MOVE_character.clip_draw(runframe * 100, 0, 100, 100, x, y)
        elif(nowX>mouseX):
            MOVE_character.clip_composite_draw(runframe * 100, 0, 100, 100, 0, 'h', x, y, 100, 100)
def random_move():
    global mouseX, mouseY
    global moving
    moving = True
    mouseX = random.randint(0,1280)
    mouseY = random.randint(120,904)

runframe = 0
idleframe = 0
i = 0
index = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    Arrow_cursur.draw(mouseX, mouseY)
    if(moving):
        move_character()
        i += 2
    else:
        i = 0
        random_move()
        IDLE_character.clip_draw(idleframe * 100, 0, 100, 100, x, y)
    keyboard_events()
    update_canvas()
    runframe = (runframe + 1) % 6
    idleframe = (idleframe + 1) % 4
    delay(0.05)

close_canvas()