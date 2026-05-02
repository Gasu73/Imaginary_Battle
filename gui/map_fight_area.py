#Archivo map_fight_area
from tkinter import *
from utils.helpers import cargar_img, setup_bg, show_frame, escribir_datos
from gui.character_select import create_character_select_screen
import utils.Fight as Fight
import utils.helpers as helpers

def create_map_screen(container, frames):
    global lugar_id, Mcanvas
    frame = Frame(container)
    frames["map"] = frame
    frame.place(relwidth=1, relheight=1)

    Mcanvas = Canvas(frame)
    Mcanvas.pack(fill="both", expand=True)

    setup_bg(Mcanvas, "map_bg.png")

    NivelG = helpers.NivelG


    # Imagen del botón
    select_pl_img = cargar_img("buttons", "select_pl_btn.png", size=(120, 100))
    

    lugar_id = Mcanvas.create_image(0, 0, anchor="center", image=select_pl_img)

    # Guardar referencia de la imagen (importante)
    Mcanvas.images = [select_pl_img]

    # Acción al hacer click
    def click():
        create_choose_screen(container, frames)
        show_frame(frames, "choose")

    Mcanvas.tag_bind(lugar_id, "<Button-1>", lambda e: click())

    # Posiciones de los niveles (en orden)
    posiciones = [
        (0.30, 1.4),
        (0.69, 1.12),
        (1.1, 1),
        (1.456, 0.875),
        (1.79, 0.46)
    ]

    # Ajuste dinámico al tamaño de pantalla
    def resize_btns(event):
        x = event.width * 0.5
        y = event.height * 0.5
        
        px, py = posiciones[NivelG - 1]
        Mcanvas.coords(lugar_id, x * px, y * py)

    Mcanvas.bind("<Configure>", resize_btns, add="+")


def map_update():
    global lugar_id, Mcanvas
    posiciones = [
        (0.30, 1.4),
        (0.69, 1.12),
        (1.1, 1),
        (1.456, 0.875),
        (1.79, 0.46)
    ]
    #Imagen Ganador
    
    # Ajuste dinámico al tamaño de pantalla
    
    x = canvasC.winfo_width()
    y = canvasC.winfo_height()

    x = x*0.5
    y = y*0.5

    px, py = posiciones[helpers.NivelG - 1]
    Mcanvas.coords(lugar_id, x * px, y * py)



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

    
    # EVENTOS
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
            canvasC.coords(cuadrado_id, x*2/3, y*1.5)
        elif i == 4:
            canvasC.coords(cuadrado_id, x*4/3, y*1.5)

    def click_select(event):
        if char_select == -1:
            print("Selecciona un personaje primero")
            return

        # inicia el combate con el personaje elegido
        create_fight_screen(container, frames)
        Fight.accion_cambiar(char_select)
        cargar_imagenes()
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
        canvasC.coords(char4_id, x*2/3, y*1.5)
        canvasC.coords(char5_id, x*4/3, y*1.5)

        # Mantener selección al redimensionar
        if char_select == 0:
            canvasC.coords(cuadrado_id, x*0.5, y)
        elif char_select == 1:
            canvasC.coords(cuadrado_id, x, y)
        elif char_select == 2:
            canvasC.coords(cuadrado_id, x*1.5, y)
        elif char_select == 3:
            canvasC.coords(cuadrado_id, x*2/3, y*1.5)
        elif char_select == 4:
            canvasC.coords(cuadrado_id, x*4/3, y*1.5)

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
    global CharEn_id, CharPl_id, IconEn_id, IconPL_id, canvasF, LabelV_En, LabelV_PL, Label_damage_id, framesG, Label_score
    framesG = frames
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

    #Personaje jugador Icono
    IconPL_id = canvasF.create_image(0, 0, anchor="center", image="")

    #Personaje Maquina Icono
    IconEn_id = canvasF.create_image(0, 0, anchor="center", image="")

    #Vida Jugador
    LabelV_PL = Label(canvasF, text="999", font=('Agency FB',20), bg="#174364", fg='white', borderwidth=10, justify='center', anchor="center")

    #Vida Maquina
    LabelV_En = Label(canvasF, text="999", font=('Agency FB',20), bg="#174364", fg='white', borderwidth=10, justify='center', anchor="center")

    #Label Daño
    Label_damage_id = canvasF.create_text(0, 0, text="", font=('Agency FB', 60), fill="white", anchor="center")

    #Label Score
    Label_score = Label(canvasF, text="", font=('Agency FB',20), bg="#174364", fg='white', borderwidth=10, justify='center', anchor="center")


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

    
    #Reajuste elementos del Canvas
    def resize_btns(event):
        x = event.width*0.5
        y = event.height*0.5

        canvasF.coords(CharPl_id, x * 0.6, y*1.6)
        canvasF.coords(CharEn_id, x * 1.4, y*1.6)

        canvasF.coords(cambiar_id, x * 0.75, y*1.8)
        canvasF.coords(atacar_id, x * 1.25, y*1.8)

        canvasF.coords(IconPL_id, x * 0.1, y*0.2)
        canvasF.coords(IconEn_id, x * 1.9, y*0.2)

        LabelV_PL.place(x=x*0.2, y=y*0.15)
        LabelV_En.place(x=x*1.7, y=y*0.15)

        Label_score.place(x=x, y=y*0.15)

        canvasF.coords(Label_damage_id, x, y)

    canvasF.bind("<Configure>", resize_btns, add="+")


#actualizar informacion de la pantalla
def cargar_imagenes():
    global CharEn_id, CharPl_id, IconPL_id, IconEn_id, canvasF, LabelV_En, LabelV_PL, Label_score
    CharEn_img = cargar_img("models", f"e_{Fight.equipo_m[Fight.idx_m]['id']:03}.png", size=(230, 450))
    CharPL_img = cargar_img("models", f"c_{Fight.equipo_j[Fight.idx_j]['id']:03}.png", size=(230, 450))

    Icon_En_img = cargar_img("characters", f"c_{Fight.equipo_m[Fight.idx_m]['id']:03}.png", size=(100, 100))
    Icon_PL_img = cargar_img("characters", f"c_{Fight.equipo_j[Fight.idx_j]['id']:03}.png", size=(100, 100))

    LabelV_PL.config(text=f"Vida: {Fight.equipo_j[Fight.idx_j]['vida']}")
    LabelV_En.config(text=f"Vida: {Fight.equipo_m[Fight.idx_m]['vida']}")

    Label_score.config(text=f"Puntaje: {helpers.score}")



    canvasF.images.append(CharEn_img)
    canvasF.images.append(CharPL_img)
    canvasF.images.append(Icon_En_img)
    canvasF.images.append(Icon_PL_img)
    canvasF.itemconfig(CharEn_id, image=CharEn_img)
    canvasF.itemconfig(CharPl_id, image=CharPL_img)
    canvasF.itemconfig(IconPL_id, image=Icon_PL_img)
    canvasF.itemconfig(IconEn_id, image=Icon_En_img)

#Mostrar Label con el daño 
def mostrar_daño(dmg, critico, on_finish=None):
    global Label_damage_id, canvasF
    canvasF.itemconfig(Label_damage_id, text=str(dmg))
    if critico:
        canvasF.itemconfig(Label_damage_id, fill = "red")
        
    x, y = canvasF.coords(Label_damage_id)

    def subir(step=0):
        if step > 10:
            canvasF.itemconfig(Label_damage_id, text="")
            canvasF.itemconfig(Label_damage_id, fill = "white")
            yM = canvasF.winfo_height()
            yM = yM*0.5

            #reset posicion
            canvasF.coords(Label_damage_id, x, yM)

            #llamada de regreso
            if on_finish:
                on_finish()
            
            return
        canvasF.coords(Label_damage_id, x, y - step * 5)
        canvasF.after(50, lambda: subir(step + 0.75))
    subir()
    

#Pantalla fin del juego
def fin_juego(container, frames):
    global about_id, Fcanvas
    frame = Frame(container)
    frames["fin"] = frame
    frame.place(relwidth=1, relheight=1)

    Fcanvas = Canvas(frame)
    Fcanvas.pack(fill="both", expand=True)

    setup_bg(Fcanvas, "lobby_bg.png")

    
    about_id = Fcanvas.create_text(
        0, 0,
        text="",
        font=('Agency FB', 50),
        fill='white',
        anchor="center",
        justify="center"
    )

    def resize_btns(event):
        center_x = event.width * 0.5
        center_y = event.height * 0.5

        # About
        Fcanvas.coords(about_id, center_x, center_y)


    #Cuando se produce un cambio en la pantalla se llama la funcion resize_btns
    Fcanvas.bind("<Configure>", resize_btns, add="+")




#funcion fin de la batalla
def mostrar_fin(ganador):
    global Label_damage_id, canvasF, framesG, about_id

    canvasF.itemconfig(Label_damage_id, text=f"¡{ganador} gana!")
    x, y = canvasF.coords(Label_damage_id)

    def subir(step=0):
        if step > 10:
            canvasF.itemconfig(Label_damage_id, text="")
            yM = canvasF.winfo_height()
            yM = yM*0.5

            canvasF.coords(Label_damage_id, x, yM)
            if helpers.NivelG <= 5:
                map_update()
                show_frame(framesG, "map")
            else:
                about = f"""Felicidades {helpers.nombreG}
            Terminaste el juego con una puntuacion de {helpers.score}
            """
                Fcanvas.itemconfig(about_id, text= about)
                show_frame(framesG, "fin")
            return
        canvasF.coords(Label_damage_id, x, y - step * 5)
        canvasF.after(50, lambda: subir(step + 0.25))
    subir()

#funcion de espera
def sleep(time, onfinish=None):
    global canvasF
    canvasF.after(time, lambda: onfinish())




