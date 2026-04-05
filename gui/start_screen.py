from tkinter import *
from utils.helpers import cargar_img, setup_bg, show_frame

def create_main_screen(container, frames):
    frame = Frame(container)
    frames["main"] = frame
    frame.place(relwidth=1, relheight=1)

    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)

    setup_bg(canvas, "main_bg.png")

    btn_img = cargar_img("buttons","next_btn.png", size=(160, 90))
    btn = Button(canvas, image=btn_img,
                 command=lambda: show_frame(frames, "lobby"))
    btn.image = btn_img
    btn_id = canvas.create_window(0, 0, window=btn)

    canvas.bind("<Configure>",
                lambda e: canvas.coords(btn_id, e.width*0.9, e.height*0.6),
                add="+")


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