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

def turnOn(box):
    box.on = True

def turnOff(box):
    box.off = False

def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "Speech Output/voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        audio = r.listen(src)
        said = ""
        try:
            said = r.recognize_google(audio)
            #print(said)
        except Exception as e:
            print("Exception : " + str(e))

    return said

class textBox():
    def __init__(self, text, x, y, w, h, tColor, rColor, font):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tColor = tColor
        self.rColor = rColor
        self.font = font
        self.display = font.render(self.text, True, self.tColor)
        self.rect = 0
        self.circle = 0
        self.circleColor = (0, 0, 0)
        self.circleDefault = (0, 0, 0)
        self.on = False


    def draw(self, screen):
        self.screen = screen
        self.rect = pg.draw.rect(screen, self.rColor, pg.Rect(self.x, self.y, self.w, self.h))
        self.circle = pg.draw.circle(screen, self.circleColor, (self.x + 25, self.y + 25), 20, 0)
        screen.blit(self.display, (self.x + 60, self.y + 5))


    def update(self, screen):
        self.draw(screen)

    def click(self, mousePos):
        if self.circle.collidepoint(mousePos):
            self.circleColor = (255, 50, 255)
            self.update(self.screen)
            pg.display.update()

            input = get_audio()
            self.text = input
            self.display = self.font.render(self.text, True, self.tColor)



            if input == "hello":
                self.circleColor = (255, 100, 100)
                pg.display.update()
                speak("Hi!")
                self.text = "Hi!"
                self.display = self.font.render(self.text, True, self.tColor)

            self.circleColor = self.circleDefault
            pg.display.update()

