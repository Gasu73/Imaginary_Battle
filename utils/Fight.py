
import random


def fight():
    from utils.helpers import personajesElegidosG, charactersDataG, NivelG

    fight = True
    global CharJugador, CharMaquina, CharEn_0 ,CharEn_1, CharEn_2, CharPl_0, CharPl_1, CharPl_2
    
    print(charactersDataG)

    # AsignarPersonajes al jugador
    CharJugador = personajesElegidosG

    CharPl_0 = charactersDataG[CharJugador[0]]
    CharPl_0["vivo"] = True

    CharPl_1 = charactersDataG[CharJugador[1]]
    CharPl_1["vivo"] = True

    CharPl_2 = charactersDataG[CharJugador[2]]
    CharPl_2["vivo"] = True


    # Asignar Personajes a la maquina
    CharMaquina = [14 + NivelG, 12, 13]

    # print(CharJugador)

    # def opciones():
    #     if len(CharMaquina) == 3:
    #         return
        
    #     num = random.randint(0, 14)
    #     if num not in CharJugador and num not in CharMaquina:
    #         CharMaquina.append(num)

    #     else: 
    #         return opciones()
        
    # print(CharMaquina)


    CharEn_0 = charactersDataG[CharMaquina[0]]
    CharEn_0["vivo"] = True

    CharEn_1 = charactersDataG[CharMaquina[1]]
    CharEn_1["vivo"] = True

    CharEn_2 = charactersDataG[CharMaquina[2]]
    CharEn_2["vivo"] = True






    
            

    
            
        
    

