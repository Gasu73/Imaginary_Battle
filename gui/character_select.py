from tkinter import *
from utils.helpers import cargar_img, setup_bg, show_frame, escribir_datos, charactersDataG
import csv

def create_character_select_screen(container, frames):
    frame = Frame(container)
    frames["choise"] = frame
    frame.place(relwidth=1, relheight=1)
    canvas = Canvas(frame, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    setup_bg(canvas, "main_bg.png")


    # traer los datos de los personajes
    characters = charactersDataG

    # boton info
    btn_info_img = cargar_img("buttons","info.png", size=(100, 100))
    info_id = canvas.create_image(0 , 0, image=btn_info_img)

    # boton atras
    btn_prev_img = cargar_img("buttons","previous_btn.png", size=(150, 100))
    prev_id = canvas.create_image(0 , 0, image=btn_prev_img)

    # Rectangulo de fondo
    info_panel = canvas.create_rectangle(0, 0, 0, 0, fill="white", outline="")
    
    # Imagen personaje grande
    preview_id = canvas.create_image(0, 0, anchor="n", image="")
    preview_photo = {"img": None}

    # texto personaje
    info_text = canvas.create_text(
        0, 0,
        text="Selecciona un personaje",
        anchor="center",
        font=("Arial", 14),
        fill="black" )
    
    btn_remove_img = cargar_img("buttons","quitar_btn.png", size=(280, 80)) 
    btn_select_img = cargar_img("buttons","select_btn.png", size=(280, 80))
    btn_notselect_img = cargar_img("buttons","notselect_btn.png", size=(280, 80))

    #variables
    global char_preview, btn_id_preview, char_select
    char_preview = -1
    char_buttons = [] # botones de personajes
    char_windows = [] # id de los botones 
    mini_photos = []  # guardar referencias de imágenes miniatura
    char_select = []  # personajes seleccionados

# boton seleccionar
    select_id = canvas.create_image(0 , 0, image="", anchor="s")
    
    def clic_select(event):
        if (char_preview in char_select):
            char_select.remove(char_preview)
            btn_id_preview.config(highlightthickness=0)
            canvas.itemconfig(select_id, image=btn_select_img)
            return
        
        if (char_preview != -1 and len(char_select) < 3):
            char_select.append(char_preview)
            btn_id_preview.config(highlightthickness=7)

            canvas.itemconfig(select_id, image=btn_remove_img)
            escribir_datos("p", char_select)

            return
        

        


    canvas.images = [btn_prev_img, btn_info_img, btn_notselect_img, btn_remove_img, btn_notselect_img]

    canvas.tag_bind(prev_id, "<Button-1>", lambda e: show_frame(frames, "main"))
    canvas.tag_bind(select_id, "<Button-1>", clic_select)



# Al precionar un personaje

    def select_character(index, b_id):
        global char_select, btn_id_preview, char_preview
        char_preview = index
        btn_id_preview = b_id

# Actualizar texto
        canvas.itemconfig(
            info_text,
            text=(
                f"Personaje: {characters[index]['nombre']}\n"
                f"Serie: {characters[index]['serie']}\n"
                f"Tipo: {characters[index]['tipo']}\n"
                f"HP: {characters[index]['vida']}\n"
                f"ATK: {characters[index]['ataque']}\n"
                f"DEF: {characters[index]['defensa']}"
            )
        )

# Cargar imagen grande del personaje
        preview_img = cargar_img("characters", f"c_{index + 1:03}.png", size=(450, 390))
        preview_photo["img"] = preview_img
        canvas.itemconfig(preview_id, image=preview_img)

        if index in char_select:
            canvas.itemconfig(select_id, image=btn_remove_img)

        elif not index in char_select and len(char_select)< 3:
            canvas.itemconfig(select_id, image=btn_select_img)
    
        else:
            canvas.itemconfig(select_id, image=btn_notselect_img)



# Crear 16 botones con su imagen

    def crear_botones(i):
        if(i==15):      #caso base
            return

        mini_img = cargar_img("characters", f"c_{i+1:03}.png", size=(150,150))
        mini_photos.append(mini_img)

        btn = Button(
            canvas,
            image=mini_img,
            bd=2,
            relief="solid",
            bg="red",
            highlightthickness=0,
        )

        btn.config(command=lambda i=i, b=btn: select_character(i, b))

        btn.image = mini_img

        btn_id = canvas.create_window(0, 0, window=btn)

        char_buttons.append(btn)
        char_windows.append(btn_id)

        return crear_botones(i+1)   #recursión
    
    crear_botones(0)
    

    # responsive


    def resize_btns(event):
        w = event.width
        h = event.height

        # Botón atrás
        canvas.coords(prev_id, w * 0.07, h * 0.07)


        # caja botones 
        zone_x = w * 0.02
        zone_y = h * 0.12
        zone_w = w * 0.52
        zone_h = h * 0.78

        # tamaño de cada boton en la caja
        cell_w = zone_w / 4
        cell_h = zone_h / 4

        # Reacomodar los 16 botones
        def pos_btn_char(i):
            if(i==15):
                return
            
            row = i // 4
            col = i % 4

            # Centro de la celda actual
            cell_center_x = zone_x + (col * cell_w) + (cell_w / 2)
            cell_center_y = zone_y + (row * cell_h) + (cell_h / 2)

            # Mover el botón al centro de su celda
            canvas.coords(char_windows[i], cell_center_x, cell_center_y)
            return pos_btn_char(i+1)
        pos_btn_char(0)


        # panel derecho informacion
        panel_x1 = w * 0.58
        panel_x2 = w * 0.92
        panel_y1 = h * 0.14
        panel_y2 = h * 0.93
        canvas.coords(info_panel, panel_x1, panel_y1, panel_x2, panel_y2)

        # centro del panel derecho
        panelC_x =(panel_x2 - panel_x1)/2 + panel_x1

        # imagen personaje grande
        canvas.coords(preview_id, panelC_x, panel_y1*1.2)

        # info texto
        text_y = (panel_y2 - panel_y1)/1.3 + panel_y1
        canvas.coords(info_text, panelC_x, text_y)

        # boton seleccionar
        canvas.coords(select_id, panelC_x, panel_y2)

        # info 
        canvas.coords(info_id, event.width * 0.95, event.height * 0.08)

    canvas.bind("<Configure>", resize_btns, add="+")


def create_avatar_select_screen(container, frames):
    frame = Frame(container)
    frames["avatar"] = frame
    frame.place(relwidth=1, relheight=1)
    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)
    setup_bg(canvas, "main_bg.png")


    cuadrado_img = cargar_img("buttons", "cuadrado_rojo.png", (220, 220))
    cuadrado_id = canvas.create_image(0, 0, anchor="center", image=cuadrado_img, state="hidden")
    
    global avatar_select
    avatar_select = 0

    avatar1_btn_img = cargar_img("buttons", "avatar_1.png", (200, 200))
    avatar1_id = canvas.create_image(0, 0, anchor="center", image=avatar1_btn_img)

    avatar2_btn_img = cargar_img("buttons", "avatar_2.png", (200, 200))
    avatar2_id = canvas.create_image(0, 0, anchor="center", image=avatar2_btn_img)

    avatar3_btn_img = cargar_img("buttons", "avatar_3.png", (200, 200))
    avatar3_id = canvas.create_image(0, 0, anchor="center", image=avatar3_btn_img)

    
    # boton atras
    btn_prev_img = cargar_img("buttons","previous_btn.png", size=(150, 100))
    prev_id = canvas.create_image(0 , 0, image=btn_prev_img)
    canvas.tag_bind(prev_id, "<Button-1>", lambda e: show_frame(frames, "main"))

    # boton info
    def click_info(event):
        print("info presionado")

    
    btn_info_img = cargar_img("buttons","info.png", size=(100, 100))
    info_id = canvas.create_image(0 , 0, image=btn_info_img)
    canvas.tag_bind(info_id, "<Button-1>", click_info)
    
    

    canvas.images = [avatar1_btn_img, avatar2_btn_img, avatar3_btn_img, cuadrado_img, btn_prev_img, btn_info_img]

    def click_avatar(event, i):
        canvas.itemconfig(cuadrado_id, state="normal")
        global avatar_select
        escribir_datos("a", i)
        avatar_select = i

        # Obtener tamaño actual del canvas
        w = canvas.winfo_width()
        h = canvas.winfo_height()

        x = w * 0.5
        y = h * 0.5

        # Mover el cuadrado
        if i == 1:
            canvas.coords(cuadrado_id, x*0.5, y)
        elif i == 2:
            canvas.coords(cuadrado_id, x*1.5, y)
        elif i == 3:
            canvas.coords(cuadrado_id, x, y)



    canvas.tag_bind(avatar1_id, "<Button-1>", lambda e: click_avatar(e, 1))
    canvas.tag_bind(avatar2_id, "<Button-1>", lambda e: click_avatar(e, 2))
    canvas.tag_bind(avatar3_id, "<Button-1>", lambda e: click_avatar(e, 3))


    def resize_btns(event):
        x = event.width*0.5
        y = event.height*0.5

        canvas.coords(avatar1_id, x*0.5, y)
        canvas.coords(avatar2_id, x*1.5, y)
        canvas.coords(avatar3_id, x, y)

        if avatar_select == 1:
            canvas.coords(cuadrado_id, x*0.5, y)

        if avatar_select == 2:
            canvas.coords(cuadrado_id, x*1.5, y)
        
        if avatar_select == 3:
            canvas.coords(cuadrado_id, x, y)

        # Botón atrás
        canvas.coords(prev_id,  event.width * 0.1,  event.height * 0.1)

        # info 
        canvas.coords(info_id, event.width * 0.95, event.height * 0.08)


    canvas.bind("<Configure>", resize_btns, add="+")
