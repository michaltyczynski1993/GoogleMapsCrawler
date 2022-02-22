from pydoc import text
from tkinter import *

class Gui(Frame):
    
    def __init__(self, master):
        super(Gui, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text = 'Enter Your Keywords')
        self.label.pack()

        self.entry = Entry(self)
        self.entry.pack()

        self.button = Button(self, text = 'Submit')
        self.button.pack(side = 'bottom')

root = Tk()
root.title('Google Maps Searcher')
root.geometry('300x150')
app = Gui(root)
root.mainloop()