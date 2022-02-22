from pydoc import text
from tkinter import *
from turtle import width

class Gui(Frame):
    
    def __init__(self, master):
        super(Gui, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text = 'Enter Your Keywords')
        self.label.config(font = ('Arial', 15))
        self.label.pack(pady = 20)

        self.entry = Entry(self)
        self.entry.pack(pady= 10, ipadx=40)

        self.button = Button(self, text = 'Submit', width = 20)
        self.button.pack(side = 'bottom', pady = 10)

root = Tk()
root.title('Google Maps Searcher')
root.geometry('300x200')
app = Gui(root)
root.mainloop()