import os
from PIL import Image, ImageTk
global nombreG, personajesG, avatarG
nombreG=""
personajesG=[]
avatarG=-1

def datos_jugador(val = "", nombre="", personajes=[], avatar=-1,):
    global nombreG, personajesG, avatarG
    match val:
        case "n":
            return nombreG
        case "p":
            return personajesG
        case "n":
            return avatarG
    if nombre !="":
        nombreG = nombre
        print(nombreG)
    if personajes != []:
        personajesG = personajes
        print(personajesG)
    if avatar != -1:
        avatarG = avatar
        print(avatarG)
    return




def cargar_img(carpeta, nombre, size=None):
    ruta = os.path.join('assets', carpeta, nombre)
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encuentra la imagen: {ruta}")
    img = Image.open(ruta)
    if size:
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    return img

def show_frame(frames, name):
    frames[name].tkraise()

def setup_bg(canvas, image_name):
    bg_PIL = cargar_img("backgrounds", image_name)
    bg_img = ImageTk.PhotoImage(bg_PIL)
    bg_id = canvas.create_image(0, 0, anchor='nw', image=bg_img)
    canvas.bg_img = bg_img

    def resize(event):
        nueva = bg_PIL.resize((event.width, event.height), Image.LANCZOS)
        img = ImageTk.PhotoImage(nueva)
        canvas.bg_img = img
        canvas.itemconfig(bg_id, image=img)

    canvas.bind("<Configure>", resize)


