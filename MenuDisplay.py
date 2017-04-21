from tkinter import *

class BaseMenuDisplay():
    def __init__(self, masterFrame, top):
        self.frame = Frame(masterFrame)
        self.top = top
        self.frame.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the frame."""
        raise NotImplementedError

class MainMenu(BaseMenuDisplay):
    def create_widgets(self):
        self.topFrame = Frame(self.frame,bg ="black", height = 200, pady = 25)
        self.topFrame.pack(side=TOP,fill=X)

        self.title = Label(self.topFrame,anchor = N,bg ="blue",foreground = "white", text = "Tank Shooting Game", font = ("Arial", 24, "bold"))
        self.title.pack(fill=BOTH)

        self.buttonFrame = Frame(self.frame,bg = "black")
        self.buttonFrame.pack(fill = BOTH, expand = True)

        self.playButton = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", anchor = N, text = " Play Game ", font=("Arial",24,"bold"), command = lambda: self.top.show_frame(LevelSelectMenu))
        self.playButton.pack(padx = 10,pady = 10)

        self.instructionsButton = Button(self.buttonFrame,bg = "blue",relief = "groove", bd = 10, foreground = "white", text = "Instructions", font=("Arial",24,"bold"), command = lambda: self.top.show_frame(InstructionsMenu))
        self.instructionsButton.pack(padx = 10, pady = 10)

        self.exitButton = Button(self.buttonFrame, bg ="blue",relief = "groove", bd = 10, foreground = "white", text="    Exit    ", font=("Arial", 24, "bold"), command=lambda: self.top.close())
        self.exitButton.pack(padx = 10, pady = 10)

from GameDisplay import *

class PlayGameMenu(BaseMenuDisplay):
    def create_widgets(self):
        self.topFrame = Frame(self.frame,bg ="blue")
        self.topFrame.pack(side=TOP,fill=X)

        self.title = Label(self.topFrame, bg= "blue",foreground = "white", text="  Play Game", font=("Arial", 24, "bold"))
        self.title.pack(side=LEFT,fill=Y)
        self.back = Button(self.topFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white",  font=("Arial", 12, "bold"),anchor=E, text="Back", command = lambda: self.top.show_frame(MainMenu))
        self.back.pack(side=RIGHT,fill=Y)

        self.buttonFrame = Frame(self.frame, bg = "black",)
        self.buttonFrame.pack(fill=BOTH, expand=True)

        self.levelsButton = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Levels",  font=("Arial", 24, "bold"), command = lambda: self.top.show_frame(LevelSelectMenu))
        self.levelsButton.pack(side=LEFT,fill=BOTH, expand = True, padx = 10, pady=30)

        self.sandboxButton = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Sandbox", font=("Arial", 24, "bold"), state=DISABLED)
        self.sandboxButton.pack(side = RIGHT,fill=BOTH, expand = True, padx = 10, pady=30)

class InstructionsMenu(BaseMenuDisplay):
    def create_widgets(self):
        self.topFrame = Frame(self.frame,bg = "blue")
        self.topFrame.pack(side=TOP,fill=X)

        self.title = Label(self.topFrame,bg="blue",foreground="white", text="  Instructions", font=("Arial", 24, "bold"))
        self.title.pack(side=LEFT)
        self.back = Button(self.topFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white",  font=("Arial", 12, "bold"),anchor=E, text="Back", command = lambda: self.top.show_frame(LevelSelectMenu))
        self.back.pack(side=RIGHT,fill=Y)

        self.outerFrame = Frame(self.frame,bg = "blue",bd = 20,relief ="sunken")
        self.outerFrame.pack(fill=BOTH,expand=True)
        self.instructionFrame = Frame(self.outerFrame,bg="black")
        self.instructionFrame.pack(fill=BOTH, expand = True)

        self.instructions = Label(self.instructionFrame,bg ="black",foreground ="white", text="\n\n\n1) Press left and right arrow keys to move tank\n"
                                                              "2) Move mouse to aim tank trajectory\n"
                                                              "3) Click to increase the force of the projectile\n"
                                                              "4) Release mouse to launch", font=("Arial", 14, "bold"),justify = "left")
        self.instructions.pack(side = TOP, fill =X)

class LevelSelectMenu(BaseMenuDisplay):
    def create_widgets(self):
        self.topFrame = Frame(self.frame,bg = "blue")
        self.topFrame.pack(side=TOP, fill=X)

        self.title = Label(self.topFrame,bg="blue",foreground = "white", text="  Level Select", font=("Arial", 24, "bold"))
        self.title.pack(side=LEFT, fill=Y)
        self.back = Button(self.topFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white",  font=("Arial", 12, "bold"), anchor=E, text="Back", command=lambda: self.top.show_frame(MainMenu))
        self.back.pack(side=RIGHT, fill=Y)

        self.buttonFrame = Frame(self.frame,bg = "black")
        self.buttonFrame.pack(fill=BOTH, expand=True)

        self.level1Button = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text = "Level 1", font=("Arial", 24, "bold"), command=lambda:self.playGame(1))
        self.level1Button.grid(row = 0, padx = 5, pady=10)

        self.level2Button = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Level 2",font=("Arial", 24, "bold"),  state=DISABLED)
        self.level2Button.grid(row = 0,column=1, padx = 5, pady=10)

        self.level3Button = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Level 3",font=("Arial", 24, "bold"),  state=DISABLED)
        self.level3Button.grid(row = 0,column=2, padx = 5, pady=10)

        self.level4Button = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Level 4", font=("Arial", 24, "bold"), state=DISABLED)
        self.level4Button.grid(row=1, padx=5, pady=10)

        self.level5Button = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Level 5", font=("Arial", 24, "bold"), state=DISABLED)
        self.level5Button.grid(row=1, column=1, padx=5, pady=10)

        self.level6Button = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Level 6", font=("Arial", 24, "bold"), state=DISABLED)
        self.level6Button.grid(row=1, column=2, padx=5, pady=10)

        self.level7Button = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Level 7", font=("Arial", 24, "bold"), state=DISABLED)
        self.level7Button.grid(row=2, padx=5, pady=10)

        self.level8Button = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Level 8", font=("Arial", 24, "bold"), state=DISABLED)
        self.level8Button.grid(row=2, column=1, padx=5, pady=10)

        self.level9Button = Button(self.buttonFrame,bg ="blue",relief = "groove",bd = 10, foreground ="white", text="Level 9", font=("Arial", 24, "bold"), state=DISABLED)
        self.level9Button.grid(row=2, column=2, padx=5, pady=10)

    def playGame(self, levelNum):
        self.top.top.wm_attributes("-fullscreen",True)
        self.top.show_frame(GameScreen)
        self.top.frames[GameScreen].start(levelNum)