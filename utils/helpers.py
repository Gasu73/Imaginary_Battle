import os
from PIL import Image, ImageTk
import csv

global nombreG, personajesG, avatarG, characters
nombreG=""
personajesG=[]
avatarG=-1
characters = []

def datos_jugador(val = "", nombre="", personajes=[], avatar=-1,):
    global nombreG, personajesG, avatarG
    match val:
        case "n":
            return nombreG
        case "p":
            return personajesG
        case "a":
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

def extraer_personajes():
    with open("data/characters.csv", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        def extraer_datos():
            try:
                fila = next(lector)

                personaje = {
                    "id": int(fila["id"]),
                    "nombre": fila["nombre"],
                    "serie": fila["serie"],
                    "tipo": fila["tipo"],
                    "vida": int(fila["vida"]),
                    "ataque": int(fila["ataque"]),
                    "defensa": int(fila["defensa"])
                }
                characters.append(personaje)
                extraer_datos()
            except:
                return
            
        extraer_datos()

def personajes(n = -1):
    if n == -1:
        return characters
    return characters[n]




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


