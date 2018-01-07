#!/usr/bin/env python
'''
xrandrgui

This file provides a simple way to change the settings on a linux machine using xrandr.  It
provides access to only the most basic settings.
'''
from tkinter import *
# Est ablish the base window
root = Tk()
root.title("xrandrgui")

# Create the widgets
lbl_bright = Label(root, text="Brightness:")
scl_bright = Scale(root, from_=0, to=200, orient=HORIZONTAL,  length=400)
lbl_space = Label(root,  text=" ")
lbl_gamma = Label(root,  text="Gamma:")
lbl_r = Label(root,  text="R:")
scl_r = Scale(root, from_=0, to=200, orient=HORIZONTAL, length=400)
lbl_g = Label(root, text="G:")
scl_g = Scale(root, from_=0, to=200, orient=HORIZONTAL,  length=400)
lbl_b = Label(root,  text="B:")
scl_b = Scale(root, from_=0, to=200, orient=HORIZONTAL,  length=400)

# Place the widgets using grid
lbl_bright.grid(row=0,  column=0, sticky="SE")
scl_bright.grid(row=0,  column=1)
lbl_space.grid(row=1,  column=0)
lbl_gamma.grid(row=2,  column=0,  sticky="SE")
lbl_r.grid(row=3,  column=0,  sticky="SE")
scl_r.grid(row=3,  column=1)
lbl_g.grid(row=4,  column=0,  sticky="SE")
scl_g.grid(row=4,  column=1)
lbl_b.grid(row=5,  column=0,  sticky="SE")
scl_b.grid(row=5,  column=1)


# Loop
root.mainloop()
