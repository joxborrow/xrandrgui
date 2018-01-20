from tkinter import *
import subprocess

# Create GUI
class xrandrgui:
    def __init__(self, master):
        self.master = master
        master.title("Simple xrandr GUI")
        self.initialize(master)

    def initialize(self, master):
        # Get attached monitors
        monitors = subprocess.getoutput("xrandr --query | awk '/ connected / {print $1}'")

        # Output
        self.label0 = Label(master, text="Output")
        self.label0.grid(row=0, column=0)
        output_options = tuple(monitors.split("\n"))
        self.op1 = StringVar(master)
        self.op1.set(output_options[0])
        self.optionmenu1 = OptionMenu(master, self.op1, *output_options)
        self.optionmenu1.grid(row=0, column=1, sticky="W")

        # Brightness
        self.label1 = Label(master, text="Brightness")
        self.label1.grid(row=1, column=0, sticky="SE")
        self.sc_brightness = Scale(master, from_=0, to_=5, length=300,
                                   orient=HORIZONTAL, resolution=.05,
                                   command=self.run_prog)
        self.sc_brightness.grid(row=1, column=1)

        # Gamma
        self.label2 = Label(master, text="Gamma")
        self.label2.grid(row=2, column=0, sticky="S")

        # R
        self.label3 = Label(master, text="R ")
        self.label3.grid(row=3, column=0, sticky="SE")
        self.sc_r = Scale(master, from_=0, to=100, orient=HORIZONTAL)
        self.sc_r.grid(row=3, column=1)

        # G
        self.label4 = Label(master, text="G ")
        self.label4.grid(row=4, column=0, sticky="SE")
        self.sc_g = Scale(master, from_=0.0, to=100.0, orient=HORIZONTAL)
        self.sc_g.grid(row=4, column=1)

        # B
        self.label5 = Label(master, text="B ")
        self.label5.grid(row=5, column=0, sticky="SE")
        self.sc_b = Scale(master, from_=0, to=100, orient=HORIZONTAL)
        self.sc_b.grid(row=5, column=1)

        # Apply
        self.bt_apply = Button(master, text="Apply", command=self.run_prog)
        self.bt_apply.grid(row=6, column=3)

        # Close
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=6, column=4)

    # Execute xrandr
    def run_prog(self, value):
        # Build xrandr command
        command_string = 'xrandr --output '
        command_string = command_string + self.op1.get()
        command_string = command_string + ' --brightness ' + str(self.sc_brightness.get())
        subprocess.call(command_string, shell=True)

# Main
if __name__ == '__main__':
    root = Tk()
    my_gui = xrandrgui(root)
    root.mainloop()
