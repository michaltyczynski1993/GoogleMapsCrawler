from distutils import command
from pydoc import text
from tkinter import *
from turtle import width
from crawler import GoogleMapsCrawler

class Gui(Frame):
    
    def __init__(self, master):
        super(Gui, self).__init__(master)
        self.pack()
        self.create_widgets()
        self.g = GoogleMapsCrawler()
        

    def create_widgets(self):
        self.label = Label(self, text = 'Enter Your Keywords')
        self.label.config(font = ('Arial', 15))
        self.label.pack(pady = 20)

        # entry field for keyword search input
        self.entry = Entry(self)
        self.entry.pack(pady= 10, ipadx=40)

        # create driver instruction label
        self.instruction_label = Label(self, text = 'if browser not open, press "Create Driver" button')
        self.instruction_label.pack(pady=5)

        # create driver button - when browser not open 'blank' page
        self.driver_button = Button(self, text = 'Create Driver')
        self.driver_button.pack()
        self.driver_button['command'] = self.create_driver

        self.button = Button(self, text = 'Submit', width = 20)
        self.button.pack(side = 'bottom', pady = 10)
        self.button['command'] = self.search_google_maps
 
    def create_driver(self):
            self.g = GoogleMapsCrawler()
        
    def search_google_maps(self):
        keywords = self.entry.get()
        self.g.main_site()
        self.g.search(keywords)
        self.g.scroll_down_results()
        self.g.open_results()

root = Tk()
root.title('Google Maps Searcher')
root.geometry('300x250')
app = Gui(root)
root.mainloop()