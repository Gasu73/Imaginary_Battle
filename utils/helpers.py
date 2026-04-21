import os
from PIL import Image, ImageTk
import csv


#variables globales del juego
global nombreG, personajesElegidosG, avatarElegidoG, charactersDataG, NivelG, PersonajeAct
PersonajeAct = -1
EnemigoAct = -1
NivelG = 1
nombreG=""
personajesElegidosG=[]
vidapersonajes=[]
avatarElegidoG=-1

charactersDataG = []


def escribir_datos(val = "", dato = any):
    global nombreG, avatarElegidoG, personajesElegidosG, PersonajeAct
    match val:
        case "n":
            nombreG = dato
            print(nombreG)
            return
        case "p":
            personajesElegidosG = dato
            print(personajesElegidosG)
            return
        case "a":
            avatarElegidoG = dato
            print(avatarElegidoG)
            return
        case "pa":
            PersonajeAct = dato
            print(PersonajeAct)
            return
        
    print("falta val")
    return




def extraer_personajes():
    with open("data/characters.csv", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        def extraer_chars():
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
                charactersDataG.append(personaje)
                extraer_chars()
            except:
                return
        extraer_chars()
            




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


