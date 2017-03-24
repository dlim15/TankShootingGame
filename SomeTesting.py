#!/usr/bin/python

from tkinter import *



def main():
    WIDTH = 1000
    HEIGHT = 1000
    top = Tk()
    top.geometry(str(WIDTH) + "x" + str(HEIGHT))

    canvas = Canvas(top, width = WIDTH, height = HEIGHT)
    canvas.pack()

    setUpMainMenu(top, canvas)
    setUpImage(top)
    top.mainloop()

def setUpMainMenu(top, canvas):
    top.wm_title("Tank Shooting Game")
    top.resizable(width=0, height=0)

    var = "Hello"
    lblName = Label(top, text=var, fg="black", bg="white")
    lblName.pack()
    lblName.place(x = 150, y = 50)

    def btnBClicked():
        lblName.config(text="Yolo!")

    btnClick = Button(canvas, text="click", command=btnBClicked)
    btnClick.place(x=150, y=100)
def setUpImage(top):

    imgTank = PhotoImage(file="tank.gif")
    lblTank = Label(top, image=imgTank)
    lblTank.image = imgTank
    lblTank.pack()
    lblTank.place(x=0,y=0)

if __name__ == "__main__":
    main()