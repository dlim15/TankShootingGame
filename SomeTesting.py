#!/usr/bin/python

from tkinter import *



def main():
    WIDTH = 1000
    HEIGHT = 1000
    top = Tk()
    top.geometry(str(WIDTH) + "x" + str(HEIGHT))
    frame = Frame(top, width=WIDTH, height = HEIGHT)
    frame.pack()

    canvas = Canvas(frame, width = WIDTH, height = HEIGHT)
    canvas.pack()

    setUpMainMenu(top, canvas)
    addKeyListenerToCanvas(canvas)
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

def addKeyListenerToCanvas(canvas):
    def leftKey(event):
        print("left clicked")
    def rightKey(event):
        print("right clicked")
    canvas.bind('<Left>',leftKey)
    canvas.bind('<Right>',rightKey)
    canvas.focus_set()


if __name__ == "__main__":
    main()