import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk

dir = os.path.dirname(__file__)




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DeTube")
        self.geometry("400x600")
        
        frames_classes = {'login': LoginFrame, 'search': SearchFrame}
        
        self.frames = {}
        for key, Frameclass in frames_classes.items():
            frame = Frameclass(self, key)
            self.frames[key] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.frames['login'].tkraise()
        
    def select_active_frame(self, frame_key):
        app.frames[frame_key].tkraise()

        
        

            
            
    

class Frame(tk.Frame):
    def __init__(self, window, key, layout):
        super().__init__(window)
        self.id = key
        
        self.layout_dic = {}
        
        layout
        
    

        

    
class LoginFrame(Frame):
    def __init__(self, window, key):
        super().__init__(window, key)
        

        
class SearchFrame(Frame):
    def __init__(self, window, key):
        super().__init__(window, key)
    
    
app = App()