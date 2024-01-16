import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD


# Function to be called when a file is dropped
def on_drop(_):
    success_label.config(text="File successfully dropped!")


def neotech_logic():
    # Create a new Toplevel window
    neotech_window = tk.Toplevel()
    neotech_window.title("Neotech Module")
    neotech_window.geometry("600x400")

    # Create a drop frame
    drop_frame = tk.Frame(neotech_window, width=400, height=100, bg='lightgrey')
    drop_frame.pack(pady=20)

    # Register the drop frame as a drop target and bind the drop event
    drop_frame.drop_target_register(DND_FILES)
    drop_frame.dnd_bind('<<Drop>>', on_drop)

    # Label to display success message
    global success_label
    success_label = tk.Label(neotech_window, text="", font=("Verdana", 12))
    success_label.pack(pady=10)

