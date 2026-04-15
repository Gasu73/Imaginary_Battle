from tkinter import *
from utils.helpers import cargar_img, setup_bg, show_frame, datos_jugador, personajes
from gui.character_select import create_character_select_screen


def create_main_screen(container, frames):
    frame = Frame(container)
    frames["main"] = frame
    frame.place(relwidth=1, relheight=1)
    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)
    setup_bg(canvas, "main_bg.png")

    # Label entrada del nombre
    Label_ingrese_img = cargar_img("titles", "ingrese_title.png", size=(700, 90))
    Label_ingrese_id = canvas.create_image(0 , 0, image=Label_ingrese_img, anchor="center")

    # Label entrada invalidad
    global after_id
    after_id = None

    L_invalida = Label(canvas, font=('Agency FB',20), fg='black')
    L_invalida_id = canvas.create_window(0, 0, anchor="center")
    canvas.itemconfig(L_invalida_id, state="hidden")


    # Entry nombre
    E_nombre = Entry(canvas, width=20, font=('Agency FB',24))
    E_nombre_id = canvas.create_window(0, 0, window=E_nombre, anchor="center")

    # boton empezar
    def click_empezar(event):
        global after_id
        texto_invalido = ""

        char = list(datos_jugador("p"))
        nombre = str(E_nombre.get())
        avatar = int(datos_jugador("a"))

        if (len(char) != 3):
            texto_invalido = "|Seleccione 3 personajes|"
        if (avatar == -1):
            texto_invalido = texto_invalido + "|Seleccione un avatar|"
        if (len(nombre) < 3):
            texto_invalido = texto_invalido + "|Ingrese un nombre valido|"

        if (len(char) == 3 and avatar != -1 and len(nombre) >= 3):
            datos_jugador("",nombre)
            create_lobby_screen(container, frames)
            show_frame(frames, "lobby")
            return
        
        if after_id:
            canvas.after_cancel(after_id)

        L_invalida.config(text=texto_invalido)
        canvas.itemconfig(L_invalida_id, window=L_invalida)
        canvas.itemconfig(L_invalida_id, state="normal",)
        
        after_id = canvas.after(5000, lambda: canvas.itemconfig(L_invalida_id, state="hidden"))
        
        print(texto_invalido)
        texto_invalido = ""
        return



    # boton empezar
    btn_start_img = cargar_img("buttons","start_btn.png", size=(280, 70))
    start_id = canvas.create_image(0 , 0, image=btn_start_img, anchor="center")

    #boton personajes
    btn_characters_img = cargar_img("buttons","personajes_btn.png", size=(280, 190))
    characters_id = canvas.create_image(0 , 0, image=btn_characters_img, anchor="nw")

    # boton avatar
    btn_avatar_img = cargar_img("buttons","avatar_btn.png", size=(280, 190))
    avatar_id = canvas.create_image(0 , 0, image=btn_avatar_img, anchor="ne")

    # boton info
    btn_info_img = cargar_img("buttons","info.png", size=(100, 100))
    info_id = canvas.create_image(0 , 0, image=btn_info_img)


    canvas.images = [btn_info_img, btn_characters_img, btn_avatar_img, btn_start_img, Label_ingrese_img]


    def click_info(event):
        print("info presionado")

    canvas.tag_bind(info_id, "<Button-1>", click_info)
    canvas.tag_bind(avatar_id, "<Button-1>", lambda e: show_frame(frames, "avatar"))
    canvas.tag_bind(characters_id, "<Button-1>", lambda e: show_frame(frames, "choise"))
    canvas.tag_bind(start_id, "<Button-1>", click_empezar)
    
    def resize_btns(event):
        center_x = event.width * 0.5
        center_y = event.height * 0.5

        # personajes y avatar
        canvas.coords(characters_id, center_x * 0.5, center_y)
        canvas.coords(avatar_id, center_x * 1.5, center_y)

        # empezar
        canvas.coords(start_id, center_x, center_y * 1.75)

        # info 
        canvas.coords(info_id, event.width * 0.95, event.height * 0.08)
        
        # label ingresar
        canvas.coords(Label_ingrese_id, center_x, center_y * 0.25)

        # Entry nombre
        canvas.coords(E_nombre_id, center_x, center_y * 0.5)

        # Entrada invalida
        canvas.coords(L_invalida_id, center_x, center_y * 1.625)



    canvas.bind("<Configure>", resize_btns, add="+")


def create_lobby_screen(container, frames):
    frame = Frame(container)
    frames["lobby"] = frame
    frame.place(relwidth=1, relheight=1)
    canvas = Canvas(frame)
    canvas.pack(fill="both", expand=True)
    setup_bg(canvas, "lobby_bg.png")


    select_char = []
    nombre = datos_jugador("n")
    avatar = datos_jugador("a")

    def selectC(i):
        if i == 3:
            return
        
        select_char.append(datos_jugador("p")[i])
        return selectC(i+1)
    selectC(0)
    


    # avatar img
    avatar_img = cargar_img("buttons", f"avatar_{avatar}.png", (150, 150))
    avatar_id = canvas.create_image(0 , 0, image=avatar_img, anchor="w")

    #nombre
    L_nombre = Label(canvas, font=('Agency FB',20), fg="black", text=nombre)
    L_nombre_id = canvas.create_window(0, 0, anchor="center", window=L_nombre)
  
    #boton info
    btn_info_img = cargar_img("buttons","info.png", size=(100, 100))
    info_id = canvas.create_image(0 , 0, image=btn_info_img)
    
    # boton mapa
    btn_mapa_img = cargar_img("buttons","map_btn.png", size=(150, 100))
    mapa_id = canvas.create_image(0 , 0, image=btn_mapa_img, anchor="center")

    #boton regresar
    btn_regresar_img = cargar_img("buttons","previous_btn.png", size=(150, 100))
    regresar_id = canvas.create_image(0 , 0, image=btn_regresar_img, anchor="center")


    canvas.images = [btn_info_img, btn_regresar_img, btn_mapa_img, avatar_img]

    #img avatar
    char_ids = []
    

    def crear_char(i):
        if(i==3):      #caso base
            return


        #boton regresar
        btn_char_img = cargar_img("characters",f"c_{select_char[i]+1:03}.png", size=(150, 150))
        print(select_char[i]+1)
        char_id = canvas.create_image(0 , 0, image=btn_char_img, anchor="center")


        canvas.images.append(btn_char_img)
        char_ids.append(char_id)

        return crear_char(i+1)   #recursión
    
    crear_char(0)




    


    def resize_btns(event):
        center_x = event.width * 0.5
        center_y = event.height * 0.5
        borde_x1 = event.width * 0.65

        # personajes y avatar
        def posChar(i):
            if i == 3:
                return
            
            canvas.coords(char_ids[i], borde_x1*(i+1)/4, center_y)
            return posChar(i+1)
        posChar(0)

        # boton mapa
        canvas.coords(mapa_id, center_x * 1.75, center_y * 1.75)

        # boton info 
        canvas.coords(info_id, event.width * 0.95, event.height * 0.08)
        
        # boton regresar
        canvas.coords(regresar_id, center_x * 0.25, center_y * 1.75)

        # label nombre
        canvas.coords(L_nombre_id, center_x * 0.25 , center_y * 0.25)

        # Imagen Avatar
        canvas.coords(avatar_id, event.width * 0.01, center_y * 0.25)





    canvas.bind("<Configure>", resize_btns, add="+")




    








