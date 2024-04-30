import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk
from Client_socket import Connection

dir = os.path.dirname(__file__)
media_path = os.path.join(dir, "Client_Media")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DeTube")
        self.geometry("300x400")
        self.displayname = ""
        frames_classes = {'login': LoginFrame, 'search': SearchFrame, 'register': RegisterFrame}
        
        self.frames = {}
        for key, Frameclass in frames_classes.items():
            frame = Frameclass(self)
            self.frames[key] = frame
            frame.grid(row=0, column=0, sticky='nsew')
            frame.make_layout()
        
        self.active_frame('login')
        
        
    def active_frame(self, frame_key):
        frame_to_raise = self.frames[frame_key]
        frame_to_raise.tkraise()
        frame_to_raise.focus_set()
        self.title(frame_key.capitalize())
        
        
        self.unbind_all('<Return>')

        if frame_key == 'login':
            self.bind_all('<Return>', lambda event: frame_to_raise.verify_login('search'))
        elif frame_key == 'register':
            self.bind_all('<Return>', lambda event: frame_to_raise.register())
        elif frame_key == 'search':
            self.bind_all('<Return>', lambda event: frame_to_raise.search_action())

                    
class LoginFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
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

        self.w['register_button'] = tk.Button(self, text="Register", command=lambda: app.active_frame('register'))
        self.w['register_button'].grid(row=3, column=1)
        
        self.w['feedback_label'] = tk.Label(self, text="")
        self.w['feedback_label'].grid(row=4, column=0, columnspan=2)
        
    def verify_login(self, page_key):
        username = self.w['username_entry_field'].get()
        password = self.w['password_entry_field'].get()
        
        connection.send({"request":"Login", "username":username, "password":password})
        answer = connection.receive()
        print(answer)
        if answer['status'] == 'success':
            self.w['username_entry_field'].delete(0, tk.END)
            self.w['feedback_label'].config(text='')
            self.window.username = answer['username']
            self.window.displayname = answer['displayname']
            app.active_frame(page_key)
            
        elif answer["status"] == "Username or password incorrect":
            self.w['feedback_label'].config(text='Invalid credentials, try again.')

        elif answer["status"] == "Username taken":
            self.w['feedback_label'].config(text='Username taken')

        
        self.w['password_entry_field'].delete(0, tk.END)
      
class SearchFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.w = {}
    
    def make_layout(self):
            self.w['instruction'] = tk.Label(self, text="Indtast din søgeforespørgsel:")
            self.w['instruction'].grid(row=0, column=0, columnspan=2)
            
            self.w['search_entry'] = tk.Entry(self)
            self.w['search_entry'].grid(row=1, column=0, columnspan=2, sticky="ew")
            
            self.w['search_button'] = tk.Button(self, text="Søg", width=10, command=self.search_action)
            self.w['search_button'].grid(row=2, column=0, sticky="w")
            
            self.w['search_feedback'] = tk.Label(self, text="")
            self.w['search_feedback'].grid(row=3, column=0)

            # logout_button = tk.Button(self.search_frame, text="Logout", command=self.switch_to_login)
            # logout_button.grid(row=3, column=0, sticky="ew", columnspan=2)

            file_name = "LogoutIcon.png"
            file_path_logout_icon = os.path.join(dir, file_name)
    
            img = Image.open(file_path_logout_icon)
            size = 30
            resized_img = img.resize((size, size), Image.Resampling.LANCZOS)  
            self.log_out_image = ImageTk.PhotoImage(resized_img)
            self.w['logout_button'] = tk.Button(self, image=self.log_out_image, command=self.log_out)
            self.w['logout_button'].grid(row=0, column=3, sticky="ne",padx=(40,0))
            
            self.w['display_name_label'] = tk.Label(self, text=self.window.displayname)
    
    def search_action(self):
        search_query = self.w['search_entry'].get()
        self.w['search_feedback'].config(text=f"Searching for '{search_query}'")
        connection.send({'request':'Search','search':search_query})
        ans = connection.receive()
        print(media_path)
        if ans['status'] == 'success':
            connection.send({'request':'Get_media','mediaid':ans['mediaids'][0]})
            file_ans = connection.receive()
            if file_ans['status'] == 'success':
<<<<<<< HEAD
                media_path = file_ans[0]
=======
                with open(os.path.join(media_path, f"{file_ans['medianame']}.{file_ans['datatype']}"), "wb") as f:
                    f.write(bytes.fromhex(file_ans["data"]))
                self.w['search_feedback'].config(text=f"1 media downloaded and is ready to view.")
            else:
                self.w['search_feedback'].config(text=f"Error in search. Try again later")
        elif ans['status'] == 'Fail':
            self.w['search_feedback'].config(text=f"No results found. Try another search query")
        else:    
            self.w['search_feedback'].config(text=f"Error in search. Try again later")
        
>>>>>>> f1dd663c09657f8e943ba89ce8c2e4a97255cab9
        
    def log_out(self):
        connection.send({'request':'Logout'})
        answer = connection.receive()
        app.active_frame('login')
    
    
class RegisterFrame(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.w = {}
        self.window = window
        
    
    def make_layout(self):
        self.w['email_label'] = tk.Label(self, text="Email:")
        self.w['email_label'].grid(row=1, column=0)
        self.w['email_entry'] = tk.Entry(self)
        self.w['email_entry'].grid(row=1, column=1)
        

        
        self.w['username_label'] = tk.Label(self, text="Username:").grid(row=2, column=0)
        self.w['username_entry'] = tk.Entry(self)
        self.w['username_entry'].grid(row=2, column=1)
        
        
        
        self.w['password_label'] = tk.Label(self, text="Password:").grid(row=3, column=0)
        self.w['password_entry'] = tk.Entry(self, show="*")
        self.w['password_entry'].grid(row=3, column=1)
        
        
        
        self.w['confirm_password_label'] = tk.Label(self, text="Confirm Password:").grid(row=4, column=0)
        self.w['confirm_password_entry'] = tk.Entry(self, show="*")
        self.w['confirm_password_entry'].grid(row=4, column=1)
        
        
            
        self.w['register_button'] = tk.Button(self, text="Register", command=self.register)
        self.w['register_button'].grid(row=5, column=1)
        
        
        self.w['back_to_login_button'] = tk.Button(self, text="Back", command=lambda: app.active_frame('login'))
        self.w['back_to_login_button'].grid(row=6, column=1)
        
        self.w['feedback_label'] = tk.Label(self, text="")
        self.w['feedback_label'].grid(row=7, column=0, columnspan=2)

    def register(self):
        email = self.w['email_entry'].get()
        username = self.w['username_entry'].get()
        password = self.w['password_entry'].get()
        confirm_password = self.w['confirm_password_entry'].get()
        if username == "":
            self.w['feedback_label'].config(text='Username can\'t be empty')

        elif len(password) < 8:
            self.w['feedback_label'].config(text='Password must me longer than 7 charactors')

        elif password != confirm_password:
            self.w['feedback_label'].config(text='Password must be identical, try again')
            
        else:
            connection.send({'request':'Register','email':email,'password':password,'username':username})
            answer = connection.receive()
            if answer['status'] == 'success':
                self.w['feedback_label'].config(text='')
                app.active_frame('search')
                self.window.username = answer['username']
                self.window.displayname = answer['displayname']
                



def close():
    connection.disconnect()
    app.destroy()

connection = Connection()
      
app = App()
app.protocol("WM_DELETE_WINDOW", close)
app.mainloop()


