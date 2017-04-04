#!/usr/bin/python
from GameClasses import *
from tkinter import *
from MenuDisplay import *
from GameDisplay import *
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util
import sys

class ApplicationGUI():
    def __init__(self, WIDTH, HEIGHT):
        self.running = False
        self.clock = pygame.time.Clock()
        self.frameRate = 60
        self.start_root(WIDTH, HEIGHT)
        self.create_widgets(MainMenu)

    def close(self):
        self.end_gameplay()
        self.top.destroy()

    def create_widgets(self, menu):
        self.master = Frame(self.top)
        self.master.pack(side="top", fill="both", expand=True)
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.frames = {}
        for f in (MainMenu, PlayGameMenu, LevelSelectMenu, GameScreen):
            frame = f(self.master, self)
            frame.grid(row=0, column=0, sticky=N+W+S+E)
            self.frames[f] = frame
        self.show_frame(menu)
    def show_frame(self, cls):
        self.frames[cls].tkraise()

    def start_root(self, WIDTH, HEIGHT):
        self.top = Tk()
        self.top.rowconfigure(0, weight=1)
        self.top.columnconfigure(0, weight=1)
        self.top.wm_title("Tank Shooting Game")
        self.top.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.top.resizable(0, 0)
        self.top.protocol("WM_DELETE_WINDOW", self.close)

    def end_gameplay(self):
        pygame.quit()
        self.running = False
        self.space = None


    def start_game(self, WIDTH, HEIGHT, level_to_play):
        #pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))

        #pymunk
        self.space = pymunk.Space()

        #### TEMPORARY ####
        #Load levels
        i = 1
        for level in (Level, Level):
            if i == level_to_play:
                self.level=level(WIDTH,HEIGHT, self.space, self.screen)
                break
            i += 1


    def run(self):
        while True:
            fps = 60
            dt = 1. / fps
            if self.running:
                self.space.step(dt)
                pygame.display.update()

            self.top.update_idletasks()
            self.top.update()
            self.clock.tick(fps)


def main():
    WIDTH = 500
    HEIGHT = 400
    app = ApplicationGUI(WIDTH, HEIGHT)

    app.run() #Forever Loops


if __name__ == "__main__":
    main()