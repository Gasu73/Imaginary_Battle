import os
from PIL import Image, ImageTk
import csv


# Variables globales del juego (estado compartido entre módulos)
global nombreG, personajesElegidosG, avatarElegidoG, charactersDataG, NivelG, PersonajeAct, back, score

PersonajeAct = -1          # índice del personaje actual del jugador
EnemigoAct = -1            # índice del enemigo actual
NivelG = 1                 # nivel actual
nombreG = ""               # nombre del jugador
personajesElegidosG = []   # lista de IDs de personajes elegidos
vidapersonajes = []        
avatarElegidoG = -1        # avatar seleccionado
back_info = "main"         # pantalla anterior
score = 0                  # puntaje

charactersDataG = []       # lista con datos de personajes (cargados desde CSV)


# Función para modificar variables globales según una clave
def escribir_datos(val = "", dato = any):
    global nombreG, avatarElegidoG, personajesElegidosG, PersonajeAct

    match val:
        case "n":   # nombre
            nombreG = dato
            print(nombreG)
            return
        case "p":   # personajes seleccionados
            personajesElegidosG = dato
            print(personajesElegidosG)
            return
        case "a":   # avatar
            avatarElegidoG = dato
            print(avatarElegidoG)
            return
        case "pa":  # personaje activo
            PersonajeAct = dato
            print(PersonajeAct)
            return
        
    print("falta val")
    return


# Lee el archivo CSV y carga los personajes en charactersDataG
def extraer_personajes():
    with open("data/characters.csv", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        # Uso de recursividad para recorrer el archivo
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
                extraer_chars()  # llamada recursiva

            except:
                # termina cuando no hay más filas
                return

        extraer_chars()


# Carga una imagen desde la carpeta assets
def cargar_img(carpeta, nombre, size=None):
    ruta = os.path.join('assets', carpeta, nombre)

    # Verifica que la imagen exista
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encuentra la imagen: {ruta}")

    img = Image.open(ruta)

    # Redimensiona si se especifica tamaño
    if size:
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)  # formato para Tkinter

    return img  # devuelve PIL si no se redimensiona


# Cambia de frame (pantalla)
def show_frame(frames, name):
    frames[name].tkraise()


# Configura un fondo dinámico en un Canvas
def setup_bg(canvas, image_name):
    bg_PIL = cargar_img("backgrounds", image_name)
    bg_img = ImageTk.PhotoImage(bg_PIL)

    # Inserta imagen en el canvas
    bg_id = canvas.create_image(0, 0, anchor='nw', image=bg_img)
    canvas.bg_img = bg_img  # referencia para evitar garbage collection

    # Redimensiona el fondo cuando cambia el tamaño de la ventana
    def resize(event):
        nueva = bg_PIL.resize((event.width, event.height), Image.LANCZOS)
        img = ImageTk.PhotoImage(nueva)
        canvas.bg_img = img
        canvas.itemconfig(bg_id, image=img)

    canvas.bind("<Configure>", resize)

