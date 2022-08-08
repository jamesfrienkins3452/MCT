import tkinter as tk

class ScreenSettings:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
    
    def width(self):
        return self.screen_width
    
    def height(self):
        return self.screen_height
    
    def size(self):
        return self.screen_width, self.screen_height