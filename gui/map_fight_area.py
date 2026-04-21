from tkinter import *
from utils.helpers import cargar_img, setup_bg, show_frame, escribir_datos
from gui.character_select import create_character_select_screen
from utils.Fight import fight

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
        fight()
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


def create_choose_screen(container, frames):
    from utils.helpers import NivelG, charactersDataG, personajesElegidosG
    from utils.Fight import CharEn_1, CharEn_2


    frame = Frame(container)
    frames["choose"] = frame
    frame.place(relwidth=1, relheight=1)
    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)
    setup_bg(canvas, f"arena_{NivelG}.png")

    
    print("frame avatar")

    cuadrado_img = cargar_img("buttons", "cuadrado_rojo.png", (220, 220))
    cuadrado_id = canvas.create_image(0, 0, anchor="center", image=cuadrado_img, state="hidden")
    
    global char_select
    char_select = 0

    per = personajesElegidosG

    char1_btn_img = cargar_img("characters", f"c_{per[0]+1:03}.png", (200, 200))
    char1_id = canvas.create_image(0, 0, anchor="center", image=char1_btn_img)

    char2_btn_img = cargar_img("characters", f"c_{per[1]+1:03}.png", (200, 200))
    char2_id = canvas.create_image(0, 0, anchor="center", image=char2_btn_img)

    char3_btn_img = cargar_img("characters", f"c_{per[2]+1:03}.png", (200, 200))
    char3_id = canvas.create_image(0, 0, anchor="center", image=char3_btn_img)

    # boton mapa
    btn_select_img = cargar_img("buttons","select_btn.png", size=(200, 120))
    select_id = canvas.create_image(0 , 0, image=btn_select_img, anchor="center")


    canvas.images = [char1_btn_img, char2_btn_img, char3_btn_img,btn_select_img, cuadrado_id]

    if CharEn_1["vivo"] == False:
        char4_btn_img = cargar_img("characters", f"c_{CharEn_1[0]:03}", (200, 200))
        char4_id = canvas.create_image(0, 0, anchor="center", image=char4_btn_img)
        canvas.images.append(char4_btn_img)

    if CharEn_2["vivo"] == False:
        char5_btn_img = cargar_img("characters", f"c_{CharEn_2[0]:03}", (200, 200))
        char5_id = canvas.create_image(0, 0, anchor="center", image=char5_btn_img)
        canvas.images.append(char5_btn_img)




    def click_personaje(event, i):
        canvas.itemconfig(cuadrado_id, state="normal")
        global char_select
        char_select = i

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
        elif i == 4:
            canvas.coords(cuadrado_id, w/3, y*1.5)
        elif i == 5:
            canvas.coords(cuadrado_id, x*(2/3), y*1.5)

    def click_select(event):
        create_fight_screen(container, frames)
        show_frame(frames, "fight")


    canvas.tag_bind(char1_id, "<Button-1>", lambda e: click_personaje(e, 1))
    canvas.tag_bind(char2_id, "<Button-1>", lambda e: click_personaje(e, 2))
    canvas.tag_bind(char3_id, "<Button-1>", lambda e: click_personaje(e, 3))
    canvas.tag_bind(select_id, "<Button-1>", lambda e: click_select(e))
    try:
        canvas.tag_bind(char4_id, "<Button-1>", lambda e: click_personaje(e, 4))
        canvas.tag_bind(char5_id, "<Button-1>", lambda e: click_personaje(e, 5))
    except:
        print("H")
    


    def resize_btns(event):
        x = event.width*0.5
        y = event.height*0.5

        canvas.coords(char1_id, x*0.5, y)
        canvas.coords(char2_id, x*1.5, y)
        canvas.coords(char3_id, x, y)
        # canvas.coords(char4_id, event.width*(1/3), y*1.5)
        # canvas.coords(char5_id, event.width*(2/3), y*1.5)


        if char_select == 1:
            canvas.coords(cuadrado_id, x*0.5, y)

        if char_select == 2:
            canvas.coords(cuadrado_id, x*1.5, y)
        
        if char_select == 3:
            canvas.coords(cuadrado_id, x, y)

        # if char_select == 4:
        #     canvas.coords(cuadrado_id, event.width*(1/3), y*1.5)

        # if char_select == 5:
        #     canvas.coords(cuadrado_id, event.width*(2/3), y*1.5)

        # boton mapa
        canvas.coords(select_id, x * 1.75, y * 1.75)


    canvas.bind("<Configure>", resize_btns, add="+")



def create_fight_screen(container, frames):
    from utils.helpers import NivelG, charactersDataG, personajesElegidosG
    from utils.Fight import CharEn_0 ,CharEn_1, CharEn_2, CharPl_0, CharPl_1, CharPl_2


    frame = Frame(container)
    frames["choose"] = frame
    frame.place(relwidth=1, relheight=1)
    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)
    setup_bg(canvas, f"arena_{NivelG}.png")



    #Personaje jugador
    CharPL_img = cargar_img("models", "c_001.png", size=(200, 600))
    CharPl_id = canvas.create_image(0, 0, anchor="center", image=CharPL_img)

    #Personaje Maquina 
    CharEn_img = cargar_img("models", "e_002.png", size=(200, 600))
    CharEn_id = canvas.create_image(0, 0, anchor="center", image=CharEn_img)

    #rectangulo cafe
    rectangulo_img = cargar_img("buttons", "rectangulo_cafe.png", size=(200, 600))
    rectangulo_id = canvas.create_image(0, 0, anchor="s", image=rectangulo_img)

    #btn cambiar
    cambiar_img = cargar_img("buttons", "cambiar_btn.png", size=(200, 600))
    cambiar_id = canvas.create_image(0, 0, anchor="s", image=cambiar_img)

    #btn atacar
    atacar_btn_img = cargar_img("buttons", "atacar_btn.png", size=(200, 600))
    atacar_id = canvas.create_image(0, 0, anchor="s", image=atacar_btn_img)


    #cargar img al canvas
    canvas.images = [CharPL_img, CharEn_img, rectangulo_img, cambiar_img, atacar_btn_img]

    #Llamadas a los botones
    canvas.tag_bind(cambiar_id, "<Button-1>", lambda e: show_frame(frames, "choise"))
    # canvas.tag_bind(atacar_id, "<Button-1>", lambda e: click_avatar(e, 2))
    # canvas.tag_bind(avatar3_id, "<Button-1>", lambda e: click_avatar(e, 3))

    
    #resize
    def resize_btns(event):
        x = event.width*0.5
        y = event.height*0.5

        canvas.coords(CharPl_id, x * 0.5, y* 1.5)
        canvas.coords(CharEn_id, x * 1.5, y* 1.5)

        canvas.coords(rectangulo_img, x, y*2)
        canvas.coords(cambiar_id, x * 0.25, y*2)
        canvas.coords(atacar_id, x * 1.25, y*2)

        


    canvas.bind("<Configure>", resize_btns, add="+")


    

