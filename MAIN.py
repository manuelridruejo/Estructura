from Clases import *
from funciones import *


registro_partidas = open("Registro partidas.txt", "r+") 
registro_jugadores = open("Registro Jugadores.txt", "r+")
registro_codigos = open("Registro codigos de partida.txt", "r+")
jugadores_archivo = registro_jugadores.read() 
codigos_archivo = registro_codigos.read()
#;1;jug1;jug2;20-04-2020;resultado;/;2;jug3;jug4;20-05-2020;resultado2;/2

#[[1,jug,jug2,20-04-2020,resultado],[2,jug3,jug4,20-05-2020,resultado2]]

cod = ""
lista_cod = []
for caracter in codigos_archivo:
  if caracter != "/":
    cod += caracter
  else:
    lista_cod.append(cod)
    cod = ""

cod2 = ""
lista_partidas_final = []

for codigo in lista_cod:
  aux = []
  for caracter in codigo:
    if caracter != ";":
      cod2 += caracter
    else:
      aux.append(cod2)
      cod2 = ""
  lista_partidas_final += [aux]

lista_codigos_existentes = []

for partida in lista_partidas_final:
  lista_codigos_existentes.append(int(partida[0]))


cadena_dni = ""
for i in jugadores_archivo:
  if i != "-":
    cadena_dni += i 

lista_dni =[]
for j in range(0, len(cadena_dni), 8):
  lista_dni.append(cadena_dni[j:j+8])


def Jugar():
  
  nombre1 = input("Ingrese el nombre de un jugador: ")
  apellido1= input("Y su apellido: ")

  dni1 = 0
  dni_mal = True
  while dni_mal == True:
    try:
      dni1 = int(input("Ingrese el DNI: ")) 
      while dni1 < 10000000 or dni1 > 99999999:
        dni1 = int(input("DNI invalido. Por favor, ingrese el DNI (8 numeros): ")) 
      dni_mal = False
    except:
      dni_mal = True

  nombre2 = input("\nIngrese el nombre del otro jugador: ")
  apellido2 = input("Y el apellido: ")

  dni2 = 0
  dni_mal = True
  while dni_mal == True:
    try:
      dni2 = int(input("Ingrese el DNI: ")) 
      while dni2 < 10000000 or dni2 > 99999999:
        dni2 = int(input("DNI invalido. Por favor, ingrese el DNI (8 numeros): ")) 
      dni_mal = False
    except:
      dni_mal = True

  jugador1 = Jugador (nombre1, apellido1, dni1)
  jugador2 = Jugador (nombre2, apellido2, dni2) 


  p1 = jugador1.nombre
  puntos1 = 0
  p2 = jugador2.nombre 
  puntos2 = 0
  ronda = 1

  if p1 == p2:
    p1 = jugador1.apellido
    p2 = jugador2.apellido

  escribir = "\nSe ha iniciado una nueva partida entre: " + p1 + " y " + p2

  print(escribir)
  registro_partidas.write(escribir)

  while puntos1 < 30 and puntos2 < 30:
    
    mazo=Mazo()       #Se crea el mazo

    cartas_en_juego = mazo.repartir()      #Se reparte el mazo

    mano, puntos_mano, pie, puntos_pie = quien_es_mano (ronda, p1, puntos1, p2, puntos2)        #Se determina que jugador es mano

    cartasmano = [cartas_en_juego[0],cartas_en_juego[2],cartas_en_juego[4]]         #Se dan las cartas al mano y al pie
    cartas_pie = [cartas_en_juego[1],cartas_en_juego[3],cartas_en_juego[5]]

    print('\nComienza la ronda '+str(ronda)+'!')

    print('\n'+mano, 'es MANO.')
    mostrar_cartas(cartasmano)
    print('\n')
    print(pie, 'es PIE.')
    mostrar_cartas(cartas_pie)
    puntos_truco = 1
    que_mano_es = 1
    hubo_envido = False
    termino = False
    quiero = ''

    while que_mano_es < 4:
      
      manos_pie = 0
      manos_mano = 0
      ganador1 = ''
      ganador2 = ''
      parda1 = False
      parda2 = False                 

      #Primera mano

      puntos_mano, puntos_pie, puntos_truco, termino, hubo_envido, carta1_mano, cartas_mano, ganador, quiero  = JugarPrimera (mano, puntos_mano, cartasmano, pie, puntos_pie, cartas_pie, puntos_truco, quiero, mano)
      
      if termino == True:
        if quiero == '':
          puntos_truco = 2
        break
      
      if hubo_envido == True:
        puntos_truco, termino, carta1_pie, cartas_pie, ganador, quiero  = JugarPrimeraSinTanto (pie, cartas_pie, mano, puntos_truco, quiero)
    
        if termino == True: 
          break

      elif hubo_envido == False:
        puntos_pie, puntos_mano, puntos_truco, termino, hubo_envido, carta1_pie, cartas_pie, ganador, quiero  = JugarPrimera (pie, puntos_pie, cartas_pie, mano, puntos_mano, cartasmano, puntos_truco, quiero, mano)

        if termino == True:
          break

      if carta1_pie > carta1_mano:
        ganador1 = pie
        print('\n'+pie, "ha ganado la mano")
        manos_pie += 1 

      elif carta1_mano > carta1_pie:
        ganador1 = mano 
        print('\n'+mano, "ha ganado la mano")
        manos_mano += 1

      elif carta1_mano == carta1_pie:
        parda1=True
        print('\nSe ha pardado')

      #Segunda Mano

      que_mano_es += 1

      if ganador1 == pie: #el pie gano primera arranca 2 el
        
        puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)

        if termino == True: 
          break

        puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

      elif ganador1 == mano: #la mano gano primera arranca la 2 el
        
        puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

        puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break

      elif  parda1 == True: #Se juega la parda
        
        puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        if carta2_mano == carta2_pie: #Se pardo segunda
          parda2 = True
          print("\nSe ha pardado")

        elif carta2_mano > carta2_pie: #gano la mano
          ganador = mano
          break
        
        elif carta2_pie > carta2_mano: #gano el pie
          ganador = pie
          break 
        
      if carta2_mano > carta2_pie: #mano gana segunda
        ganador2 = mano
        print('\n'+mano, "ha ganado la mano")
        manos_mano += 1

      elif carta2_pie > carta2_mano: #pie gana segunda
        ganador2 = pie
        manos_pie += 1
        print('\n'+pie, "ha ganado la mano")

      elif carta2_pie == carta2_mano and parda1 == False: #se parda 2 y no esta pardada primera
        if ganador1 == pie:
          ganador = pie
          break

        elif ganador1 == mano:
          ganador = mano

      if manos_pie == 2:
        ganador = pie
        break

      if manos_mano == 2:
        ganador = mano
        break 

      # Tercera Mano 
      
      que_mano_es += 1

      if ganador2 == pie:                 #pie gana 2 arranca en 3
      
        puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)

        if termino == True: 
          break

        puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

      elif ganador2 == mano: #mano gano 2 arranca en 3
        puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

        puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break
        
      elif  parda2 == True and parda1 == True: #Se juega la parda
        puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        if carta3_mano == carta3_pie: #Se pardo tercera gana la mano
          ganador = mano

        elif carta3_mano > carta3_pie: #gano la mano
          ganador = mano
        
        elif carta3_pie > carta3_mano: #gano el pie
          ganador = pie
        
      elif carta3_mano > carta3_pie: #gano la mano la 3 se le suman los puntos
        ganador = mano
        break

      elif carta3_pie > carta3_mano: #gano el pie la tercera se le suman los puntos
        ganador = pie
        break

      que_mano_es += 1

    if ganador == mano:
      puntos_mano += puntos_truco
      print("\nHa ganado: ", mano, " se le suman ", puntos_truco, " puntos")
      registro_partidas.write("\nHa ganado: " + mano + " se le suman " + str(puntos_truco) + " puntos") 
      
    elif ganador == pie:
      puntos_pie += puntos_truco
      print("\nHa ganado: ", pie, " se le suman ", puntos_truco, " puntos")
      registro_partidas.write("\nHa ganado: " + pie + " se le suman " + str(puntos_truco) + " puntos") 

    if p1 == mano:
      puntos1 = puntos_mano
      puntos2 = puntos_pie
    elif p2 == mano:
      puntos2 = puntos_mano
      puntos1 = puntos_pie
    
    print('\nPuntos de '+ p1 + ": " + str(puntos1))
    print('\nPuntos de ' + p2 + ": " + str(puntos2))
    print('\n------------------------------------------------------------------------------\n\n')
    registro_partidas.write('\nPuntos de ' + p1 + ": " + str(puntos1))
    registro_partidas.write('\nPuntos de ' + p2 + ": " + str(puntos2))
    registro_partidas.write('\n------------------------------------------------------------------------------\n\n')

    ronda +=1


  if puntos1 >= 30 and puntos2 >= 30:
          
    if puntos1 > puntos2:
      print('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
      registro_partidas.write('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
      ganador_final = "gano {}, {} a {}".format(p1, puntos1, puntos2) 
    elif puntos2 > puntos1:
      print('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
      registro_partidas.write('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
      ganador_final = "gano {}, {} a {}".format(p2, puntos2, puntos1) 
    elif puntos2 == puntos1:
      print('\nHA HABIDO UN EMPATE.')
      registro_partidas.write('\nHA HABIDO UN EMPATE.')
      ganador_final = "empate"
  elif puntos2 >= 30:
    print('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
    registro_partidas.write('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
    ganador_final = "gano {}, {} a {}".format(p2, puntos2, puntos1) 

  elif puntos1 >= 30:
    print('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
    registro_partidas.write('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
    ganador_final = "gano {}, {} a {}".format(p1, puntos1, puntos2)


  dni_a_agregar=[jugador1.DNI, jugador2.DNI]
  for f in dni_a_agregar:
    if f not in lista_dni:
      registro_jugadores.write("-" + str(f) + "-")


  partida_jugada = Partida(ganador_final, [jugador1.nombre,jugador2.nombre], lista_codigos_existentes)
  escritura = "{};{};{};{};{};/".format(str(partida_jugada.codigo_partida), partida_jugada.jugadores[0], partida_jugada.jugadores[1], partida_jugada.fecha, partida_jugada.resultado)
  registro_codigos.write(escritura)

opcion2 = 1
while opcion2 != 3:

  print("\nBienvenido! ¿Qué desea hacer?")
  print("\n1. Buscar una partida")
  print("\n2. Jugar un partido de Truco")
  print("\n3. Salir")
  opcion2 = input("\nElija: ")

  while opcion2 not in ['1', '2', '3']:
    opcion2 = input("Error. Elija entre 1,2 o 3: ")
  opcion2 = int(opcion2)
  
  
  if opcion2 == 1:
    codigo_correcto = False
    while codigo_correcto == False:
      try:
        codigo_a_buscar = int(input("Por favor ingrese el codigo de partida: "))
        while codigo_a_buscar not in lista_codigos_existentes:
          codigo_a_buscar = int(input("Error. Intente nuevamente. Por favor ingrese el codigo de partida: "))
        codigo_correcto = True
      
      except:
        codigo_correcto = False
    
    for partida in lista_partidas_final:
      #print(partida)
      if codigo_a_buscar == int(partida[0]):
        partida_encontrada = partida

    impresion = "La partida {} entre {} y {} salio {} y ocurrio el dia: {}".format(partida_encontrada[0],partida_encontrada[1], partida_encontrada[2], partida_encontrada[4], partida_encontrada[3])
    print(impresion)
  
  elif opcion2 == 2:
    Jugar()



registro_partidas.close() 
registro_jugadores.close()
registro_codigos.close()