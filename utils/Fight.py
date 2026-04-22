import random
from utils.helpers import charactersDataG
import utils.helpers as helpers
import time


# VARIABLES GLOBALES
Start = False
CharMaquina = []
equipo_j = []
equipo_m = []
idx_j = 0 #Personaje Actual Jugador
idx_m = 0 #Personaje Actual Maquina
turno_jugador = True



# START

def fight_start():
    global CharMaquina, equipo_j, equipo_m, idx_j, idx_m, turno_jugador, Start
    Start = True

    # Máquina
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

    idx_m = 0
    turno_jugador = True



# CAPTURA

def capturar_personaje(equipo_origen, equipo_destino, idx):
    p = equipo_origen[idx]
    p["vida"] = charactersDataG[p["id"]]["vida"]
    equipo_destino.append(p)
    equipo_origen.pop(idx)



# ATAQUE

def atacar(equipo_a, idx_a, equipo_d, idx_d):
    atacante = equipo_a[idx_a]
    defensor = equipo_d[idx_d]

    daño = atacante["ataque"] - defensor["defensa"]
    if daño < 0:
        daño = 0

    defensor["vida"] -= daño

    print(f"damage: {daño} \n", f"personaje: {equipo_d[idx_d]['nombre']}\n", f"vida: {equipo_d[idx_d]['vida']}\n")

    if defensor["vida"] < 0:
        defensor["vida"] = 0

    #PERSONAJE MUERE
    if defensor["vida"] == 0:
        capturar_personaje(equipo_d, equipo_a, idx_d)

        if len(equipo_d) > 0:
            idx_d = 0
            from gui.map_fight_area import cargar_sprites
            cargar_sprites()
        else:
            idx_d = None

    return idx_a, idx_d



# CAMBIAR

def cambiar_personaje(equipo, idx_actual, nuevo_idx):
    if nuevo_idx < 0 or nuevo_idx >= len(equipo):
        return idx_actual, False
    if nuevo_idx == idx_actual:
        return idx_actual, False
    

    return nuevo_idx, True




# ACCIONES

def accion_atacar():
    global idx_j, idx_m, turno_jugador

    if not turno_jugador:
        return

    idx_j, idx_m = atacar(equipo_j, idx_j, equipo_m, idx_m)
    turno_jugador = False
    time.sleep(4)
    turno_maquina()


def accion_cambiar(nuevo):
    global idx_j, equipo_j

    idx_j, _ = cambiar_personaje(equipo_j, idx_j, nuevo)
    from gui.map_fight_area import cargar_sprites
    cargar_sprites()


def turno_maquina():
    global equipo_j, equipo_m, idx_j, idx_m, turno_jugador

    if not equipo_j or not equipo_m:
        return

    accion = random.choice(["atacar", "cambiar"])

    if accion == "cambiar" and len(equipo_m) > 1:
        opciones = list(range(len(equipo_m)))
        opciones.remove(idx_m)
        nuevo = random.choice(opciones)
        idx_m, _ = cambiar_personaje(equipo_m, idx_m, nuevo)
        from gui.map_fight_area import cargar_sprites
        cargar_sprites()

    idx_m, idx_j = atacar(equipo_m, idx_m, equipo_j, idx_j)
    
    turno_jugador = True






    
            

    
            
        
    

