import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Grid Layout Example")

# Create widgets
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
entry1 = tk.Entry(root)
button1 = tk.Button(root, text="Click Me!")

# Arrange widgets in the grid
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
entry1.grid(row=0, column=1)
button1.grid(row=1, column=1)

# Configure row and column weights
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()
