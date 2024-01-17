import tkinter as tk
from tkinter import ttk
from Benchmark import benchmark_logic
from Creation import creation_logic
from Flextronics import flextronics_logic
from Jabil import jabil_logic
from Kimball import kimball_logic
from Neotech import neotech_logic
from Plexus import plexus_logic
from Sanmina import sanmina_logic
from SMTC import smtc_logic
import tkinterdnd2


def open_customer_module(customer_name):
    # Define a dictionary mapping customer names to their corresponding functions
    customer_logic = {
        "Benchmark": benchmark_logic,
        "Creation": creation_logic,
        "Flextronics": flextronics_logic,
        "Jabil": jabil_logic,
        "Kimball": kimball_logic,
        "Neotech": neotech_logic,
        "Plexus": plexus_logic,
        "Sanmina": sanmina_logic,
        "SMTC": smtc_logic
    }

    # Get the corresponding function based on customer name and call it
    logic_function = customer_logic.get(customer_name)
    if logic_function:
        logic_function()
    else:
        # Handle the case where the customer name is not found
        print(f"Customer '{customer_name}' not recognized.")


def main():
    root = tk.Tk()
    root.title("TTI_CPN Comparison")
    root.geometry("1000x650")  # Set the initial size of the window

    # Configure style for the buttons
    style = ttk.Style()
    style.configure('TButton', font=('Verdana', 16), padding=10)

    # Creating a title label
    title_label = tk.Label(root, text="TTI Shared Data", font=("Verdana", 24))
    title_label.pack(pady=20)

    # Create a frame that will contain the buttons for each customer
    buttons_frame = tk.Frame(root)
    buttons_frame.pack()

    # Create buttons for each customer and add them to the buttons frame
    customers = ["Benchmark", "Creation", "Flextronics", "Jabil", "Kimball", "Neotech", "Plexus", "Sanmina", "SMTC"]
    for customer in customers:
        button = ttk.Button(buttons_frame, text=customer, command=lambda c=customer: open_customer_module(c))
        button.pack(pady=5, fill='x', padx=200)

    root.mainloop()


if __name__ == "__main__":
    main()