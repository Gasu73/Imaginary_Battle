#Archivo Fight
import random
from utils.helpers import charactersDataG
import utils.helpers as helpers
import time


# VARIABLES GLOBALES
global CharMaquina, equipo_j, equipo_m, idx_j, idx_m, turno_jugador, Start
CharMaquina = []
equipo_j = []
equipo_m = []
idx_j = 0 #Personaje Actual Jugador
idx_m = 0 #Personaje Actual Maquina
turno_jugador = True



#funcion inicio de batalla
def fight_start():
    global CharMaquina, equipo_j, equipo_m, idx_j, idx_m, turno_jugador
    CharMaquina = []
    equipo_j = []
    equipo_m = []

    # Se escoge un valor aleatorio entre 0, 14 excluyendo los IDs del jugador
    CharMaquina = [14 + helpers.NivelG]
    def generar():
        if len(CharMaquina) == 3:
            return
        num = random.randint(0, 14)
        if num not in helpers.personajesElegidosG and num not in CharMaquina:
            CharMaquina.append(num)
        generar()
        
    generar()

    # Equipos
    equipo_j = [
        charactersDataG[helpers.personajesElegidosG[0]].copy(),
        charactersDataG[helpers.personajesElegidosG[1]].copy(),
        charactersDataG[helpers.personajesElegidosG[2]].copy()
    ]

    equipo_m = [
        charactersDataG[CharMaquina[0]].copy(),
        charactersDataG[CharMaquina[1]].copy(),
        charactersDataG[CharMaquina[2]].copy()
    ]

    idx_j = 0
    idx_m = 0
    turno_jugador = True





def capturar_personaje(equipo_origen, equipo_destino, idx):
    p = equipo_origen[idx]
    p["vida"] = charactersDataG[p["id"]]["vida"]
    equipo_destino.append(p)
    equipo_origen.pop(idx)



#Funcion de ataque de ambos bandos
def atacar(equipo_a, idx_a, equipo_d, idx_d):
    import gui.map_fight_area as map_fight_area
    
    #se asigna una variable con el atacante y defensa
    atacante = equipo_a[idx_a]
    defensor = equipo_d[idx_d]

    #guardar cual es el equipo atacante
    E_atacante = "Jugador" if equipo_a is equipo_j else "Máquina"

    #calculos de daño y vida restante
    daño = atacante["ataque"] - defensor["defensa"]
    if daño < 1:
        daño = 1

    defensor["vida"] -= daño

    if defensor["vida"] < 0:
        defensor["vida"] = 0

    from gui.map_fight_area import cargar_imagenes
    if not equipo_m == []:
        cargar_imagenes()

    def despues_de_daño():
        global turno_jugador, idx_j, idx_m
        # actualizar imágenes después de animación
        from gui.map_fight_area import cargar_imagenes
        cargar_imagenes()

        #Personaje Muere
        if defensor["vida"] == 0:

            #El equipo contrario adquiere el personaje muerto
            capturar_personaje(equipo_d, equipo_a, idx_d)

            #Todavia hay integrantes
            if len(equipo_d) > 0:
                if E_atacante == "Jugador":
                    idx_m = 0
                else:
                    idx_j = 0
                from gui.map_fight_area import cargar_imagenes
                cargar_imagenes()
            #Dar el ganador
            else:
                ganador = E_atacante
                if ganador == "Jugador":
                    helpers.NivelG += 1 #Subir de nivel

                import gui.map_fight_area as mf
                from gui.map_fight_area import mostrar_fin
                mf.canvasF.after(100, lambda: mostrar_fin(ganador)) #Label Ganador

        #Manejar turnos
        if E_atacante == "Jugador":
            turno_jugador = False
            turno_maquina()
        else:
            turno_jugador = True

    #Animacion de daño
    map_fight_area.mostrar_daño(daño, despues_de_daño)



#cambiar de personaje
def cambiar_personaje(equipo, idx_actual, nuevo_idx):
    if nuevo_idx < 0 or nuevo_idx >= len(equipo):
        return idx_actual, False
    if nuevo_idx == idx_actual:
        return idx_actual, False
    

    return nuevo_idx, True


#click del boton atacar
def accion_atacar():
    global idx_j, idx_m, turno_jugador
    if not turno_jugador:
        return
    atacar(equipo_j, idx_j, equipo_m, idx_m)



#cambiar de personaje jugador
def accion_cambiar(nuevo):
    global idx_j, equipo_j
    
    idx_j, _ = cambiar_personaje(equipo_j, idx_j, nuevo)
    from gui.map_fight_area import cargar_imagenes
    cargar_imagenes()

#Turno de la maquina
def turno_maquina():
    global equipo_j, equipo_m, idx_j, idx_m, turno_jugador
    import gui.map_fight_area as mf
    if not equipo_j or not equipo_m:
        return

    accion = random.choice(["atacar", "cambiar"]) #eleccion de la maquina

    if accion == "cambiar" and len(equipo_m) > 1:
        #de la longitud del equipo_m se escoge un numero aleatorio y se excluye el idx actual

        opciones = list(range(len(equipo_m)))
        opciones.remove(idx_m)
        nuevo = random.choice(opciones)
        idx_m, _ = cambiar_personaje(equipo_m, idx_m, nuevo)

        from gui.map_fight_area import cargar_imagenes
        cargar_imagenes()

    def on_finish():
        atacar(equipo_m, idx_m, equipo_j, idx_j)

    mf.sleep(2000, on_finish) #funcion de espera
