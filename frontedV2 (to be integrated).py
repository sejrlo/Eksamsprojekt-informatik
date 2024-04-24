import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk

dir = os.path.dirname(__file__)

class App(tk.Tk):
    def __init__(self, start_frame):
        super().__init__()
        self.title("AppTube")
        self.geometry("400x600")

        # Dictionary to hold the frames
        self.frames = {}
        
        frame_classes = {'login': LoginFrame, 'register': RegisterFrame, 'search': SearchFrame}
        for key, FrameClass in frame_classes.items():
            frame = FrameClass(self, self.switch_frame)
            self.frames[key] = frame
            frame.grid(row=0, column=0, sticky='nsew')
            
        self.switch_frame(start_frame)

    def switch_frame(self, frame_key):
        """Switch to a frame given by frame_key."""
        current_frame = (frame_key, self.frames[frame_key])
        print(current_frame)
        for frame_name, frame_object in self.frames.items():
            if frame_name != frame_key:
                frame_object.hide()



class Frame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame
    
    def hide_frame(self):
        self.frame.grid_remove()
        
        
class RegisterFrame(Frame):
    def __init__(self, master):
        super().__init__()
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        email_grid = {"row": 1, "column": 0}
        username_grid = {"row": 2, "column": 0}
        password_grid = {"row": 3, "column": 0}
        confirm_password_grid = {"row": 4, "column": 0}
        
        print(confirm_password_grid["column"]+1)
        
        tk.Label(self, text="Email:").grid(row=email_grid["row"], column=email_grid["column"])
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=email_grid["row"], column=email_grid["column"]+1)
    

        tk.Label(self, text="Username:").grid(row=username_grid["row"], column=email_grid["column"])
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=username_grid["row"], column=email_grid["column"]+1)
        self.username_entry.focus()  
        
        tk.Label(self, text="Password:").grid(row=password_grid["row"], column=password_grid["column"])
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=password_grid["row"], column=password_grid["column"]+1)
        
        tk.Label(self, text="Confirm Password:").grid(row=confirm_password_grid["row"], column=confirm_password_grid["column"])
        self.confirm_password_entry = tk.Entry(self, show="$")
        self.confirm_password_entry.grid(row=confirm_password_grid["row"], column=confirm_password_grid["column"]+1)
        

        login_button = tk.Button(self, text="Login", command=self.attempt_register)
        login_button.grid(row=2, column=1)
        
        self.feedback_label = tk.Label(self, text="")
        self.feedback_label.grid(row=3, column=0, columnspan=2)

    def attempt_register(self):
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if password == confirm_password:
            user = self.create_user(email, username, password)
            if self.create_user(username, password):
                self.on_success()  
        else:
            self.feedback_label.config(text="Password must be identical, try again")

    def create_user(self, username, password):
        return username == "" and password == "" 


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__()
        super().__init__(master)
        self.frame = tk.Frame(self)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)
        self.username_entry.focus()  
        
        tk.Label(self, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

        login_button = tk.Button(self, text="Login", command=self.attempt_login)
        login_button.grid(row=2, column=1)
        
        self.feedback_label = tk.Label(self, text="")
        self.feedback_label.grid(row=3, column=0, columnspan=2)

    def attempt_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.verify_credentials(username, password):
            self.on_success()  
        else:
            self.feedback_label.config(text="Invalid credentials, try again.")

    def verify_credentials(self, username, password):
        return username == "" and password == "" 


class SearchFrame(Frame):
    def __init__(self, master):
        super().__init__()
        super().__init__(master)
        self.frame = tk.Frame(self)  # Initialize the frame here
        self.create_widgets() 

    def create_widgets(self):
        instruction = tk.Label(self.frame, text="Indtast din søgeforespørgsel:")
        instruction.grid(row=0, column=0, columnspan=2)
        
        self.search_entry = tk.Entry(self.frame)
        self.search_entry.grid(row=1, column=0, columnspan=2, sticky="ew")
        
        search_button = tk.Button(self.frame, text="Søg", width=10, command=self.search_action)
        search_button.grid(row=2, column=0, sticky="w")
        
        self.search_feedback = tk.Label(self.frame, text="")
        self.search_feedback.grid(row=2, column=1)

        # logout_button = tk.Button(self.search_frame, text="Logout", command=self.switch_to_login)
        # logout_button.grid(row=3, column=0, sticky="ew", columnspan=2)

        file_name = "LogoutIcon.png"
        file_path_logout_icon = os.path.join(dir, file_name)
 
        img = Image.open(file_path_logout_icon)
        size = 30
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)  
        self.top_right_image = ImageTk.PhotoImage(resized_img)
        top_right_button = tk.Button(self.frame, image=self.top_right_image, command=self.switch_to_login)
        top_right_button.grid(row=0, column=3, sticky="ne",padx=(160,0))
        
        
    def switch_to_search(self):
        self.login_frame.grid_remove()
        self.search_frame.grid()
        self.search_entry.focus()  # Focus on search entry after logging in
        self.update_idletasks()  # Refresh GUI to ensure visibility

    def switch_to_login(self):
        self.frame.grid_remove()
        self.login_frame.grid()
        self.login_frame.username_entry.focus()  # Focus back to username entry on logout
        self.update_idletasks()  # Refresh GUI to ensure visibility

    def search_action(self):
        search_query = self.search_entry.get()
        self.search_feedback.config(text=f"Searching for {search_query}")
        print(search_query)



app = App('login')