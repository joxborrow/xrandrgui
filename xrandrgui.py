from tkinter import *

class xrandrgui:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.initialize(master)

    def initialize(self, master):

        # Brightness
        self.label1 = Label(master, text="Brightness")
        self.label1.grid(row=0, column=0)
        self.sc_brightness = Scale(master, from_=0, to=200, orient=HORIZONTAL)
        self.sc_brightness.grid(row=0, column=1)

        # Gamma
        self.label2 = Label(master, text="Gamma")
        self.label2.grid(row=1, column=0)

        # R
        self.label3 = Label(master, text="R ")
        self.label3.grid(row=2, column=0, sticky="SE")
        self.sc_r = Scale(master, from_=0, to=100, orient=HORIZONTAL)
        self.sc_r.grid(row=2, column=1)

        # G
        self.label4 = Label(master, text="G")
        self.label4.grid(row=3, column=0)
        self.sc_g = Scale(master, from_=0.0, to=100.0, orient=HORIZONTAL)
        self.sc_g.grid(row=3, column=1)

        # B
        self.label5 = Label(master, text="B")
        self.label5.grid(row=4, column=0)
        self.sc_b = Scale(master, from_=0, to=100, orient=HORIZONTAL)
        self.sc_b.grid(row=4, column=1)

        # Apply
        self.bt_apply = Button(master, text="Apply")
        self.bt_apply.grid(row=5, column=3)

        # Clos
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=5, column=4)

if __name__ == '__main__':
    root = Tk()
    my_gui = xrandrgui(root)
    root.mainloop()
