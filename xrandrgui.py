from tkinter import Tk, Label, Button

class xrandrgui:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.initialize(master)

    def initialize(self, master):
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

if __name__ == '__main__':
    root = Tk()
    my_gui = xrandrgui(root)
    root.mainloop()
