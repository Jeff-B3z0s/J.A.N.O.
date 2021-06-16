# VARIABLES SECTION

import pygame as pg
import button
import shamrockMod
working = True

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


HomeBtn, WBtn, ScheduleBtn, AssistantBtn, ConfigBtn = 0, 0, 0, 0, 0
texts = ["Home", "Textbot", "Schedule", "Assistant Cmds", "Config"]
buttons = [HomeBtn, WBtn, ScheduleBtn, AssistantBtn, ConfigBtn]
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

whiteImg = pg.image.load('Assets/Images/Icons/Whiteboard.png')

icons = [calanderImg, configImg, homeImg, janoImg, whiteImg]


homeImg = pg.transform.smoothscale(homeImg, (43, 49))
whiteImg = pg.transform.smoothscale(whiteImg, (53, 36))
calanderImg = pg.transform.smoothscale(calanderImg, (50, 42))
janoImg = pg.transform.smoothscale(janoImg, (37, 48))
configImg = pg.transform.smoothscale(configImg, (41, 43))