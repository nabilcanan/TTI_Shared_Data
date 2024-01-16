import tkinter as tk


#  Jabil
def jabil_logic():
    # Create a new Toplevel window for Benchmark
    benchmark_window = tk.Toplevel()
    benchmark_window.title("Jabil Module")
    benchmark_window.geometry("600x400")

    # Add content specific to the Benchmark module
    label = tk.Label(benchmark_window, text="This is the Jabil module", font=("Verdana", 16))
    label.pack(pady=20)
