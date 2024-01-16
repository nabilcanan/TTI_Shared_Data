import tkinter as tk
from tkinter import ttk
from Benchmark import benchmark_logic


def open_customer_module(customer_name):
    if customer_name == "Benchmark":
        benchmark_logic()


def main():
    root = tk.Tk()
    root.title("TTI_CPN Comparison")
    root.geometry("1000x650")  # Set the initial size of the window

    # Configure style for the buttons
    style = ttk.Style()
    style.configure('TButton', font=('Times New Roman', 16), padding=10)

    # Creating a title label
    title_label = tk.Label(root, text="TTI Shared Data", font=("Arial", 24))
    title_label.pack(pady=20)

    # Create a frame that will contain the buttons
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
