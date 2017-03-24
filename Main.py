#!/usr/bin/python

from tkinter import *
import MenuDisplay

def main():
    WIDTH = 300
    HEIGHT = 200
    top = Tk()
    top.geometry(str(WIDTH) + "x" + str(HEIGHT))
    top.wm_title("Tank Shooting Game")
    top.resizable(width=0, height=0)

    setUpMainMenu(top)

    top.mainloop() #Forever Loops

def setUpMainMenu(top):
    lblName = Label(top, text="Yolo!", fg="black", bg="white")
    lblName.pack()
    lblName.place(x=150, y=50)

if __name__ == "__main__":
    main()