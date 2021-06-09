# Setup Python -----------------------------------------------#

import sys, os, math, time
import cv2
import pygame as pg
import numpy as np
from pygame.locals import *
pg.init()
pg.font.init()
clock = pg.time.Clock()


# Setup pygame/ Window ---------------------------------------#
WINDOW_SIZE = (1100, 800)
pg.display.set_caption("JANO")
screen = pg.display.set_mode(WINDOW_SIZE, 0, 64)

# FONTS ------------------------------------------------------#
font = pg.font.Font('Assets/Fonts/Coves Bold 700.otf', 32)
white = (255, 255, 255)

text = font.render('J A N O', True, white)
textRect = text.get_rect()
textRect.center = (WINDOW_SIZE[0] - 820 + 820//2, 50)

# TEXT -------------------------------------------------------#
home = font.render('Home', True, "#FFFFFF")
wb = font.render('Whiteboard', True, "#424B5C")
schedule = font.render('Schedule', True, "#424B5C")
assistant = font.render('Assistant', True, "#424B5C")
config = font.render('Config', True, "#424B5C")
notes = font.render('Notes', True, "#424B5C")

buttons = [home, wb, schedule, assistant, config, notes]

homeRect = home.get_rect()
wbRect = home.get_rect()
sRect = home.get_rect()
aRect = home.get_rect()
cRect = config.get_rect()
nRect = notes.get_rect()

jefe = font.render('Jefe', True, "#424B5C")
jefeRect = jefe.get_rect()
jefeRect.center = (140, 770)

# Assets -----------------------------------------------------#

shamrock = pg.image.load('Assets/Images/Shamrock.png')
shamrock = pg.transform.scale(shamrock, (260, 320))
shamRect = shamrock.get_rect()
shamRect.center = (WINDOW_SIZE[0] - 820 + 820//2, 440)

powerBtn = pg.image.load('Assets/Images/Power.png')
powerBtn = pg.transform.scale(powerBtn, (52, 62))
powerRect = powerBtn.get_rect()
powerRect.center = (WINDOW_SIZE[0] - 820 + 820//2, 410)

calanderImg = pg.image.load('Assets/Images/Icons/Calander.png')
configImg = pg.image.load('Assets/Images/Icons/Config.png')
homeImg = pg.image.load('Assets/Images/Icons/Home.png')
janoImg = pg.image.load('Assets/Images/Icons/Jano.png')
notesImg = pg.image.load('Assets/Images/Icons/Notes.png')
whiteImg = pg.image.load('Assets/Images/Icons/Whiteboard.png')

icons = [calanderImg, configImg, homeImg, janoImg, notesImg, whiteImg]


homeImg = pg.transform.smoothscale(homeImg, (43, 49))
whiteImg = pg.transform.smoothscale(whiteImg, (53, 36))
calanderImg = pg.transform.smoothscale(calanderImg, (50, 42))
janoImg = pg.transform.smoothscale(janoImg, (37, 48))
configImg = pg.transform.smoothscale(configImg, (41, 43))
notesImg = pg.transform.smoothscale(notesImg, (46, 59))

# MENU LOOP --------------------------------------------------#
def menu(screen):
    while True:
        pg.mouse.set_cursor(*pg.cursors.arrow)

        # DISPLAY --------------------------------------------#
        screen.fill("#131217")
        pg.draw.rect(screen, "#191A1F", pg.Rect(WINDOW_SIZE[0]-820, 0, 820, WINDOW_SIZE[1]), border_radius=5)
        pg.draw.line(screen, "#2A2E37", (616, 77), (760, 77), 5)
        pg.draw.circle(screen, (0,0,0), (WINDOW_SIZE[0] - 820 + 820//2, 440), 250, 16)

        # TITLE
        screen.blit(text, textRect)

        # TEXT AND ICON
        textX = 85
        screen.blit(home, (textX,110))
        screen.blit(homeImg, (20, 100))

        screen.blit(wb, (textX, 170))
        screen.blit(whiteImg, (15, 165))

        screen.blit(schedule, (textX, 230))
        screen.blit(calanderImg, (15, 225))

        screen.blit(assistant, (textX, 290))
        screen.blit(janoImg, (20, 285))

        screen.blit(config, (textX, 410))
        screen.blit(configImg, (23, 400))

        screen.blit(notes, (textX, 470))
        screen.blit(notesImg, (20, 455))

        # DIVISION LINES
        #pg.draw.line(screen, "#2A2E37", (10, 70), (270, 70), 5)
        pg.draw.line(screen, "#2A2E37", (10, 370), (270, 370), 5)
        pg.draw.line(screen, "#2A2E37", (10, 730), (270, 730), 5)
        screen.blit(jefe, jefeRect)


        # BIG IMAGES
        screen.blit(shamrock, shamRect)
        screen.blit(powerBtn, powerRect)



        # EVENT LOOP -----------------------------------------#

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                width, height = event.size
                if width < 400:
                    width = 400
                if height < 400:
                    height = 400
                screen = pg.display.set_mode((width, height), HWSURFACE | DOUBLEBUF ) # | RESIZABLE)

        pg.display.update()

        #Framerate
        clock.tick(60)


menu(screen)

