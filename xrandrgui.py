#!/usr/bin/env python
'''
xrandrgui

This file provides a simple way to change the settings on a linux machine using xrandr.  It
provides access to only the most basic settings.
'''
from tkinter import *

root = Tk()
root.geometry("370x200+30+30")
w = Label(root, text="Brightness:")
w.place(x=10, y=1,  width=80,  height=20)
w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
w.pack()
w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
w.pack()
w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
w.pack()
w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
w.pack()
root.mainloop()
