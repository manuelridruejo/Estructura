from Clases import *
from envido import *
from funciones import * 

  
def Main ():
    puntos1=0
    puntos2=0
    p1='Jugador 1'
    p2='Jugador 2'
    ronda=1

    while puntos1 < 30 and puntos2 < 30:
        mazo=Mazo()
        cartas_en_juego = mazo.repartir()
        cartasmano = [cartas_en_juego[0],cartas_en_juego[2],cartas_en_juego[4]]
        cartaspie = [cartas_en_juego[1],cartas_en_juego[3],cartas_en_juego[5]]
        opcion=0
        termino=False
        mano, pie = quien_es_mano (ronda, p1, p2)
        valor_mano=1

        while opcion!=4 and termino==False:
            #JUEGA LA MANO PRIMER0
            opcion = jugar_primera()
            if opcion == 1:
                puntos1, puntos2 = envido (p1,puntos1,p2,puntos2)
            if opcion == 2:
                h=0

Main()