from tkinter import *
from utils.helpers import cargar_img, setup_bg

def create_character_select_screen(container, frames):
    frame = Frame(container)
    frames["choise"] = frame
    frame.place(relwidth=1, relheight=1)

    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)

    setup_bg(canvas, "choise_character_bg.png")

    # Acá va a ir la lógica de selección de personajes