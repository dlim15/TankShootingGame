#!/usr/bin/python
import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="How to play\n"
                                   "1)Press the left and right buttons to move\n"
                                   "2)Press up and down to aim\n"
                                   "3)Press and hold the charge button to set the force used\n"
                                   "4)Release to shoot", justify = "left")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       lvl1 = tk.Button(self, width = 5, height = 5, text = "Level 1")
       lvl1.grid(row =0, column =0)
       lvl2 = tk.Button(self, width=5, height=5, text="Level 2")
       lvl2.grid(row =0, column =1)
       lvl3 = tk.Button(self, width=5, height=5, text="Level 3")
       lvl3.grid(row =0, column =2)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Instructions", command=p1.lift)
        b2 = tk.Button(buttonframe, text="levels", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Play", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    root.title("Tank Shooting Game")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()