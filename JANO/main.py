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

import Textbot
import button
import shamrockMod
import var
print(var.working)
from user import User



# MISC VARIABLES
global shamrockOn
global cursor
cursor = "pointer"
shamrockOn = False

nextChannel = "0"

# MENU LOOP ---------------------------------------------------#
def menu(screen):
    shamrockOn = False
    cursor = "pointer"
    user = 0
    loop = True
    btnClicked = "0_0"
    page = "0"
    while loop:

        # DISPLAY ---------------------------------------------#
        screen.fill("#131217")
        pg.draw.rect(screen, "#191A1F", pg.Rect(var.WINDOW_SIZE[0]-820, 0, 820, var.WINDOW_SIZE[1]), border_radius=5)
        pg.draw.line(screen, "#2A2E37", (616, 77), (760, 77), 5)
        pg.draw.circle(screen, (0,0,0), (var.WINDOW_SIZE[0] - 820 + 820//2, 440), 250, 16)

        # TITLE -----------------------------------------------#
        screen.blit(var.text, var.textRect)

        # TEXT AND ICON ---------------------------------------#

        for btn in var.buttons:
            btn.show(screen)
            btn.hover(pg.mouse.get_pos(), cursor)

        #IMAGES -----------------------------------------------#
        screen.blit(var.homeImg, (20, 100))
        screen.blit(var.whiteImg, (15, 165))
        screen.blit(var.calanderImg, (15, 225))
        screen.blit(var.janoImg, (20, 285))
        screen.blit(var.configImg, (23, 400))
        #screen.blit(notesImg, (20, 455))

        # DIVISION LINES --------------------------------------#

        pg.draw.line(screen, "#2A2E37", (10, 370), (270, 370), 5)
        pg.draw.line(screen, "#2A2E37", (10, 730), (270, 730), 5)
        screen.blit(var.jefe, var.jefeRect)


        # BIG IMAGES -------------------------------------------#
        screen.blit(var.shamrock, var.shamRect)
        screen.blit(var.powerBtn, var.powerRect)

        # CURSOR FUNCTIONS -------------------------------------#
        shamrockFunction = False
        if var.shamRect.collidepoint(pg.mouse.get_pos()) == 1:
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


        var.textBox.update(screen)



        # EVENT LOOP -------------------------------------------#

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            # MOUES CLICKING FUNCTIONS

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:


                for btn in var.buttons:
                    btnClicked = btn.click()
                    if btnClicked != "0_0":
                        page = btnClicked

                if page == "Home":
                    pass
                elif page == "Textbot":
                    Textbot.Textbot(screen)
                elif page == "Schedule":
                    Textbot.Schedule(screen)

                elif page == "Assistant Cmds":
                    Textbot.Assistant(screen)
                elif page == "Config":
                    Textbot.Config(screen)

                if shamrockFunction == True:
                    if shamrockOn == False:
                        shamrockMod.turnOn(var.textBox)
                        var.textBox.circleDefault = (100, 255, 100)
                        shamrockOn = True
                        #if user == 0:
                        #    user = shamrockMod.startProgram(user)

                    else:
                        shamrockMod.turnOff(var.textBox)
                        var.textBox.circleDefault = (0, 0, 0)
                        shamrockOn = False
                    var.textBox.circleColor = var.textBox.circleDefault
                if shamrockOn == True:
                    var.textBox.click(pg.mouse.get_pos())


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
menu(var.screen)

