from gtts import gTTS
import sys, os, math, time
import cv2
import trainingModel
import pygame as pg
import numpy as np
from pygame.locals import *
import playsound
import speech_recognition as sr
from gtts import gTTS
from user import User
import nltk
from nltk.stem.porter import PorterStemmer

pg.init()
pg.font.init()
clock = pg.time.Clock()

def turnOn(box):
    box.on = True

def turnOff(box):
    box.off = False

def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = f'Speech Output/voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


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
            else:
                trainingModel.process(input)


            self.circleColor = self.circleDefault
            pg.display.update()


def startProgram(user):
    speak("Welcome to the program.")
    name = "unknown"
    while True:
        speak("What is your name?")
        input = get_audio()
        speak(f'Is your name {input}? Please answer strictly with a yes or no. Im not that smart.')
        ans = get_audio()
        if ans.lower() == "yes":
            speak('nice.')
            name = input.lower()
            break
        elif ans.lower() == "no":
            speak('oh, let us try again')
        else:
            speak("sorry, I didn't quite get that. I'm kind of a really dumb program.")

    speak(f"welcome to Jano, {name}")
    return name
