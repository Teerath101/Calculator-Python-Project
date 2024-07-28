import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("Tkinter.Ttk Widgets Example")

# Create a label widget
label = tk.Label(main_window, text="This is a Tkinter.Ttk Label")
label.pack()

# Create an entry widget
entry = tk.Entry(main_window)
entry.pack()

# Create a button widget
button = tk.Button(main_window, text="Click Me")
button.pack()





main_window.mainloop()
