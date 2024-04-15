import tkinter as tk
from tkinter import ttk
from Client_socket import Connection

connection = Connection()
    
class Search_menu():
    def __init__(self):
        self.window = tk.Tk()
        self.create_layout()
        self.running = True
        self.mainloop()
      
    def create_layout(self):
        # Opret hovedvinduet
        self.window.title("Søgefelt Eksempel")
        self.window.geometry("400x200+100+100")

        # Opret en ramme til at holde widgets
        frame = ttk.Frame(self.window, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Opret et etiket (label) widget
        label = ttk.Label(frame, text="Indtast din søgeforespørgsel:")
        label.grid(row=0, column=0, sticky=tk.W, pady=2)

        # Opret et tekstindtastningsfelt (entry) widget
        self.search_entry = ttk.Entry(frame, width=50)  # Changed to an instance attribute
        self.search_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=2)
        self.search_entry.focus()

        # Opret en knap widget til at initiere søgning
        search_button = ttk.Button(frame, text="Søg", command=lambda: self.search_action())
        search_button.grid(row=2, column=0, sticky=tk.W, pady=2)

        # Create a Text widget for search feedback (moved outside the method for reuse)
        self.search_feedback = tk.Text(self.window, height=10, width=50)
        self.search_feedback.grid(row=2, column=1, sticky=tk.W, pady=2)

    """ Events """
    def search_action(self):
        search_query = self.search_entry.get()  # Hent tekst fra søgefeltet direkte
        print(search_query)
        
        # Clear the Text widget before inserting new text
        self.search_feedback.delete("1.0", tk.END)
        self.search_feedback.insert("1.0", "Searching for: " + search_query)

    def mainloop(self):
        # Kør hovedbegivenhedsløkkenˆ
        print("running")
        if self.running:
            self.window.mainloop()

search_menu = Search_menu()
