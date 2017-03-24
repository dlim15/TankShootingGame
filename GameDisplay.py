from MenuDisplay import *
from tkinter import *
class GameScreen(BaseMenuDisplay):
    def create_widgets(self):

        self.topFrame = Frame(self)
        self.topFrame.pack()

        self.topFrame.place(x=0,y=0,width=super().winfo_screenwidth(),height=super().winfo_screenheight())
        self.title = Label(self.topFrame, text="Game Screen", font=("Arial", 24, "bold"))
        self.title.pack()
        self.title.place(x=1,y=1, width=200,height=30)
        self.back = Button(self.topFrame,anchor=E, text="Back", command = self.backToMain)
        self.back.pack()
        self.back.place(x=super().winfo_screenwidth()/2,y=0, width=40,height=30)
        self.quit = Button(self.topFrame,anchor=E, text="X",font=("Arial", 20, "bold"), command = lambda:self.top.quit())
        self.quit.pack()
        self.quit.place(x=super().winfo_screenwidth()-39,y=0, width=35,height=30)
        self.addCanvas()
        self.addTank()

    def backToMain(self):
        self.top.attributes("-fullscreen",False)
        self.top.show_frame(MainMenu)

    def addCanvas(self):
        self.canvas = Canvas(self.topFrame)
        self.canvas.pack()
        self.canvas.place(x=0, y=30,width=super().winfo_screenwidth(), height=super().winfo_screenheight())

    def addTank(self):
        imgTank = PhotoImage(file="tank.gif")
        self.lblTank = Label(self.canvas, image=imgTank)
        self.lblTank.image = imgTank
        self.lblTank.pack()
        self.lblTank.place(x=0, y=super().winfo_screenheight()/3, width=200, height=104)
    #
    # def leftKey(self,event):
    #     self.lblTank.