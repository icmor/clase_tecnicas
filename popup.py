""" Create a popup window"""

import tkinter as tk

def popup(message):
    window = tk.Toplevel()
    window.title("")
    label = tk.Label(master=window, text=message)
    label.pack(fill=tk.BOTH, expand=True)
