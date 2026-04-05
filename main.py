from tkinter import *
from gui.start_screen import create_main_screen, create_lobby_screen
from gui.character_select import create_character_select_screen
from utils.helpers import show_frame

root = Tk()
root.title("Imaginary_Battle")
root.state("zoomed")

frames = {}
container = Frame(root)
container.pack(fill="both", expand=True)

# Crear pantallas
create_main_screen(container, frames)
create_lobby_screen(container, frames)
create_character_select_screen(container, frames)

show_frame(frames, "main")
root.mainloop()

