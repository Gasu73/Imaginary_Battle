from tkinter import *
from utils.helpers import cargar_img, setup_bg, show_frame, datos_jugador
from gui.character_select import create_character_select_screen


def create_main_screen(container, frames):
    frame = Frame(container)
    frames["main"] = frame
    frame.place(relwidth=1, relheight=1)

    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)

    setup_bg(canvas, "main_bg.png")


    btn_start_img = cargar_img("buttons","start_btn.png", size=(280, 70))
    start_id = canvas.create_image(0 , 0, image=btn_start_img)

    btn_characters_img = cargar_img("buttons","personajes_btn.png", size=(280, 190))
    characters_id = canvas.create_image(0 , 0, image=btn_characters_img)

    btn_avatar_img = cargar_img("buttons","avatar_btn.png", size=(280, 190))
    avatar_id = canvas.create_image(0 , 0, image=btn_avatar_img)

    btn_info_img = cargar_img("buttons","info.png", size=(100, 100))
    info_id = canvas.create_image(0 , 0, image=btn_info_img)


    canvas.images = [btn_info_img, btn_characters_img, btn_avatar_img, btn_start_img]


    def click_info(event):
        print("info presionado")

    canvas.tag_bind(info_id, "<Button-1>", click_info)
    canvas.tag_bind(avatar_id, "<Button-1>", lambda e: show_frame(frames, "avatar"))
    canvas.tag_bind(characters_id, "<Button-1>", lambda e: show_frame(frames, "choise"))
    canvas.tag_bind(start_id, "<Button-1>", lambda e: show_frame(frames, "lobby"))
    
    def resize_btns(event):
        center_x = event.width * 0.5
        
        # personajes y avatar
        canvas.coords(characters_id, center_x - 200, event.height * 0.55)
        canvas.coords(avatar_id, center_x + 200, event.height * 0.55)

        # empezar
        canvas.coords(start_id, center_x, event.height * 0.75)

        # info (arriba derecha por ejemplo)
        canvas.coords(info_id, event.width * 0.95, event.height * 0.08)

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
