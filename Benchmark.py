import tkinter as tk
from tkinter import filedialog
import pandas as pd


def select_and_load_excel():
    # Open a dialog to select an Excel file
    file_path = filedialog.askopenfilename(title="Select CPN Excel File",
                                           filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if file_path:
        # Load the selected Excel file into a Pandas DataFrame
        try:
            df = pd.read_excel(file_path)
            print(df)  # Printing the DataFrame to the console, replace with your own display logic
        except Exception as e:
            print(f"Error loading Excel file: {e}")


def benchmark_logic():
    # Create a new Toplevel window for Benchmark
    benchmark_window = tk.Toplevel()
    benchmark_window.title("Benchmark Module")
    benchmark_window.geometry("600x400")

    # Add content specific to the Benchmark module
    label = tk.Label(benchmark_window, text="This is the Benchmark module", font=("Verdana", 24))
    label.pack(pady=20)

    # Add content specific to the Benchmark module
    label = tk.Label(benchmark_window, text="Here select the BOM file that you ran beforehand", font=("Verdana", 16))
    label.pack(pady=20)

    # Button for selecting and loading Excel file this load the CPN Excel file that we want
    # Added to the correct Excel file and loaded them into pandas to display them into the run control
    load_button = tk.Button(benchmark_window, text="Select CPN Excel File", command=select_and_load_excel)
    load_button.pack(pady=10)
