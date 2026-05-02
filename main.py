from tkinter import *
from gui.start_screen import create_main_screen, create_info_screen
from gui.character_select import create_character_select_screen, create_avatar_select_screen
from gui.map_fight_area import fin_juego
from utils.helpers import show_frame, extraer_personajes
import winsound

root = Tk()
root.title("Imaginary_Battle")
root.geometry("1280x720")      
root.minsize(1000, 650)        # tamaño mínimo para que no se rompa el layout
root.state("zoomed")           # maximizar al inicio

frames = {}                    # Lista donde se guardan las pantallas
container = Frame(root)        # Frame principal
container.pack(fill="both", expand=True)

# Crear pantallas

extraer_personajes()
create_character_select_screen(container, frames)
create_avatar_select_screen(container, frames)
create_main_screen(container, frames)
create_info_screen(container, frames)
fin_juego(container, frames)


winsound.PlaySound(
    "assets/musica.wav",
    winsound.SND_ASYNC | winsound.SND_LOOP
)

show_frame(frames, "main")
root.mainloop()
