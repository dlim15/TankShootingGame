
from tkinter import *
from MenuDisplay import *
import os

class GameScreen(BaseMenuDisplay):
    def start(self, levelNum):
        os.environ['SDL_WINDOWID'] = str(self.canvas.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        self.top.start_game(self.frame.winfo_screenwidth(), self.frame.winfo_screenheight(), levelNum)

    def create_widgets(self):
        self.title = Label(self.frame, text="Game Screen", font=("Arial", 24, "bold"))
        self.title.pack()
        self.title.place(x=1,y=1, width=200,height=30)
        self.back = Button(self.frame,anchor=E, text="Back", command = self.backToMain)
        self.back.pack()
        self.back.place(x=self.frame.winfo_screenwidth()/2,y=0, width=40,height=30)
        self.quit = Button(self.frame,anchor=E, text="X",font=("Arial", 20, "bold"), command = lambda:self.top.close())
        self.quit.pack()
        self.quit.place(x=self.frame.winfo_screenwidth()-39,y=0, width=35,height=30)
        self.addCanvas()

    def backToMain(self):
        self.top.top.attributes("-fullscreen",False)
        self.top.running = False
        self.top.show_frame(MainMenu)

    def addCanvas(self):
        self.canvas = Canvas(self.frame,width=self.frame.winfo_screenwidth(), height=self.frame.winfo_screenheight())
        self.canvas.pack(expand=1,fill=BOTH)
        self.canvas.place(x=0, y=30)
        # self.btnLeft = Button(self.canvas,text="<-", font=("Arial", 20, "bold"), command=self.moveLeft);
        # self.btnRight = Button(self.canvas,text="->", font=("Arial", 20, "bold"), command=self.moveRight);
        # self.btnLeft.pack()
        # self.btnRight.pack()
        # self.btnLeft.place(x=100,y=super().winfo_screenheight()*7/8, width=35,height=30)
        # self.btnRight.place(x=150,y=super().winfo_screenheight()*7/8, width=35,height=30)