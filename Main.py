#!/usr/bin/python

from tkinter import *
from MenuDisplay import *

class ApplicationGUI(Tk):
    def __init__(self, WIDTH, HEIGHT):
        Tk.__init__(self)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.wm_title("Tank Shooting Game")
        self.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.create_widgets()
        self.resizable(0, 0)
        self.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        self.destroy()

    def create_widgets(self):
        self.master = Frame(self)
        self.master.pack(side="top", fill="both", expand=True)
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.frames = {}
        for f in (MainMenu, PlayGameMenu):
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

    app.mainloop() #Forever Loops


if __name__ == "__main__":
    main()