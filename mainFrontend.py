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
            frame = Frameclass(self)
            self.frames[key] = frame
            frame.grid(row=0, column=0, sticky='nsew')
            frame.make_layout()
        
        self.select_active_frame('login')
        
        
    def select_active_frame(self, frame_key):
        self.frames[frame_key].tkraise()
        self.title(frame_key.capitalize())

        
        

                
class LoginFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.w = {}
        
    def make_layout(self):        
        self.w['username_entry_label'] = tk.Label(self, text="Username:").grid(row=0, column=0)
        self.w['username_entry_field'] = tk.Entry(self)
        self.w['username_entry_field'].grid(row=0, column=1)
        self.w['username_entry_field'].focus() 
        
        self.w['password_entry_label'] = tk.Label(self, text="Password:").grid(row=1, column=0)
        self.w['password_entry_field'] = tk.Entry(self, show="*")
        self.w['password_entry_field'].grid(row=1, column=1)

        self.w['login_button'] = tk.Button(self, text="Login", command=lambda: self.verify_login('search'))
        self.w['login_button'].grid(row=2, column=1)
        
        self.feedback_label = tk.Label(self, text="")
        self.feedback_label.grid(row=3, column=0, columnspan=2)
        
    def verify_login(self, page_key):
        username = self.w['username_entry_field'].get()
        password = self.w['password_entry_field'].get()
        print(username, password)
        app.select_active_frame(page_key)
        
        
        
        
class SearchFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.w = {}
    
    def make_layout(self):
            self.w['instruction'] = tk.Label(self, text="Indtast din søgeforespørgsel:")
            self.w['instruction'].grid(row=0, column=0, columnspan=2)
            
            self.w['search_entry'] = tk.Entry(self)
            self.w['search_entry'].grid(row=1, column=0, columnspan=2, sticky="ew")
            
            self.w['search_button'] = tk.Button(self, text="Søg", width=10, command=self.search_action)
            self.w['search_button'].grid(row=2, column=0, sticky="w")
            
            self.w['search_feedback'] = tk.Label(self, text="")
            self.w['search_feedback'].grid(row=2, column=1)

            # logout_button = tk.Button(self.search_frame, text="Logout", command=self.switch_to_login)
            # logout_button.grid(row=3, column=0, sticky="ew", columnspan=2)

            file_name = "LogoutIcon.png"
            file_path_logout_icon = os.path.join(dir, file_name)
    
            img = Image.open(file_path_logout_icon)
            size = 30
            resized_img = img.resize((size, size), Image.Resampling.LANCZOS)  
            self.log_out_image = ImageTk.PhotoImage(resized_img)
            self.w['logout_button'] = tk.Button(self, image=self.log_out_image, command=self.log_out)
            self.w['logout_button'].grid(row=0, column=3, sticky="ne",padx=(160,0))
    
    def search_action(self):
        search_query = self.search_widget['instruction'].get()
        self.search_feedback.config(text=f"Searching for {search_query}")
        print(search_query)
        
        
    def log_out(self):
        app.select_active_frame('login')
    
app = App()

app.mainloop()