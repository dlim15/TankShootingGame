from tkinter import *

class BaseMenuDisplay(Frame):
    def __init__(self, masterFrame, top):
        Frame.__init__(self, masterFrame)
        self.top = top
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the frame."""
        raise NotImplementedError

class MainMenu(BaseMenuDisplay):
    def create_widgets(self):
        self.topFrame = Frame(self, height = 200)
        self.topFrame.grid()

        self.title = Label(self.topFrame, text = "Tank Shooting Game", font = ("Arial", 24, "bold"))
        self.title.grid(sticky=W+E)

        self.buttonFrame = Frame(self)
        self.buttonFrame.grid()

        self.playButton = Button(self.buttonFrame, text = "Play Game", font=("Arial",24,"bold"), command = lambda: self.top.show_frame(PlayGameMenu))
        self.playButton.grid(sticky=W+E)

class PlayGameMenu(BaseMenuDisplay):
    def create_widgets(self):
        self.topFrame = Frame(self)
        self.topFrame.grid()

        self.title = Label(self.topFrame, text="Play Game", font=("Arial", 24, "bold"))
        self.title.grid(sticky=W)
        self.back = Button(self.topFrame,anchor=E, text="Back", command = lambda: self.top.show_frame(MainMenu))
        self.back.grid(column = 1, row = 0, sticky=E)

        self.buttonFrame = Frame(self)
        self.buttonFrame.grid()

        self.levelsButton = Button(self.buttonFrame, text="Levels")
        self.levelsButton.grid(column = 0, row = 1, sticky=N+S)

        self.sandboxButton = Button(self.buttonFrame, text="Sandbox",state=DISABLED)
        self.sandboxButton.grid(column = 1, row = 1,sticky=N+S)