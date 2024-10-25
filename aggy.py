import pygame as pg
import math,random,time
from PIL import Image
import keyboard
pg.init()

def text_centered(display, x, y, font, color, text):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    display.blit(text_surface, text_rect)

def display_gif_frame(screen, gif_path, frame_index,x,y,scale):
    gif = Image.open(gif_path)
    
    frame_index = frame_index % gif.n_frames
    gif.seek(frame_index)
    
    frame = gif.convert("RGBA")
    mode = frame.mode
    size = frame.size
    data = frame.tobytes()

    image = pg.image.fromstring(data, size, mode)
    image = pg.transform.scale(image,(80,80))
    # Display the frame
    screen.blit(image, (x,y))
    pg.display.flip()


displaysize = (pg.display.Info().current_w,pg.display.Info().current_h)
COLOR = "#006dae"
PI = math.pi
SYSRUNIMG = pg.transform.scale(pg.image.load("sysrun.png"),displaysize)

pg.mouse.set_visible(False)
display = pg.display.set_mode(displaysize)
FONT = pg.font.SysFont("Calibri",27)
completeness = 0


keyboard.block_key("alt")
keyboard.block_key("tab")



clock = pg.time.Clock()
dead = False
ium = 0
while not dead:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                quit()


    display.fill(COLOR)
    

    text_centered(display,displaysize[0]/2,displaysize[1]/2+20,FONT,"white",f"Working on updates  {completeness}% complete.")
    text_centered(display,displaysize[0]/2,displaysize[1]/2+35+20,FONT,"white",f"Don't turn off your PC. This will take a while.")
    text_centered(display,displaysize[0]/2,displaysize[1]-55,FONT,"white",f"Your PC may restart several times")
    display_gif_frame(display, "windows-loandig-cargando.gif", ium,displaysize[0]/2-40,displaysize[1]/2-90,1)
    
    pg.display.flip()

    ium += 1
    clock.tick(30)
    if random.random()> 0.993:
        completeness += 1
    elif random.random() > 0.991:
        completeness = 0
        q = 0
        while q < 600:
            q += random.choice([1,2])
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        quit()

            display.fill((0,0,0))
            if q > 60:
                display.blit(SYSRUNIMG,(0,0))
                display_gif_frame(display, "windows-loandig-cargando.gif", ium,displaysize[0]/2-40,displaysize[1]-240,0.8)
            pg.display.flip()
            ium += 1
            clock.tick(30)






















