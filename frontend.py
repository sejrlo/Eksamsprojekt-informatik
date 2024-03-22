import tkinter as tk
from tkinter import ttk

# Funktion til at håndtere søgeknappens handling
def search_action():
    search_query = search_entry.get()  # Hent tekst fra søgefeltet
    print(f"Søgeforespørgsel: {search_query}")  # Simuler en søgehandling ved at udskrive til konsollen

# Opret hovedvinduet
root = tk.Tk()
root.title("Søgefelt Eksempel")

# Konfigurer vinduets størrelse og startposition
root.geometry("400x200+100+100")

# Opret en ramme til at holde widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Opret et etiket (label) widget
label = ttk.Label(frame, text="Indtast din søgeforespørgsel:")
label.grid(row=0, column=0, sticky=tk.W, pady=2)

# Opret et tekstindtastningsfelt (entry) widget
search_entry = ttk.Entry(frame, width=50)
search_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=2)
search_entry.focus()  # Sæt fokus til tekstfeltet ved programstart

# Opret en knap widget til at initiere søgning
search_button = ttk.Button(frame, text="Søg", command=search_action)
search_button.grid(row=2, column=0, sticky=tk.W, pady=2)

# Kør hovedbegivenhedsløkken
root.mainloop()