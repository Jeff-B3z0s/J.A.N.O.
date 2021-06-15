from gtts import gTTS
import sys, os, math, time
import pygame as pg
import numpy as np
from pygame.locals import *

pg.init()
pg.font.init()
clock = pg.time.Clock()

import var

global loop
loop = True


def Textbot(screen):
    loop = True
    cursor = "pointer"
    btnClicked = "0_0"
    page = "0"
    while loop == True:

        # DISPLAY ---------------------------------------------#
        screen.fill("#131217")
        pg.draw.rect(screen, "#191A1F", pg.Rect(var.WINDOW_SIZE[0] - 820, 0, 820, var.WINDOW_SIZE[1]), border_radius=5)
        pg.draw.line(screen, "#2A2E37", (616, 77), (760, 77), 5)

        # TITLE -----------------------------------------------#
        text = var.font.render('TEXBOT', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (var.WINDOW_SIZE[0] - 820 + 820 // 2, 50)
        screen.blit(text, textRect)

        # TEXT AND ICON ---------------------------------------#

        for btn in var.buttons:
            btn.show(screen)
            btn.hover(pg.mouse.get_pos(), cursor)

        # IMAGES -----------------------------------------------#
        screen.blit(var.homeImg, (20, 100))
        screen.blit(var.whiteImg, (15, 165))
        screen.blit(var.calanderImg, (15, 225))
        screen.blit(var.janoImg, (20, 285))
        screen.blit(var.configImg, (23, 400))
        # screen.blit(notesImg, (20, 455))

        # DIVISION LINES --------------------------------------#

        pg.draw.line(screen, "#2A2E37", (10, 370), (270, 370), 5)
        pg.draw.line(screen, "#2A2E37", (10, 730), (270, 730), 5)
        screen.blit(var.jefe, var.jefeRect)

        # CURSOR FUNCTIONS -------------------------------------#

        if cursor == "diamond":
            pg.mouse.set_cursor(*pg.cursors.diamond)
        elif cursor == "pointer":
            pg.mouse.set_cursor(*pg.cursors.arrow)
        else:
            pg.mouse.set_cursor(*pg.cursors.arrow)

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
                    loop = False
                elif page == "Textbot":
                    pass
                elif page == "Schedule":
                    loop = False
                    Schedule(screen)

                elif page == "Assistant Cmds":
                    loop = False
                    Assistant(screen)
                elif page == "Config":
                    loop = False
                    Config(screen)



            elif event.type == VIDEORESIZE:
                width, height = event.size
                if width < 400:
                    width = 400
                if height < 400:
                    height = 400
                screen = pg.display.set_mode((width, height), HWSURFACE | DOUBLEBUF)  # | RESIZABLE

        pg.display.update()

        # Framerate
        clock.tick(60)
    print(loop)



def Assistant(screen):

    loop = True
    cursor = "pointer"
    btnClicked = "0_0"
    page = "0"
    while loop == True:

        # DISPLAY ---------------------------------------------#
        screen.fill("#131217")
        pg.draw.rect(screen, "#191A1F", pg.Rect(var.WINDOW_SIZE[0] - 820, 0, 820, var.WINDOW_SIZE[1]), border_radius=5)
        pg.draw.line(screen, "#2A2E37", (616, 77), (760, 77), 5)


        # TITLE -----------------------------------------------#
        text = var.font.render('COMMANDS', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (var.WINDOW_SIZE[0] - 820 + 820 // 2, 50)
        screen.blit(text, textRect)

        # TEXT AND ICON ---------------------------------------#

        for btn in var.buttons:
            btn.show(screen)
            btn.hover(pg.mouse.get_pos(), cursor)

        # IMAGES -----------------------------------------------#
        screen.blit(var.homeImg, (20, 100))
        screen.blit(var.whiteImg, (15, 165))
        screen.blit(var.calanderImg, (15, 225))
        screen.blit(var.janoImg, (20, 285))
        screen.blit(var.configImg, (23, 400))
        # screen.blit(notesImg, (20, 455))

        # DIVISION LINES --------------------------------------#

        pg.draw.line(screen, "#2A2E37", (10, 370), (270, 370), 5)
        pg.draw.line(screen, "#2A2E37", (10, 730), (270, 730), 5)
        screen.blit(var.jefe, var.jefeRect)


        # CURSOR FUNCTIONS -------------------------------------#



        if cursor == "diamond":
            pg.mouse.set_cursor(*pg.cursors.diamond)
        elif cursor == "pointer":
            pg.mouse.set_cursor(*pg.cursors.arrow)
        else:
            pg.mouse.set_cursor(*pg.cursors.arrow)


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
                    loop = False
                elif page == "Textbot":
                    loop = False
                    Textbot(screen)
                elif page == "Schedule":
                    pass

                elif page == "Assistant Cmds":
                    loop = False
                    Assistant(screen)
                elif page == "Config":
                    loop = False
                    Config(screen)



            elif event.type == VIDEORESIZE:
                width, height = event.size
                if width < 400:
                    width = 400
                if height < 400:
                    height = 400
                screen = pg.display.set_mode((width, height), HWSURFACE | DOUBLEBUF)  # | RESIZABLE


        pg.display.update()

        # Framerate
        clock.tick(60)
    print(loop)


def Config(screen):

    loop = True
    cursor = "pointer"
    btnClicked = "0_0"
    page = "0"
    while loop == True:

        # DISPLAY ---------------------------------------------#
        screen.fill("#131217")
        pg.draw.rect(screen, "#191A1F", pg.Rect(var.WINDOW_SIZE[0] - 820, 0, 820, var.WINDOW_SIZE[1]), border_radius=5)
        pg.draw.line(screen, "#2A2E37", (616, 77), (760, 77), 5)


        # TITLE -----------------------------------------------#
        text = var.font.render('CONFIGURATION', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (var.WINDOW_SIZE[0] - 820 + 820 // 2, 50)
        screen.blit(text, textRect)

        # TEXT AND ICON ---------------------------------------#

        for btn in var.buttons:
            btn.show(screen)
            btn.hover(pg.mouse.get_pos(), cursor)

        # IMAGES -----------------------------------------------#
        screen.blit(var.homeImg, (20, 100))
        screen.blit(var.whiteImg, (15, 165))
        screen.blit(var.calanderImg, (15, 225))
        screen.blit(var.janoImg, (20, 285))
        screen.blit(var.configImg, (23, 400))
        # screen.blit(notesImg, (20, 455))

        # DIVISION LINES --------------------------------------#

        pg.draw.line(screen, "#2A2E37", (10, 370), (270, 370), 5)
        pg.draw.line(screen, "#2A2E37", (10, 730), (270, 730), 5)
        screen.blit(var.jefe, var.jefeRect)


        # CURSOR FUNCTIONS -------------------------------------#



        if cursor == "diamond":
            pg.mouse.set_cursor(*pg.cursors.diamond)
        elif cursor == "pointer":
            pg.mouse.set_cursor(*pg.cursors.arrow)
        else:
            pg.mouse.set_cursor(*pg.cursors.arrow)


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
                    loop = False
                elif page == "Textbot":
                    loop = False
                    Textbot(screen)
                elif page == "Schedule":
                    pass

                elif page == "Assistant Cmds":
                    loop = False
                    Assistant(screen)
                elif page == "Config":
                    loop = False
                    Config(screen)



            elif event.type == VIDEORESIZE:
                width, height = event.size
                if width < 400:
                    width = 400
                if height < 400:
                    height = 400
                screen = pg.display.set_mode((width, height), HWSURFACE | DOUBLEBUF)  # | RESIZABLE


        pg.display.update()

        # Framerate
        clock.tick(60)
    print(loop)




def Schedule(screen):

    loop = True
    cursor = "pointer"
    btnClicked = "0_0"
    page = "0"
    while loop == True:

        # DISPLAY ---------------------------------------------#
        screen.fill("#131217")
        pg.draw.rect(screen, "#191A1F", pg.Rect(var.WINDOW_SIZE[0] - 820, 0, 820, var.WINDOW_SIZE[1]), border_radius=5)
        pg.draw.line(screen, "#2A2E37", (616, 77), (760, 77), 5)


        # TITLE -----------------------------------------------#
        text = var.font.render('SCHEDULE', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (var.WINDOW_SIZE[0] - 820 + 820 // 2, 50)
        screen.blit(text, textRect)

        # TEXT AND ICON ---------------------------------------#

        for btn in var.buttons:
            btn.show(screen)
            btn.hover(pg.mouse.get_pos(), cursor)

        # IMAGES -----------------------------------------------#
        screen.blit(var.homeImg, (20, 100))
        screen.blit(var.whiteImg, (15, 165))
        screen.blit(var.calanderImg, (15, 225))
        screen.blit(var.janoImg, (20, 285))
        screen.blit(var.configImg, (23, 400))
        # screen.blit(notesImg, (20, 455))

        # DIVISION LINES --------------------------------------#

        pg.draw.line(screen, "#2A2E37", (10, 370), (270, 370), 5)
        pg.draw.line(screen, "#2A2E37", (10, 730), (270, 730), 5)
        screen.blit(var.jefe, var.jefeRect)


        # CURSOR FUNCTIONS -------------------------------------#



        if cursor == "diamond":
            pg.mouse.set_cursor(*pg.cursors.diamond)
        elif cursor == "pointer":
            pg.mouse.set_cursor(*pg.cursors.arrow)
        else:
            pg.mouse.set_cursor(*pg.cursors.arrow)


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
                    loop = False
                elif page == "Textbot":
                    loop = False
                    Textbot(screen)
                elif page == "Schedule":
                    pass

                elif page == "Assistant Cmds":
                    loop = False
                    Assistant(screen)
                elif page == "Config":
                    loop = False
                    Config(screen)



            elif event.type == VIDEORESIZE:
                width, height = event.size
                if width < 400:
                    width = 400
                if height < 400:
                    height = 400
                screen = pg.display.set_mode((width, height), HWSURFACE | DOUBLEBUF)  # | RESIZABLE


        pg.display.update()

        # Framerate
        clock.tick(60)
    print(loop)


