# Setup Python -----------------------------------------------#
from gtts import gTTS
import sys, os, math, time
import cv2
import pygame as pg
import numpy as np
from pygame.locals import *
import playsound
import speech_recognition as sr
from gtts import gTTS

pg.init()
pg.font.init()
clock = pg.time.Clock()

sys.path.insert(1, 'Assets/Modules')

import button
import shamrockMod
from user import User


# Setup pygame/ Window ---------------------------------------#
WINDOW_SIZE = (1100, 800)
pg.display.set_caption("Jano")
screen = pg.display.set_mode(WINDOW_SIZE, 0, 64)

# FONTS ------------------------------------------------------#
font = pg.font.Font('Assets/Fonts/Coves Bold 700.otf', 32)
white = (255, 255, 255)

text = font.render('J A N O', True, white)
textRect = text.get_rect()
textRect.center = (WINDOW_SIZE[0] - 820 + 820//2, 50)

# TEXT -------------------------------------------------------#


HomeBtn, WBtn, ScheduleBtn, AssistantBtn, ConfigBtn, NotesBtn = 0, 0, 0, 0, 0, 0
texts = ["Home", "Whiteboard", "Schedule", "Assistant Cmds", "Config", "Notes"]
buttons = [HomeBtn, WBtn, ScheduleBtn, AssistantBtn, ConfigBtn, NotesBtn]
yCords = [110, 170, 230, 290, 410, 470]
chosen = [True, False, False, False, False, False]

for i in range(len(texts)):
    buttons[i] = button.Button(texts[i], 80, yCords[i], "#424B5C", font, chosen[i])




jefe = font.render('Jefe', True, "#424B5C")
jefeRect = jefe.get_rect()
jefeRect.center = (140, 770)

# TEXTBOX ----------------------------------------------------#

#pg.draw.rect(screen, "#212027", pg.Rect(WINDOW_SIZE[0] - 820 + 30, 725, 820 - 60, 50))
#pg.draw.circle(screen, (0, 0, 0), (WINDOW_SIZE[0] - 820 + 55, 750), 20, 0)
textBox = shamrockMod.textBox("...", WINDOW_SIZE[0] - 820 + 30, 725, 760, 50, "#FFFFFF", "#212027", font)
textBox.update(screen)


# ASSETS -----------------------------------------------------#

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


# MISC VARIABLES
global shamrockOn
global cursor
cursor = "pointer"
shamrockOn = False


# MENU LOOP ---------------------------------------------------#
def menu(screen):
    shamrockOn = False
    cursor = "pointer"
    user = 0
    while True:

        # DISPLAY ---------------------------------------------#
        screen.fill("#131217")
        pg.draw.rect(screen, "#191A1F", pg.Rect(WINDOW_SIZE[0]-820, 0, 820, WINDOW_SIZE[1]), border_radius=5)
        pg.draw.line(screen, "#2A2E37", (616, 77), (760, 77), 5)
        pg.draw.circle(screen, (0,0,0), (WINDOW_SIZE[0] - 820 + 820//2, 440), 250, 16)

        # TITLE -----------------------------------------------#
        screen.blit(text, textRect)

        # TEXT AND ICON ---------------------------------------#

        for btn in buttons:
            btn.show(screen)
            btn.hover(pg.mouse.get_pos(), cursor)

        #IMAGES -----------------------------------------------#
        screen.blit(homeImg, (20, 100))
        screen.blit(whiteImg, (15, 165))
        screen.blit(calanderImg, (15, 225))
        screen.blit(janoImg, (20, 285))
        screen.blit(configImg, (23, 400))
        screen.blit(notesImg, (20, 455))

        # DIVISION LINES --------------------------------------#

        pg.draw.line(screen, "#2A2E37", (10, 370), (270, 370), 5)
        pg.draw.line(screen, "#2A2E37", (10, 730), (270, 730), 5)
        screen.blit(jefe, jefeRect)


        # BIG IMAGES -------------------------------------------#
        screen.blit(shamrock, shamRect)
        screen.blit(powerBtn, powerRect)

        # CURSOR FUNCTIONS -------------------------------------#
        shamrockFunction = False
        if shamRect.collidepoint(pg.mouse.get_pos()) == 1:
            cursor = "diamond"
            shamrockFunction = True
        else:
            cursor = "pointer"

        if cursor == "diamond":
            pg.mouse.set_cursor(*pg.cursors.diamond)
        elif cursor == "pointer":
            pg.mouse.set_cursor(*pg.cursors.arrow)
        else:
            pg.mouse.set_cursor(*pg.cursors.arrow)


        # TEXT BOX ---------------------------------------------#


        textBox.update(screen)



        # EVENT LOOP -------------------------------------------#

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            # MOUES CLICKING FUNCTIONS
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                for btn in buttons:
                    btn.click()
                if shamrockFunction == True:
                    if shamrockOn == False:
                        shamrockMod.turnOn(textBox)
                        textBox.circleDefault = (100, 255, 100)
                        shamrockOn = True
                        #if user == 0:
                        #    user = shamrockMod.startProgram(user)

                    else:
                        shamrockMod.turnOff(textBox)
                        textBox.circleDefault = (0, 0, 0)
                        shamrockOn = False
                    textBox.circleColor = textBox.circleDefault
                if shamrockOn == True:
                    textBox.click(pg.mouse.get_pos())


            elif event.type == VIDEORESIZE:
                width, height = event.size
                if width < 400:
                    width = 400
                if height < 400:
                    height = 400
                screen = pg.display.set_mode((width, height), HWSURFACE | DOUBLEBUF ) # | RESIZABLE

        pg.display.update()

        #Framerate
        clock.tick(60)


shamrockOn = False
menu(screen)

