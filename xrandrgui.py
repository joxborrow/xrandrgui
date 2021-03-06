#!/usr/bin/env python
#----------------------------------------------------------------
# This is a short script creating a gui interface to the 
# xrandr command in linux. It makes adjustments easy for
# anyone through a gui interface.
#----------------------------------------------------------------
import tkinter as tk
import subprocess as sp

# Create GUI
class xrandrgui(tk.Frame):
    def __init__(self, master):
        self.master = master
        master.title("Simple xrandr GUI")
        self.initialize(master)

    def initialize(self, master):
        # Get attached monitors
        monitors = sp.getoutput("xrandr --query | awk '/ connected / {print $1}'")

        # Get resolutions
        resolutions = sp.getoutput("xrandr --query | awk '/   / {print $1}'")

        # Initialize Frame 1
        self.Frame1 = tk.LabelFrame(master)
        self.Frame1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="EWNS", padx=10, pady=(10,0))

        # Output
        self.label0 = tk.Label(self.Frame1, text="Output")
        self.label0.grid(row=0, column=0, padx=2, pady=2, sticky="E")
        output_options = tuple(monitors.split("\n"))
        self.op1 = tk.StringVar(master)
        self.op1.set(output_options[0])
        self.optionmenu1 = tk.OptionMenu(self.Frame1, self.op1, *output_options, command=self.run_prog)
        self.optionmenu1.config(width=10)
        self.optionmenu1.grid(row=0, column=1, sticky="W", padx=2, pady=2)

        # Resolution
        self.label01 = tk.Label(self.Frame1, text="Resolution")
        self.label01.grid(row=1, column=0, padx=2, pady=2, sticky="E")
        resolution_options = tuple(resolutions.split("\n"))
        self.op2 = tk.StringVar(master)
        self.op2.set(resolution_options[0])
        self.optionmenu2 = tk.OptionMenu(self.Frame1, self.op2, *resolution_options, command=self.change_res)
        self.optionmenu2.config(width=10)
        self.optionmenu2.grid(row=1, column=1, sticky="W", padx=2, pady=2)

        # X Scale
        self.label02 = tk.Label(self.Frame1, text="X Scale")
        self.label02.grid(row=0, column=2, sticky="E", padx=2, pady=2)
        init_spinbox = tk.StringVar(root)
        init_spinbox.set("1")
        self.spinbox01 = tk.Spinbox(self.Frame1, from_=.1, to_=2, increment=.1,
                                    textvariable=init_spinbox, command=self.change_scale)
        self.spinbox01.grid(row=0, column=3, sticky="EWNS", padx=2, pady=2)

        # Y Scale
        self.label03 = tk.Label(self.Frame1, text="Y Scale")
        self.label03.grid(row=1, column=2, sticky="E", padx=2, pady=2)
        init_spinbox2 = tk.StringVar(root)
        init_spinbox2.set("1")
        self.spinbox02 = tk.Spinbox(self.Frame1, from_=.1, to_=2, increment=.1,
                                    textvariable=init_spinbox2, command=self.change_scale)
        self.spinbox02.grid(row=1, column=3, sticky="EWNS", padx=2, pady=2)

        # Rotate
        self.label04 = tk.Label(self.Frame1, text="Rotate")
        self.label04.grid(row=2, column=2, sticky="E", padx=2, pady=2)
        rotate_options = tuple(('normal', 'left', 'right', 'inverted'))
        self.op3 = tk.StringVar(master)
        self.op3.set(rotate_options[0])
        self.optionmenu3 = tk.OptionMenu(self.Frame1, self.op3, *rotate_options, command=self.change_rotation)
        self.optionmenu3.config(width=10)
        self.optionmenu3.grid(row=2, column=3, sticky="NSEW", padx=2, pady=2)

        # Frame 2
        self.Frame2 = tk.LabelFrame(master, text="Brightness")
        self.Frame2.grid(row=2, column=0, columnspan=3, sticky="EWNS", padx=10, pady=10)

        # Brightness
        self.sc_brightness = tk.Scale(self.Frame2, from_=0, to_=5, length=420,
                                   orient=tk.HORIZONTAL, resolution=.05,
                                   command=self.run_prog)
        self.sc_brightness.grid(row=2, column=1, padx=2, pady=2, columnspan=4, sticky="NSEW")

        # Frame 3
        self.Frame3 = tk.LabelFrame(master, text="Gamma")
        self.Frame3.grid(row=3, column=0, sticky="SENW", padx=10, columnspan=2, rowspan=4,
                    pady=10)

        # R
        self.label3 = tk.Label(self.Frame3, text="R ")
        self.label3.grid(row=4, column=0, sticky="SE", padx=2, pady=2)
        self.sc_r = tk.Scale(self.Frame3, from_=0, to_=5, length=400,
                          orient=tk.HORIZONTAL, resolution=.05,
                          command=self.run_prog)
        self.sc_r.grid(row=4, column=1, padx=2, pady=2)

        # G
        self.label4 = tk.Label(self.Frame3, text="G ")
        self.label4.grid(row=5, column=0, sticky="SE", padx=2, pady=2)
        self.sc_g = tk.Scale(self.Frame3, from_=0, to_=5, length=400,
                          orient=tk.HORIZONTAL, resolution=.05,
                          command=self.run_prog)
        self.sc_g.grid(row=5, column=1, padx=2, pady=2)

        # B
        self.label5 = tk.Label(self.Frame3, text="B ")
        self.label5.grid(row=6, column=0, sticky="SE", padx=2, pady=2)
        self.sc_b = tk.Scale(self.Frame3, from_=0, to_=5, length=400,
                          orient=tk.HORIZONTAL, resolution=.05,
                          command=self.run_prog)
        self.sc_b.grid(row=6, column=1, padx=2, pady=2)

        # Initialize control values
        self.sc_brightness.set(1)

    # Execute xrandr
    def run_prog(self, value):
        # Build xrandr command
        command_string = 'xrandr --output '
        command_string = command_string + self.op1.get()
        command_string = command_string + ' --brightness ' + str(self.sc_brightness.get())
        command_string = command_string + ' --gamma ' + str(self.sc_r.get()) + ":" + \
                         str(self.sc_g.get()) + ":" + str(self.sc_b.get())
        print(command_string)
        sp.call(command_string, shell=True)

    # Change resolution
    def change_res(self, value):
        command_string = 'xrandr --output '
        command_string = command_string + self.op1.get()
        command_string = command_string + ' --mode ' + self.op2.get()
        print(command_string)
        sp.call(command_string, shell=True)

    # Change Scale
    def change_scale(self):
        command_string = 'xrandr --output '
        command_string = command_string + self.op1.get()
        command_string = command_string + ' --scale '
        command_string = command_string + self.spinbox01.get() + 'x'
        + self.spinbox02.get()
        print(command_string)
        sp.call(command_string, shell=True)

    # Change Rotation
    def change_rotation(self, value):
        command_string = 'xrandr --output '
        command_string = command_string + self.op1.get()
        command_string = command_string + ' --rotate '
        command_string = command_string + self.op3.get()
        print(command_string)
        sp.call(command_string, shell=True)

# Main
if __name__ == '__main__':
    root = tk.Tk()
    my_gui = xrandrgui(root)
    root.mainloop()
