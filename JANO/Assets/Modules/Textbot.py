from gtts import gTTS
import sys, os, math, time
import pygame as pg
import numpy as np
from pygame.locals import *
import shamrockMod
import trainingModel

pg.init()
pg.font.init()
clock = pg.time.Clock()

import var

global loop
loop = True
global output_text
output_text = "bruh"
def respond(inp, output_text):
    print(inp)

    inp.lower()
    if inp == "hello":

        output_text = "Hi there!"
    else:
        inp = trainingModel.process(inp)
        output, tag = trainingModel.respondB(inp, trainingModel.intents)
        output_text = output
    return output_text


def Textbot(screen):
    tColor = (255, 255, 255)
    user_text = 'type here...'
    output_text = "I'll respond here!\nAsk me anything."
    loop = True
    cursor = "pointer"
    btnClicked = "0_0"
    page = "0"
    active = False
    while loop == True:

        if active == True:
            tColor = (255, 255, 255)
        else:
            tColor = (50, 50, 50)
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


        # TEXTBOX --------------------------------------------#


        outputBox = pg.Rect(var.WINDOW_SIZE[0] - 820 + 30, 75, 760, 600)
        pg.draw.rect(screen, "#212027", outputBox)

        outputText = var.font.render(output_text, True, (255, 255, 255))
        outputTextRect = pg.Rect(var.WINDOW_SIZE[0] - 820 + 45, 85, 760, 600)

        screen.blit(outputText, outputTextRect)

        textbox = pg.Rect(var.WINDOW_SIZE[0] - 820 + 30, 725, 760, 50)
        pg.draw.rect(screen, "#212027", textbox)

        text = var.font.render(user_text, True, tColor)

        textRect = pg.Rect(var.WINDOW_SIZE[0] - 785, 730, 760, 50)
        screen.blit(text, textRect)

        # EVENT LOOP -------------------------------------------#

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            # MOUES CLICKING FUNCTIONS

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                page = "0"
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

                if textbox.collidepoint(pg.mouse.get_pos()) == 1:
                    if active == True:
                        active = False
                    else:
                        active = True

            if event.type == pg.KEYDOWN:

                # Check for backspace
                if active == True:
                    if event.key == pg.K_BACKSPACE:

                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]

                    # Unicode standard is used for string
                    # formation
                    elif event.key == pg.K_RETURN:
                        output_text = respond(user_text, output_text)
                        user_text = ''
                    else:
                        user_text += event.unicode




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
        text = var.font.render('COMMANDS - INCOMPLETE', True, (255, 255, 255))
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

                page = "0"
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

                page = "0"
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
        text = var.font.render('SCHEDULE - INCOMPLETE', True, (255, 255, 255))
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

                page = "0"
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



