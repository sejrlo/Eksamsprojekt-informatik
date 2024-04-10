import tkinter as tk
from tkinter import ttk
# from Client_socket import Connection

class Connection():
    def send(self, data):
        return f'request: {data['request']} with search query "{data['search_query']}"'

connection = Connection()



class Search_menu():
    def __init__(self):
        self.window = tk.Tk()
      
    def create_layout(self):
        # Opret hovedvinduet
        search_menu.title("Søgefelt Eksempel")

        # Konfigurer vinduets størrelse og startposition
        search_menu.geometry("400x200+100+100")

        # Opret en ramme til at holde widgets
        frame = ttk.Frame(search_menu, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Opret et etiket (label) widget
        label = ttk.Label(frame, text="Indtast din søgeforespørgsel:")
        label.grid(row=0, column=0, sticky=tk.W, pady=2)

        # Opret et tekstindtastningsfelt (entry) widget
        search_entry = ttk.Entry(frame, width=50)
        search_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=2)
        search_entry.focus()  # Sæt fokus til tekstfeltet ved programstart

        # Opret en knap widget til at initiere søgning
        search_button = ttk.Button(frame, text="Søg", command=self.search_action(search_entry.get()))
        search_button.grid(row=2, column=0, sticky=tk.W, pady=2)
    
      
    """ Events """
    def search_action(self, entry):
        search_query = entry  # Hent tekst fra søgefeltet
        
        request = connection.send({"request":"search_results", "search_query": search_query})

        print(request)
        
        search_feedback = tk.Text(search_menu, height=10, width = 50)
        search_feedback.insert("1.0", "Searching...")
        search_feedback.grid(row=2, column=1, sticky=tk.W, pady=2)

    def register(username, password, confirmpassword):
        if password == confirmpassword:
            connection.send({"request":"register", "username":username, "password":password})
            status = connection.receive()
            if status[status] == "success":
                pass
       
    def login(username, password):
        connection.send({"request":"login", "username":username, "password":password})
        status = connection.receive()
        if status[status] == "success":
            pass

    

    def run(self):
        # Kør hovedbegivenhedsløkken
        self.window.mainloop()


search_menu = Search_menu()
