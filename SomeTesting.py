#!/usr/bin/python

from tkinter import *

def main():

    top = Tk()
    top.geometry("300x200")


    var = StringVar()
    var.set("Hello")
    lblName = Label(top, textvariable=var)
    lblName.pack()
    def btnBClicked():
        var.set("Yolo!")



    btnClick = Button(top, text="click", command=btnBClicked)
    btnClick.place(x=150,y=100)



    top.mainloop()