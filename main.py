import tkinter as tk
from Benchmark import benchmark_logic
from Creation import creation_logic
from Flextronics import flextronics_logic
from Jabil import jabil_logic
from Kimball import kimball_logic
from Neotech import neotech_logic
from Plexus import plexus_logic
from Sanmina import sanmina_logic
# from Kauffman_Engineering import kauffman_logic
from SMTC import smtc_logic
from PIL import Image, ImageTk


def button_click(customer_name):
    # Functionality to be executed when a label/button is clicked
    open_customer_module(customer_name)


def update_background(canvas, frames, current=0, width=1000, height=650):
    frame = frames[current]
    # Use a dictionary to store a reference to the image, preventing garbage collection.
    if not hasattr(canvas, 'image_references'):
        canvas.image_references = {}  # Initialize if it doesn't exist
    # Store the reference with the current index
    canvas.image_references[current] = frame
    canvas.itemconfig("background", image=frame)
    current = (current + 1) % len(frames)
    canvas.after(100, update_background, canvas, frames, current, width, height)


def load_gif_frames(filename, width, height):
    frames = []
    with Image.open(filename) as im:
        while True:
            try:
                im.seek(im.tell())
                # Use Image.LANCZOS or another available filter directly
                frame_image = im.copy().resize((width, height), Image.LANCZOS)
                frames.append(ImageTk.PhotoImage(frame_image))
                im.seek(im.tell() + 1)
            except EOFError:
                break  # Exit the loop when there are no more frames.
    return frames


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
        "SMTC": smtc_logic,
        # "Kauffman Engineering": kauffman_logic
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
    root.geometry("1000x650")

    # Create canvas for GIF background and buttons
    canvas = tk.Canvas(root, width=1000, height=650)
    canvas.pack(fill="both", expand=True)

    # Load GIF frames
    frames = load_gif_frames("electro.gif", 1000, 650)

    # Create a canvas object for the GIF
    gif = canvas.create_image(0, 0, image=frames[0], anchor="nw",
                              tags="background")  # Anchor the image to the top-left corner

    # Start the GIF animation
    update_background(canvas, frames, width=1000, height=650)

    # Title above the buttons
    canvas.create_text(500, 50, text="TTI_Shared_Data", font=('Verdana', 24), fill='white')

    # Customers list
    customers = ["Benchmark", "Creation", "Flextronics", "Jabil", "Kimball", "Neotech", "Plexus", "Sanmina", "SMTC"]

    # Create buttons using text objects on the canvas, for each individual button
    button_y = 100  # Adjust starting y position for the first button if needed
    button_height = 40  # Height of the button
    button_width = 300  # Width of the button
    for customer in customers:
        # Create rectangle as button background
        btn_bg = canvas.create_rectangle(500 - button_width // 2, button_y - button_height // 2,
                                         500 + button_width // 2, button_y + button_height // 2,
                                         fill='grey', outline='white', tags=customer)
        # Create text on top of the rectangle
        btn_text = canvas.create_text(500, button_y, text=customer, font=('Verdana', 16), fill='white', tags=customer)
        # Bind the click event to the rectangle and text
        canvas.tag_bind(customer, '<Button-1>', lambda event, name=customer: button_click(name))
        button_y += 60  # Increment y position for the next button thus will provide a clear overview of the next coming buttons

    root.mainloop()


if __name__ == "__main__":
    main()
