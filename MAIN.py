from Clases import *
from envido import *
from funciones import * 
from TRUCO import *

  
p1 = 'Jugador 1 '
puntos1 = 0
p2 = 'Jugador 2'
puntos2 = 0
ronda = 1

while puntos1 < 30 and puntos2 < 30:
  mazo=Mazo()
  cartas_en_juego = mazo.repartir()
  mano, puntos_mano, pie, puntos_pie = quien_es_mano (ronda, p1, puntos1, p2, puntos2)
  cartasmano = [cartas_en_juego[0],cartas_en_juego[2],cartas_en_juego[4]]
  cartaspie = [cartas_en_juego[1],cartas_en_juego[3],cartas_en_juego[5]]
  print(mano, 'es MANO. Estas son sus cartas:')
  print(mostrar_cartas(cartasmano))
  print('\n\n')
  print(pie, 'es PIE. Estas son sus cartas:')
  print(mostrar_cartas(cartaspie)) 
  puntos_truco = 1
  que_mano_es = 1
  hubo_envido = False
  termino = False
  while que_mano_es < 4:
    
    manos_pie = 0
    manos_mano = 0
    parda1 = False
    parda2 = False
    parda3 = False
    puntos_mano, puntos_pie, puntos_truco, termino, hubo_envido, carta1_mano, cartasmano, truco, retruco, vale_cuatro = JugarPrimera (mano, puntos_mano, pie, puntos_pie,cartasmano)

    if hubo_envido == True:
      puntos_pie, puntos_mano, puntos_truco, termino, carta1_pie, cartas_pies, truco, retruco, vale_cuatro = JugarPrimeraSinTanto (pie, puntos_pie, mano, puntos_mano,cartaspie)
      if termino == True: #HAY QUE PRINTEAR CUANTOS PUNTOS SUMA Y QUIEN GANO LA MANO EN TODOS LOS BREAKS Y VER QUIEN GANO LOS PUNTOS
        break
    elif hubo_envido == False:
      puntos_pie, puntos_mano, puntos_truco, termino, hubo_envido, carta1_pie, cartas_pies, truco, retruco, vale_cuatro = JugarPrimera (pie, puntos_pie, mano, puntos_mano,cartaspie)
      if termino == True:
         break
    if carta1_pie > carta1_mano:
       ganador = pie
       manos_pie += 1 
    elif carta1_mano > carta1_pie:
       ganador = mano 
       manos_mano += 1
    elif carta1_mano == carta1_pie:
       parda1=True
    #Segunda Mano
    que_mano_es += 1
    if ganador == pie:
      puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pies, truco, retruco, vale_cuatro = Jugar_Segunda(pie, puntos_pie, mano, puntos_mano,cartaspie, truco, retruco, vale_cuatro)
      if termino == True: 
        break
      puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, truco, retruco, vale_cuatro = Jugar_Segunda(mano, puntos_mano,pie,puntos_pie,cartasmano,truco,retruco,vale_cuatro)
      if termino == True: 
        break
    elif ganador == mano: 
      puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, truco, retruco, vale_cuatro = Jugar_Segunda(mano, puntos_mano,pie,puntos_pie,cartasmano,truco,retruco,vale_cuatro)
      if termino == True: 
        break
      puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pies, truco, retruco, vale_cuatro = Jugar_Segunda(pie, puntos_pie, mano, puntos_mano,cartaspie, truco, retruco, vale_cuatro)
      if termino == True: 
        break
    elif  parda1 == True: #Se juega la parda
      puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, truco, retruco, vale_cuatro = Jugar_Segunda(mano, puntos_mano,pie,puntos_pie,cartasmano,truco,retruco,vale_cuatro)
      if termino == True: 
        break
      puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pies, truco, retruco, vale_cuatro = Jugar_Segunda(pie, puntos_pie, mano, puntos_mano,cartaspie, truco, retruco, vale_cuatro)
      if termino == True: 
        break
      if carta2_mano == carta2_pie: #Se pardo segunda
        parda2 = True
      elif carta2_mano > carta2_pie: #gano la mano
        puntos_mano += puntos_truco
        break
      elif carta2_pie > carta2_mano: #gano el pie
        puntos_pie += puntos_truco
        break 
    elif carta2_mano > carta2_pie:
      ganador = mano
      manos_mano += 1
    elif carta2_pie > carta2_mano:
      ganador = pie
      manos_pie += 1
    if manos_pie == 2:
      puntos_pie += puntos_truco
      break
    if manos_mano == 2:
      puntos_mano += puntos_truco
      break 
    # Tercera Mano 
    que_mano_es += 1
