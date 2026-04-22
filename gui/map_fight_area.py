from tkinter import *
from utils.helpers import cargar_img, setup_bg, show_frame, escribir_datos
from gui.character_select import create_character_select_screen
import utils.Fight as Fight
import utils.helpers as helpers

def create_map_screen(container, frames):
    frame = Frame(container)
    frames["map"] = frame
    frame.place(relwidth=1, relheight=1)
    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)
    setup_bg(canvas, "map_bg.png")

    select_pl_img = cargar_img("buttons","select_pl_btn.png", size=(120, 100))
    lugar1_id = canvas.create_image(0, 0, anchor="center", image=select_pl_img)
    lugar2_id = canvas.create_image(0, 0, anchor="center", image=select_pl_img)
    lugar3_id = canvas.create_image(0, 0, anchor="center", image=select_pl_img)
    lugar4_id = canvas.create_image(0, 0, anchor="center", image=select_pl_img)
    lugar5_id = canvas.create_image(0, 0, anchor="center", image=select_pl_img)

    

    def click():
        create_choose_screen(container, frames)
        show_frame(frames, "choose")



    canvas.tag_bind(lugar1_id, "<Button-1>",lambda e: click())
    canvas.tag_bind(lugar2_id, "<Button-1>",lambda e: click())
    canvas.tag_bind(lugar3_id, "<Button-1>",lambda e: click())
    canvas.tag_bind(lugar4_id, "<Button-1>",lambda e: click())
    canvas.tag_bind(lugar5_id, "<Button-1>",lambda e: click())

    canvas.images = select_pl_img

    #canvas.tag_bind(avatar1_id, "<Button-1>", lambda e: click_avatar(e, 1))

    def resize_btns(event):
        x = event.width*0.5
        y = event.height*0.5

 
        canvas.coords(lugar1_id, x*0.30, y*1.4) #
        canvas.coords(lugar2_id, x*0.69, y*1.12) #
        canvas.coords(lugar3_id, x*1.1, y) #
        canvas.coords(lugar4_id, x*1.456, y*0.875) #
        canvas.coords(lugar5_id, x*1.79, y*0.46) #


    canvas.bind("<Configure>", resize_btns, add="+")

global char_ids, canvasC, CharEn_id, CharPl_id, canvasF

def create_choose_screen(container, frames):
    global char_ids, canvasC
    frame = Frame(container)
    frames["choose"] = frame
    frame.place(relwidth=1, relheight=1)

    canvasC = Canvas(frame)
    canvasC.pack(fill="both", expand=True)
    setup_bg(canvasC, f"arena_{helpers.NivelG}.png")

    Fight.fight_start()


    # SELECCIÓN
    char_select = -1 

    cuadrado_img = cargar_img("buttons", "cuadrado_rojo.png", (220, 220))
    cuadrado_id = canvasC.create_image(0, 0, anchor="center", image=cuadrado_img, state="hidden")

    # Botón seleccionar
    btn_select_img = cargar_img("buttons", "select_btn.png", size=(200, 120))
    select_id = canvasC.create_image(0, 0, image=btn_select_img, anchor="center")

    canvasC.images = [btn_select_img, cuadrado_img]
    
    char1_id = canvasC.create_image(0, 0, anchor="center", image="")
    char2_id = canvasC.create_image(0, 0, anchor="center", image="")
    char3_id = canvasC.create_image(0, 0, anchor="center", image="")
    char4_id = canvasC.create_image(0, 0, anchor="center", image="")
    char5_id = canvasC.create_image(0, 0, anchor="center", image="")

    

    char_ids = [char1_id, char2_id, char3_id, char4_id, char5_id]

    opciones(Fight.equipo_j)

    # =========================
    # EVENTOS
    # =========================
    def click_personaje(event, i):
        nonlocal char_select

        char_select = i
        canvasC.itemconfig(cuadrado_id, state="normal")

        w = canvasC.winfo_width()
        h = canvasC.winfo_height()

        x = w * 0.5
        y = h * 0.5

        if i == 0:
            canvasC.coords(cuadrado_id, x*0.5, y)
        elif i == 1:
            canvasC.coords(cuadrado_id, x, y)
        elif i == 2:
            canvasC.coords(cuadrado_id, x*1.5, y)
        elif i == 3:
            canvasC.coords(cuadrado_id, x/3, y*1.5)
        elif i == 4:
            canvasC.coords(cuadrado_id, x*2/3, y*1.5)

    def click_select(event):
        if char_select == -1:
            print("Selecciona un personaje primero")
            return

        # inicia el combate con el personaje elegido
        create_fight_screen(container, frames)
        Fight.accion_cambiar(char_select)
        cargar_sprites()
        show_frame(frames, "fight")

   
    # BINDS
    canvasC.tag_bind(char1_id, "<Button-1>", lambda e: click_personaje(e, 0))
    canvasC.tag_bind(char2_id, "<Button-1>", lambda e: click_personaje(e, 1))
    canvasC.tag_bind(char3_id, "<Button-1>", lambda e: click_personaje(e, 2))
    canvasC.tag_bind(char4_id, "<Button-1>", lambda e: click_personaje(e, 3))
    canvasC.tag_bind(char5_id, "<Button-1>", lambda e: click_personaje(e, 4))
    canvasC.tag_bind(select_id, "<Button-1>", click_select)

   
    # RESIZE
    def resize_btns(event):
        x = event.width * 0.5
        y = event.height * 0.5

        canvasC.coords(char1_id, x*0.5, y)
        canvasC.coords(char2_id, x, y)
        canvasC.coords(char3_id, x*1.5, y)
        canvasC.coords(char4_id, x/3, y*1.5)
        canvasC.coords(char5_id, x*2/3, y*1.5)

        # Mantener selección al redimensionar
        if char_select == 0:
            canvasC.coords(cuadrado_id, x*0.5, y)
        elif char_select == 1:
            canvasC.coords(cuadrado_id, x, y)
        elif char_select == 2:
            canvasC.coords(cuadrado_id, x*1.5, y)
        elif char_select == 3:
            canvasC.coords(cuadrado_id, x/3, y*1.5)
        elif char_select == 4:
            canvasC.coords(cuadrado_id, x*2/3, y*1.5)

        # Botón seleccionar
        canvasC.coords(select_id, x * 1.75, y * 1.75)


    canvasC.bind("<Configure>", resize_btns, add="+")

def opciones(lista, n=0):
    global char_ids, canvasC
    # condición de salida
    if n == 5:
        return
    
    if n >= len(lista):
        canvasC.itemconfig(char_ids[n], image="")

    else:
        personaje = lista[n]

        char_img = cargar_img("characters", f"c_{personaje['id']:03}.png", (200, 200))

        canvasC.itemconfig(char_ids[n], image=char_img)

        # guardar referencia
        if char_img not in canvasC.images:
            canvasC.images.append(char_img)

    opciones(lista, n + 1)


def create_fight_screen(container, frames):
    global CharEn_id, CharPl_id, canvasF
    frame = Frame(container)
    frames["fight"] = frame
    frame.place(relwidth=1, relheight=1)
    canvasF = Canvas(frame)
    canvasF.pack(fill="both", expand=True)
    setup_bg(canvasF, f"arena_{helpers.NivelG}.png")


    #btn cambiar
    cambiar_img = cargar_img("buttons", "cambiar_btn.png", size=(200, 100))
    cambiar_id = canvasF.create_image(0, 0, anchor="s", image=cambiar_img)

    #btn atacar
    atacar_img = cargar_img("buttons", "atacar_btn.png", size=(200, 100))
    atacar_id = canvasF.create_image(0, 0, anchor="s", image=atacar_img)


    #cargar img al canvas
    canvasF.images = [cambiar_img, atacar_img]

     #Personaje jugador
    CharPl_id = canvasF.create_image(0, 0, anchor="s", image="")

    #Personaje Maquina 
    CharEn_id = canvasF.create_image(0, 0, anchor="s", image="")
    cargar_sprites()

    #click atacar
    def click_atacar():
        Fight.accion_atacar()

    #click cambiar
    def click_cambiar():
        opciones(Fight.equipo_j)
        show_frame(frames, "choose")

    #Llamadas a los botones
    canvasF.tag_bind(cambiar_id, "<Button-1>", lambda e: click_cambiar())
    canvasF.tag_bind(atacar_id, "<Button-1>", lambda e: click_atacar())

    
    #resize
    def resize_btns(event):
        x = event.width*0.5
        y = event.height*0.5

        canvasF.coords(CharPl_id, x * 0.6, y*1.6)
        canvasF.coords(CharEn_id, x * 1.4, y*1.6)

        canvasF.coords(cambiar_id, x * 0.75, y*1.8)
        canvasF.coords(atacar_id, x * 1.25, y*1.8)


    canvasF.bind("<Configure>", resize_btns, add="+")

def cargar_sprites():
    global CharEn_id, CharPl_id, canvasF
    CharEn_img = cargar_img("models", f"e_{Fight.equipo_m[Fight.idx_m]['id']:03}.png", size=(230, 450))
    CharPL_img = cargar_img("models", f"c_{Fight.equipo_j[Fight.idx_j]['id']:03}.png", size=(230, 450))
    canvasF.images.append(CharEn_img)
    canvasF.images.append(CharPL_img)
    canvasF.itemconfig(CharEn_id, image=CharEn_img)
    canvasF.itemconfig(CharPl_id, image=CharPL_img)

    return 


    

