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
        self.quit = Button(self.topFrame,anchor=E, text="X",font=("Arial", 20, "bold"), command = lambda:self.top.close())
        self.quit.pack()
        self.quit.place(x=super().winfo_screenwidth()-39,y=0, width=35,height=30)
        self.addCanvas()
        self.addTank()
        # self.addKeyListenerToCanvas()

    def backToMain(self):
        self.top.attributes("-fullscreen",False)
        self.top.show_frame(MainMenu)



    def addCanvas(self):
        self.canvas = Canvas(self.topFrame,width=super().winfo_screenwidth(), height=super().winfo_screenheight())
        self.canvas.pack(expand=1,fill=BOTH)
        self.canvas.place(x=0, y=30)
        self.btnLeft = Button(self.canvas,text="<-", font=("Arial", 20, "bold"), command=self.moveLeft);
        self.btnRight = Button(self.canvas,text="->", font=("Arial", 20, "bold"), command=self.moveRight);
        self.btnLeft.pack()
        self.btnRight.pack()
        self.btnLeft.place(x=100,y=super().winfo_screenheight()*7/8, width=35,height=30)
        self.btnRight.place(x=150,y=super().winfo_screenheight()*7/8, width=35,height=30)

    def addTank(self):
        imgTank = PhotoImage(file="tank.gif")
        self.lblTank = Label(self.canvas, image=imgTank)
        self.lblTank.image = imgTank
        self.lblTank.pack()
        self.lblTank.place(x=0, y=super().winfo_screenheight()*2/3, width=200, height=104)
    def moveLeft(self):
        self.lblTank.place(x=self.lblTank.winfo_x()-10,y=self.lblTank.winfo_y())

    def moveRight(self):
        self.lblTank.place(x=self.lblTank.winfo_x()+10,y=self.lblTank.winfo_y())
        # self.canvas.move(self.lblTank,10,0)
    # @staticmethod
    # def leftKey(event):
    #     print("left clicked")
    # @staticmethod
    # def rightKey(event):
    #     print("right clicked")
    #
    # def addKeyListenerToCanvas(self):
    #     self.canvas.bind('<Left>',self.leftKey)
    #     self.canvas.bind('<Right>',self.rightKey)
    #     self.canvas.focus_set()

