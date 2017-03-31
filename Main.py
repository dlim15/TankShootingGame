#!/usr/bin/python

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


    def start_game(self, WIDTH, HEIGHT):
        #pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        #pymunk
        self.space = pymunk.Space()

        #### TEMPORARY ####
        self.screen.fill((255,255,255))
        pygame.draw.circle(self.screen, (0, 0, 0), (250, 250), 125)
        self.space.gravity = (0.0,-900.0)


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