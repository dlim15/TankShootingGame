#!/usr/bin/python

from tkinter import *
from MenuDisplay import *

class ApplicationGUI(Tk):
    def __init__(self, WIDTH, HEIGHT):
        Tk.__init__(self)
        self.wm_title("Tank Shooting Game")
        self.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.create_widgets()
        self.resizable(0, 0)

    def create_widgets(self):
        self.master = Frame(self)
        self.master.grid(row=0, column=0, sticky=W+E)
        self.frames = {}
        for f in (MainMenu, PlayGameMenu):
            frame = f(self.master, self)
            frame.grid(row=2, column=2, sticky=NW+SE)
            self.frames[f] = frame
        self.show_frame(MainMenu)
    def show_frame(self, cls):
        self.frames[cls].tkraise()

def main():
    WIDTH = 500
    HEIGHT = 400
    app = ApplicationGUI(WIDTH, HEIGHT)

    app.mainloop() #Forever Loops


if __name__ == "__main__":
    main()