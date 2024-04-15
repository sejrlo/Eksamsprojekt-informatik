import tkinter as tk
from tkinter import ttk

class LoginFrame(tk.Frame):
    def __init__(self, master, on_success):
        super().__init__(master)
        self.on_success = on_success
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)
        self.username_entry.focus()  # Focus on username initially
        
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
            self.on_success()  # Switch to the search frame if login is successful
        else:
            self.feedback_label.config(text="Invalid credentials, try again.")

    def verify_credentials(self, username, password):
        return username == "admin" and password == "password"  # Example check

class Search_menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Søgefelt Eksempel")
        self.geometry("400x400+100+100")
        self.setup_frames()
        self.mainloop()

    def setup_frames(self):
        self.search_frame = tk.Frame(self)
        self.create_search_widgets()
        self.login_frame = LoginFrame(self, self.switch_to_search)
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.search_frame.grid(row=0, column=0, sticky="nsew")
        self.search_frame.grid_remove()

    def create_search_widgets(self):
        instruction = tk.Label(self.search_frame, text="Indtast din søgeforespørgsel:")
        instruction.grid(row=0, column=0, columnspan=2)
        
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.grid(row=1, column=0, columnspan=2, sticky="ew")
        
        search_button = tk.Button(self.search_frame, text="Søg", width=10, command=self.search_action)
        search_button.grid(row=2, column=0, sticky="w")
        
        self.search_feedback = tk.Label(self.search_frame, text="")
        self.search_feedback.grid(row=2, column=1)

        logout_button = tk.Button(self.search_frame, text="Logout", command=self.switch_to_login)
        logout_button.grid(row=3, column=0, sticky="ew", columnspan=2)

    def switch_to_search(self):
        self.login_frame.grid_remove()
        self.search_frame.grid()
        self.search_entry.focus()  # Focus on search entry after logging in
        self.update_idletasks()  # Refresh GUI to ensure visibility

    def switch_to_login(self):
        self.search_frame.grid_remove()
        self.login_frame.grid()
        self.login_frame.username_entry.focus()  # Focus back to username entry on logout
        self.update_idletasks()  # Refresh GUI to ensure visibility

    def search_action(self):
        search_query = self.search_entry.get()
        self.search_feedback.config(text=f"Searching for {search_query}")
        print(search_query)

app = Search_menu()