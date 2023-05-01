import Clases
import envido
import TRUCO

def mostrar_cartas(lista):
    cartas = ""
    for i in lista:
        cartas += (str(i))
    return "sus cartas son {}".format(cartas)

def tirar_3 (jugador,cartas):
    lista = []
    print(jugador + mostrar_cartas(cartas))
    print("Que carta desea tirar:")
    print("0."+str(cartas[0]))
    print("1."+str(cartas[1]))
    print("2."+str(cartas[2]))
    op = int(input("Elija:"))
    while op not in [0,1,2]:
        print(jugador + mostrar_cartas(cartas))
        print("Que carta desea tirar:")
        print("0."+str(cartas[0]))
        print("1."+str(cartas[1]))
        print("2."+str(cartas[2]))
        op = int(input("Elija entre 0,1,2:"))
    for j in cartas:
        if j != cartas[op]:
            lista.append(j)
    return cartas[op],lista

def tirar_2(jugador,cartas):
    lista = []
    print(jugador + mostrar_cartas(cartas))
    print("Que carta desea tirar:")
    print("0."+str(cartas[0]))
    print("1."+str(cartas[1]))
    op = int(input("Elija:"))
    while op not in [0,1]:
        print("Que carta desea tirar:")
        print("0."+str(cartas[0]))
        print("1."+str(cartas[1]))
        op = int(input("Elija entre 0,1:"))
    for j in cartas:
        if j != cartas[op]:
            lista.append(j)
    return cartas[op],lista

def tirar_1(jugador,cartas):
    lista = []
    print(jugador + mostrar_cartas(cartas))
    print("Le queda una sola carta, presione 0 para tirarla:")
    print("0."+str(cartas[0]))
    op = int(input("Elija:"))
    while op != 0:
        op = int(input("Elija 0:"))
    return cartas[op]

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

def JugarPrimera (p1, puntos1, p2, puntos2, cartasj1):
  mostrar_cartas(cartasj1)
  termino = False
  hubo_envido = False
  truco = False
  retruco = False
  vale_cuatro = False
  print(p1+', que desea hacer?')
  print('1. Cantar envido')
  print('2. Cantar truco')
  print('3. Tirar carta')
  print('4. Irse al mazo') 
  opcion = int(input('\tElija:'))

  if opcion == 1:
    puntos1, puntos2 = envido (p1, puntos1, p2, puntos2)
    hubo_envido = True
    
    print(p1+', que desea hacer?')
    print('1. Cantar truco')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('\tElija:'))

    if opcion == 1:
      truco = True
      puntos_truco, quiero, retruco, vale_cuatro = CantarTruco (p1, p2)
    
      if quiero == False:
        termino = True
      
      else:
        carta1_p1, cartasj1 = tirar_3(p1,str(cartasj1))
        print("{} ha tirado el {}".format(p1,str(carta1_p1)))
    
    elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3(p1,str(cartasj1))
        print("{} ha tirado el {}".format(p1,str(carta1_p1)))
    
    elif opcion == 3:
      termino = True

  elif opcion == 2:
    truco = True 
    puntos_truco, quiero, retruco, vale_cuatro = CantarTruco (p1, p2)
    
    if quiero == False:
      termino = True
      return puntos1, puntos2, puntos_truco, termino, hubo_envido, "", cartasj1, truco, retruco, vale_cuatro
    
    else:
        carta1_p1, cartasj1 = tirar_3(p1,cartasj1)
        print("{} ha tirado el {}".format(p1,str(carta1_p1)))
  elif opcion == 3:
    carta1_p1, cartasj1 = tirar_3(p1,cartasj1)
    print("{} ha tirado el {}".format(p1,str(carta1_p1)))
  elif opcion == 4:
    termino = True
    return puntos1, puntos2, puntos_truco, termino, hubo_envido, "", cartasj1, truco, retruco, vale_cuatro
  return puntos1, puntos2, puntos_truco, termino, hubo_envido, carta1_p1, cartasj1, truco, retruco, vale_cuatro

def JugarPrimeraSinTanto (p1, puntos1, p2, puntos2, cartasj1):
  truco = False
  retruco = False
  vale_cuatro = False
  print(p1+', que desea hacer?')
  print('1. Cantar truco')
  print('2. Tirar carta')
  print('3. Irse al mazo')
  opcion = int(input('\tElija:'))

  if opcion == 1:
    truco = True
    puntos_truco, quiero, retruco, vale_cuatro = CantarTruco (p1, p2)
  
    if quiero == False:
      termino = True
    
    else:
        carta1_p1,cartasj1 = tirar_3(p1,cartasj1)
        print("{} ha tirado el {}".format(p1,carta1_p1))
  elif opcion == 2:
    carta1_p1,cartasj1 = tirar_3(p1,cartasj1)
    print("{} ha tirado el {}".format(p1,carta1_p1))
  elif opcion == 3:
    termino = True
  
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, truco, retruco, vale_cuatro 

def Jugar_Segunda(p1, puntos1, p2, puntos2, cartasj1, truco, retruco, vale_cuatro):
  if truco == False:
    print(p1+', que desea hacer?')
    print('1. Cantar truco')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('\tElija:'))
    
    if opcion == 1:
      truco = True
      puntos_truco, quiero, retruco, vale_cuatro = CantarTruco (p1, p2)
    
      if quiero == False:
        termino = True
      
      else:
          carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
          print("{} ha tirado el {}".format(p1,carta1_p1))
    elif opcion == 2:
      carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
      print("{} ha tirado el {}".format(p1,carta1_p1))
    elif opcion == 3:
      termino = True
  elif truco == True and retruco == False and vale_cuatro == False:
      print(p1+', que desea hacer?')
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))
      if opcion == 1:
        retruco = True
        puntos_truco, quiero, vale_cuatro = CantarReTruco (p1, p2)
      
        if quiero == False:
          termino = True
        
        else:
            carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
            print("{} ha tirado el {}".format(p1,carta1_p1))
      elif opcion == 2:
        carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
        print("{} ha tirado el {}".format(p1,carta1_p1))
      elif opcion == 3:
        termino = True
  elif truco == True and retruco == True and vale_cuatro == False:
      print(p1+', que desea hacer?')
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))
      if opcion == 1:
        vale_cuatro = True
        puntos_truco, quiero = CantarValeCuatro (p1, p2)
      
        if quiero == False:
          termino = True
        
        else:
            carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
            print("{} ha tirado el {}".format(p1,carta1_p1))
      elif opcion == 2:
        carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
        print("{} ha tirado el {}".format(p1,carta1_p1))
      elif opcion == 3:
        termino = True
  elif vale_cuatro == True:
     carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
     print("{} ha tirado el {}".format(p1,carta1_p1))
     
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, truco, retruco, vale_cuatro 
