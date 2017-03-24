#!/usr/bin/python

from tkinter import *
from MenuDisplay import *
from GameDisplay import *


class ApplicationGUI():
    def __init__(self, WIDTH, HEIGHT):
        self.top = Tk()
        self.top.rowconfigure(0,weight=1)
        self.top.columnconfigure(0,weight=1)
        self.top.wm_title("Tank Shooting Game")
        self.top.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.create_widgets()
        self.top.resizable(0, 0)
        self.top.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        self.top.destroy()

    def create_widgets(self):
        self.master = Frame(self.top)
        self.master.pack(side="top", fill="both", expand=True)
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.frames = {}
        for f in (MainMenu, PlayGameMenu, LevelSelectMenu, GameScreen):
            frame = f(self.master, self)
            frame.grid(row=0, column=0, sticky=N+W+S+E)
            self.frames[f] = frame
        self.show_frame(MainMenu)
    def show_frame(self, cls):
        self.frames[cls].tkraise()

def main():
    WIDTH = 500
    HEIGHT = 400
    app = ApplicationGUI(WIDTH, HEIGHT)

    app.top.mainloop() #Forever Loops


if __name__ == "__main__":
    main()