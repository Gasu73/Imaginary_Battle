from tkinter import *
from utils.helpers import cargar_img, setup_bg, show_frame
from gui.character_select import create_character_select_screen


def create_main_screen(container, frames):
    frame = Frame(container)
    frames["main"] = frame
    frame.place(relwidth=1, relheight=1)

    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)

    setup_bg(canvas, "main_bg.png")

    btn_start_img = cargar_img("buttons","start_btn.png", size=(280, 70))
    btn_start = Button(canvas, image=btn_start_img,
                 command=lambda: show_frame(frames, "lobby"))
    btn_start.image = btn_start_img
    start_id = canvas.create_window(0, 0, window=btn_start, anchor="center")

    btn_characters_img = cargar_img("buttons","personajes_btn.png", size=(280, 190))
    btn_characters = Button(canvas, image=btn_characters_img,
                 command=lambda: show_frame(frames, "choise"))
    btn_characters.image = btn_characters_img
    characters_id = canvas.create_window(0, 0, window=btn_characters)

    btn_avatar_img = cargar_img("buttons","avatar_btn.png", size=(280, 190))
    btn_avatar = Button(canvas, image=btn_avatar_img,
                 command=lambda: show_frame(frames, "lobby"))
    btn_avatar.image = btn_avatar_img
    avatar_id = canvas.create_window(0, 0, window=btn_avatar)
    

    def resize_btns(event):
        # centro horizontal
        center_x = event.width * 0.5
        
        # fila superior (2 botones)
        canvas.coords(characters_id, center_x - 200, event.height * 0.55)
        canvas.coords(avatar_id, center_x + 200, event.height * 0.55)

        # botón inferior centrado
        canvas.coords(start_id, center_x, event.height * 0.75)

    canvas.bind("<Configure>", resize_btns, add="+")


def create_lobby_screen(container, frames):
    frame = Frame(container)
    frames["lobby"] = frame
    frame.place(relwidth=1, relheight=1)

    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)

    setup_bg(canvas, "lobby_bg.png")

    # Botón siguiente
    next_img = cargar_img("buttons","next_btn.png", size=(160, 90))
    next_btn = Button(canvas, image=next_img,
                      command=lambda: show_frame(frames, "choise"))
    next_btn.image = next_img
    next_id = canvas.create_window(0, 0, window=next_btn)

    # Botón atrás
    prev_img = cargar_img("buttons", "previous_btn.png", size=(160, 90))
    prev_btn = Button(canvas, image=prev_img,
                      command=lambda: show_frame(frames, "main"))
    prev_btn.image = prev_img
    prev_id = canvas.create_window(0, 0, window=prev_btn)

    def resize_btns(event):
        canvas.coords(next_id, event.width*0.9, event.height*0.5)
        canvas.coords(prev_id, event.width*0.9, event.height*0.7)

    canvas.bind("<Configure>", resize_btns, add="+")