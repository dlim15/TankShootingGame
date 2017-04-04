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
        self.topFrame = Frame(self, height = 200, pady = 25)
        self.topFrame.pack(side=TOP,fill=X)

        self.title = Label(self.topFrame,anchor = N, text = "Tank Shooting Game", font = ("Arial", 24, "bold"))
        self.title.pack(fill=BOTH)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(fill = BOTH, expand = True)

        self.playButton = Button(self.buttonFrame, anchor = N, text = " Play Game ", font=("Arial",24,"bold"), command = lambda: self.top.show_frame(PlayGameMenu), pady = 5)
        self.playButton.pack()

        self.instructionsButton = Button(self.buttonFrame, text = "Instructions", font=("Arial",24,"bold"), state=DISABLED, pady = 5)
        self.instructionsButton.pack()

        self.exitButton = Button(self.buttonFrame, text="    Exit    ", font=("Arial", 24, "bold"), command=lambda: self.top.close(), pady = 5)
        self.exitButton.pack()

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
        self.buttonFrame.pack(fill=BOTH, expand=True)

        self.levelsButton = Button(self.buttonFrame, text="Levels", command = lambda: self.top.show_frame(LevelSelectMenu))
        self.levelsButton.pack(side=LEFT,fill=BOTH, expand = True)

        self.sandboxButton = Button(self.buttonFrame, text="Sandbox",state=DISABLED)
        self.sandboxButton.pack(side = RIGHT,fill=BOTH, expand = True)

class LevelSelectMenu(BaseMenuDisplay):
    def create_widgets(self):
        self.topFrame = Frame(self)
        self.topFrame.pack(side=TOP, fill=X)

        self.title = Label(self.topFrame, text="Level Select", font=("Arial", 24, "bold"))
        self.title.pack(side=LEFT, fill=Y)
        self.back = Button(self.topFrame, anchor=E, text="Back", command=lambda: self.top.show_frame(PlayGameMenu))
        self.back.pack(side=RIGHT, fill=Y)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(fill=BOTH, expand=True)

        self.level1Button = Button(self.buttonFrame, text = "Level 1", font=("Arial", 24, "bold"), command=lambda:self.playGame(1))
        self.level1Button.grid(row = 0, padx = 10, pady=10)

        self.level2Button = Button(self.buttonFrame, text="Level 2",font=("Arial", 24, "bold"),  state=DISABLED)
        self.level2Button.grid(row = 0,column=1, padx = 10, pady=10)

        self.level3Button = Button(self.buttonFrame, text="Level 3",font=("Arial", 24, "bold"),  state=DISABLED)
        self.level3Button.grid(row = 0,column=2, padx = 10, pady=10)

        self.level4Button = Button(self.buttonFrame, text="Level 4", font=("Arial", 24, "bold"), state=DISABLED)
        self.level4Button.grid(row=1, padx=10, pady=10)

        self.level5Button = Button(self.buttonFrame, text="Level 5", font=("Arial", 24, "bold"), state=DISABLED)
        self.level5Button.grid(row=1, column=1, padx=10, pady=10)

        self.level6Button = Button(self.buttonFrame, text="Level 6", font=("Arial", 24, "bold"), state=DISABLED)
        self.level6Button.grid(row=1, column=2, padx=10, pady=10)

        self.level7Button = Button(self.buttonFrame, text="Level 7", font=("Arial", 24, "bold"), state=DISABLED)
        self.level7Button.grid(row=2, padx=10, pady=10)

        self.level8Button = Button(self.buttonFrame, text="Level 8", font=("Arial", 24, "bold"), state=DISABLED)
        self.level8Button.grid(row=2, column=1, padx=10, pady=10)

        self.level9Button = Button(self.buttonFrame, text="Level 9", font=("Arial", 24, "bold"), state=DISABLED)
        self.level9Button.grid(row=2, column=2, padx=10, pady=10)

    def playGame(self, levelNum):
        self.top.top.attributes("-fullscreen",True)
        self.top.show_frame(GameScreen)
        self.top.frames[GameScreen].start(levelNum)