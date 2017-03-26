#!/usr/bin/python

from tkinter import *
from MenuDisplay import *
from GameDisplay import *
import pygame
import sys


class ApplicationGUI():
    def __init__(self, WIDTH, HEIGHT):
        self.running = True
        self.frameRate = 60
        self.clock = pygame.time.Clock()
        self.start_root(WIDTH, HEIGHT)
        self.create_widgets(MainMenu)

    def close(self):
        self.running = False
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

    def run(self):
        while self.running:
            fps = 60
            dt = 1. / fps
            #space.step(dt) TODO

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