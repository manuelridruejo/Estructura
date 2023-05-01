import TRUCO as T
import envido as E
import Clases as C

def mostrar_cartas(lista):
  cartas = "sus cartas son: "
  for i in lista:
    cartas += (str(i)+', ')
  print(cartas)


def tirar_3 (jugador, cartas):
  lista = []
  print("\n"+jugador+", que carta desea tirar:")
  print("0. "+str(cartas[0]))
  print("1. "+str(cartas[1]))
  print("2. "+str(cartas[2]))
  op = int(input("Elija:"))

  while op not in [0,1,2]:
    print("\n"+jugador+", que carta desea tirar:")
    print("0. "+str(cartas[0]))
    print("1. "+str(cartas[1]))
    print("2. "+str(cartas[2]))
    op = int(input("Elija entre 0,1,2:"))

  for j in cartas:
    if j != cartas[op]:
      lista.append(j)

  return cartas[op], lista


def tirar_2(jugador,cartas):
  
  lista = []
  
  print("\n"+jugador+", que carta desea tirar:")
  print("0. "+str(cartas[0]))
  print("1. "+str(cartas[1]))
  op = int(input("Elija:"))
  
  while op not in [0,1]:
    print("\n"+jugador+", que carta desea tirar:")
    print("0."+str(cartas[0]))
    print("1."+str(cartas[1]))
    op = int(input("Elija entre 0,1:"))
  
  for j in cartas:
    if j != cartas[op]:
      lista.append(j)
  
  return cartas[op],lista

def tirar_1(jugador, cartas):
  
  print('\n'+jugador+", le queda una sola carta, presione 0 para tirarla:")
  print("0."+str(cartas[0]))
  op = int(input("Elija:"))
  
  while op != 0:
    op = int(input("Elija 0:"))

  return cartas[0], []


def quien_es_mano (ronda, p1, puntos1, p2, puntos2):
  
  if ronda%2 == 0:
    mano = p1
    pie = p2
    puntos_mano = puntos1
    puntos_pie = puntos2

  if ronda%2 != 0:
    mano = p2
    pie = p1
    puntos_mano = puntos2
    puntos_pie = puntos1

  return mano, puntos_mano, pie, puntos_pie


def JugarPrimera (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_truco, quiero, mano):                 #JUGAR PRIMERA
  
  termino = False
  hubo_envido = False
  carta1_p1=''
  ganador = ''

  if quiero == jug1 or quiero == '':

    if puntos_truco == 1:
      print('\n'+jug1+', que desea hacer?')
      mostrar_cartas(cartasj1)
      print('1. Cantar envido')
      print('2. Cantar truco')
      print('3. Tirar carta')
      print('4. Irse al mazo') 
      opcion = int(input('Elija:'))

      if opcion == 1:
        puntos1, puntos2 = E.envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n'+jug1+', que desea hacer?')
        mostrar_cartas(cartasj1)
        print('1. Cantar truco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('Elija:'))

        if opcion == 1:
          puntos_truco, termino, ganador, quiero = T.CantarTruco (jug1, jug2)
          
          if termino != True:
            carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
            print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
        
        elif opcion == 2:
          carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
          print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
      
        elif opcion == 3:
          termino = True
          ganador = jug2

      elif opcion == 2:
        puntos_truco, termino, ganador, quiero = T.CantarTruco (jug1, jug2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 4:
        termino = True
        ganador = jug2

    elif puntos_truco == 2:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar envido')
      print('2. Cantar retruco')
      print('3. Tirar carta')
      print('4. Irse al mazo') 
      opcion = int(input('Elija:'))

      if opcion == 1:
        puntos1, puntos2 = E.envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar retruco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('Elija:'))

        if opcion == 1:
          puntos_truco, termino, ganador, quiero = T.CantarReTruco (jug1, jug2)
      
          if termino != True:
            carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
            print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
      
        elif opcion == 2:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
      
        elif opcion == 3:
          termino = True
          ganador = jug2

      elif opcion == 2:
        puntos_truco, termino, ganador, quiero = T.CantarReTruco (jug1, jug2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 4:
        termino = True
        ganador = jug2
      
    elif puntos_truco == 3:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar envido')
      print('2. Cantar vale cuatro')
      print('3. Tirar carta')
      print('4. Irse al mazo') 
      opcion = int(input('Elija:'))

      if opcion == 1:
        puntos1, puntos2 = E.envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar vale cuatro')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('Elija:'))

        if opcion == 1:
          puntos_truco, termino, ganador, quiero = T.CantarValeCuatro (jug1, jug2)
      
          if termino != True:
            carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
            print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
      
        elif opcion == 2:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
        
        elif opcion == 3:
          termino = True
          ganador = jug2

      elif opcion == 2:
        puntos_truco, termino, ganador, quiero = T.CantarValeCuatro (jug1, jug2)
    
        if termino != True:
          carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 4:
        termino = True
        ganador = jug2
      
    elif puntos_truco == 4:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar envido')
      print('2. Tirar carta')
      print('3. Irse al mazo') 
      opcion = int(input('Elija:'))

      if opcion == 1:
        puntos1, puntos2 = E.envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Tirar carta')
        print('2. Irse al mazo')
        opcion = int(input('Elija:'))

        if opcion == 1:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
        
        elif opcion == 2:
          termino = True
          ganador = jug2

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2
  
  elif quiero == jug2:
    print('\n' + jug1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Cantar envido')
    print('2. Tirar carta')
    print('3. Irse al mazo') 
    opcion = int(input('Elija:'))

    if opcion == 1:
      puntos1, puntos2 = E.envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
      hubo_envido = True
        
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = int(input('Elija:'))

      if opcion == 1:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        termino = True
        ganador = jug2
    
    elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = jug2

  return puntos1, puntos2, puntos_truco, termino, hubo_envido, carta1_p1, cartasj1, ganador, quiero


def JugarPrimeraSinTanto (jug1, cartasj1, jug2, puntos_truco, quiero):                            #JUGAR PRIMERA SIN TANTO
  
  carta1_p1 = ''
  ganador = ''
  termino = False 

  if quiero == jug1 or quiero == '':

    if puntos_truco == 1:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))

      while opcion not in [1,2,3]:
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar truco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('Elija:'))

      if opcion == 1:
        puntos_truco, termino, ganador, quiero = T.CantarTruco (jug1, jug2)

        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2

    elif puntos_truco == 2:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))
      
      while opcion not in [1,2,3]:
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar retruco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('Elija:'))

      if opcion == 1:
        puntos_truco, termino, ganador, quiero = T.CantarReTruco (jug1, jug2)

        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2

    elif puntos_truco == 3:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))

      while opcion not in [1,2,3,]:
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar vale cuatro')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('Elija:'))
      
      if opcion == 1:
        puntos_truco, termino, ganador, quiero = T.CantarValeCuatro (jug1, jug2)
          
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2
    
    elif puntos_truco == 4:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = int(input('Elija:'))

      while opcion not in [1,2]:
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Tirar carta')
        print('2. Irse al mazo')
        opcion = int(input('Elija:'))

      if opcion == 1:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        termino = True
        ganador = jug2
  
  elif quiero == jug2:
    print('\n' + jug1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = int(input('Elija:'))

    while opcion not in [1,2]:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas(cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = int(input('Elija:'))

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
      print("\n{} ha tirado el {}".format (jug1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = jug2

  return puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero


def Jugar_Segunda(p1, puntos1, p2, puntos2, cartasj1, puntos_truco, quiero):                            #JUGAR SEGUNDA MANO
  
  termino= False
  carta1_p1 = ""
  ganador = ''

  if quiero == p1 or quiero == '':

    if puntos_truco == 1:
      print('\n'+p1+', que desea hacer?')
      mostrar_cartas(cartasj1)
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))

      while opcion not in [1,2,3]:
        print('\n' + p1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar truco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('Elija:'))
          
      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = T.CantarTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))
 
      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2 

    elif puntos_truco == 2:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))

      while opcion not in [1,2,3]:
        print('\n' + p1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar retruco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('\tElija:'))

      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = T.CantarReTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
          print("\n{} ha tirado el {}".format(p1,carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
        print("\n{} ha tirado el {}".format(p1, carta1_p1))
 
      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 3:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))

      while opcion not in [1,2,3]:
        print('\n' + p1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar vale cuatro')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('\tElija:'))

      if opcion == 1:     
        puntos_truco, termino, ganador, quiero = T.CantarValeCuatro (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 4:
      carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
      print("\n{} ha tirado el {}".format (p1, carta1_p1))
  
  elif quiero == p2:
    print('\n' + p1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = int(input('Elija:'))

    while opcion not in [1,2]:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = int(input('Elija:'))

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
      print("\n{} ha tirado el {}".format (p1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = p2
     
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero 


def Jugar_Tercera (p1, puntos1, p2, puntos2, cartasj1, puntos_truco, quiero):                #JUGAR TERCER MANO
  
  termino = False
  carta1_p1 = ""
  ganador = ''

  if quiero == p1 or quiero == '':

    if puntos_truco == 1:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))

      while opcion not in [1,2,3]:
        print('\n' + p1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar truco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('Elija:'))
      
      if opcion == 1:
        puntos_truco, termino, ganador, quiero = T.CantarTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 2:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))

      while opcion not in [1,2,3]:
        print('\n' + p1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar retruco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('\tElija:'))

      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = T.CantarReTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 3:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))

      while opcion not in [0,1,2,3]:
        print('\n' + p1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Cantar vale cuatro')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = int(input('\tElija:'))

        if opcion == 1:
          
          puntos_truco, temrino, ganador, quiero = T.CantarValeCuatro (p1, p2)
        
          if termino != True:
            carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
            print("\n{} ha tirado el {}".format (p1, carta1_p1))

        elif opcion == 2:
          carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

        elif opcion == 3:
          termino = True
          ganador = p2

    elif puntos_truco == 4:
      carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
      print("\n{} ha tirado el {}".format (p1, carta1_p1))
   
  elif quiero == p2:
    print('\n' + p1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = int(input('Elija:'))

    while opcion not in [1,2]:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = int(input('Elija:'))

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_1(p1, cartasj1)
      print("\n{} ha tirado el {}".format(p1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = p2
     
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero 