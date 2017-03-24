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
        self.topFrame.pack(side=TOP,fill=X)

        self.title = Label(self.topFrame,anchor = N, text = "Tank Shooting Game", font = ("Arial", 24, "bold"))
        self.title.pack(fill=BOTH)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(fill = X)

        self.playButton = Button(self.buttonFrame, anchor = N, text = "Play Game", font=("Arial",24,"bold"), command = lambda: self.top.show_frame(PlayGameMenu))
        self.playButton.pack()

from GameDisplay import *

class PlayGameMenu(BaseMenuDisplay):
    def create_widgets(self):
        self.topFrame = Frame(self)
        self.topFrame.pack(side=TOP,fill=X)

        self.title = Label(self.topFrame, text="Play Game", font=("Arial", 24, "bold"))
        self.title.pack(side=LEFT,fill=Y)
        self.back = Button(self.topFrame,anchor=E, text="Back", command = lambda: self.top.show_frame(MainMenu))
        self.back.pack(side=RIGHT,fill=Y)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(fill=X)

        self.levelsButton = Button(self.buttonFrame, text="Levels", command = self.playGame)
        self.levelsButton.pack(side=LEFT,fill=Y,expand=True)

        self.sandboxButton = Button(self.buttonFrame, text="Sandbox",state=DISABLED)
        self.sandboxButton.pack(side = RIGHT,fill=Y,expand=True)
    def playGame(self):
        self.top.attributes("-fullscreen",True)
        self.top.show_frame(GameScreen)
