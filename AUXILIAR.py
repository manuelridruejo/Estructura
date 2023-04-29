######################################################## CLASES ##############################################################################

from random import shuffle, randint


PALOS = ["Oro", "Espada", "Copa", "Basto"] # Variable global en mayúsculas Guía PEP-8
NUMEROS = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
JERARQUIAS = {
    ("Oro", 1): 7,
    ("Oro", 2): 8,
    ("Oro", 3): 9,
    ("Oro", 4): 0,
    ("Oro", 5): 1,
    ("Oro", 6): 2,
    ("Oro", 7): 10,
    ("Oro", 10): 4,
    ("Oro", 11): 5,
    ("Oro", 12): 6,
    ("Espada", 1): 13,
    ("Espada", 2): 8,
    ("Espada", 3): 9,
    ("Espada", 4): 0,
    ("Espada", 5): 1,
    ("Espada", 6): 2,
    ("Espada", 7): 11,
    ("Espada", 10): 4,
    ("Espada", 11): 5,
    ("Espada", 12): 6,
    ("Basto", 1): 12,
    ("Basto", 2): 8,
    ("Basto", 3): 9,
    ("Basto", 4): 0,
    ("Basto", 5): 1,
    ("Basto", 6): 2,
    ("Basto", 7): 3,
    ("Basto", 10): 4,
    ("Basto", 11): 5,
    ("Basto", 12): 6,
    ("Copa", 1): 7,
    ("Copa", 2): 8,
    ("Copa", 3): 9,
    ("Copa", 4): 0,
    ("Copa", 5): 1,
    ("Copa", 6): 2,
    ("Copa", 7): 3,
    ("Copa", 10): 4,
    ("Copa", 11): 5,
    ("Copa", 12): 6
}

JERARQUIAS_ENVIDO = {
    ("Oro", 1): 1,
    ("Oro", 2): 2,
    ("Oro", 3): 3,
    ("Oro", 4): 4,
    ("Oro", 5): 5,
    ("Oro", 6): 6,
    ("Oro", 7): 7,
    ("Oro", 10): 0,
    ("Oro", 11): 0,
    ("Oro", 12): 0,
    ("Espada", 1): 1,
    ("Espada", 2): 2,
    ("Espada", 3): 3,
    ("Espada", 4): 4,
    ("Espada", 5): 5,
    ("Espada", 6): 6,
    ("Espada", 7): 7,
    ("Espada", 10): 0,
    ("Espada", 11): 0,
    ("Espada", 12): 0,
    ("Basto", 1): 1,
    ("Basto", 2): 2,
    ("Basto", 3): 3,
    ("Basto", 4): 4,
    ("Basto", 5): 5,
    ("Basto", 6): 6,
    ("Basto", 7): 7,
    ("Basto", 10): 0,
    ("Basto", 11): 0,
    ("Basto", 12): 0,
    ("Copa", 1): 1,
    ("Copa", 2): 2,
    ("Copa", 3): 3,
    ("Copa", 4): 4,
    ("Copa", 5): 5,
    ("Copa", 6): 6,
    ("Copa", 7): 7,
    ("Copa", 10): 0,
    ("Copa", 11): 0,
    ("Copa", 12): 0
}


class Carta():
    def __init__(self, palo : str, numero : int) -> None:
        self.palo = palo
        self.numero = numero
        self.jerarquia = JERARQUIAS[(palo, numero)]
        self.jerarquia_envido = JERARQUIAS_ENVIDO [(palo, numero)]

    def __str__(self):
        return "{} de {}".format(self.numero, self.palo)
    
    def __eq__(self, other):
        return self.jerarquia == other.jerarquia 
    
    def __gt__(self, other):
        return self.jerarquia > other.jerarquia

    def __lt__(self, other):
        return self.jerarquia < other.jerarquia 
    
    def __ge__(self, other):
        return self.jerarquia >= other.jerarquia 
    
    def __le__(self, other):
        return self.jerarquia <= other.jerarquia 
    
    def __ne__(self, other):
        return self.jerarquia != other.jerarquia 
    def __repr__ (self):
      return str(self)
    

class Mazo():
    def __init__(self) -> None:
        self.cartas = []
        for palo in PALOS:
            for numero in NUMEROS:
                self.cartas.append(Carta(palo,numero))
        self.mezclar()
    
    def __str__(self):
        impresion_mazo = ""
        for carta in self.cartas:
            impresion_mazo += (str(carta) + "\n")
        impresion_mazo = impresion_mazo[:-1]
        return impresion_mazo
    
    def mezclar(self):
        shuffle(self.cartas)
    
    def repartir(self):
        cartas=[]
        for i in range(6):
            cartas.append(self.cartas[i])
        return cartas

######################################################## FUNCIONES ##########################################################################

def mostrar_cartas(lista):
    cartas = ""
    for i in lista:
        cartas += (str(i))
    return "sus cartas son {}".format(cartas)

def tirar_3 (jugador,cartas):
    lista = []
    print(jugador + mostrar_cartas(cartas))
    print("Que carta desea tirar:")
    print("0."+cartas[0])
    print("1."+cartas[1])
    print("2."+cartas[2])
    op = int(input("Elija:"))
    while op not in [0,1,2]:
        print(jugador + mostrar_cartas(cartas))
        print("Que carta desea tirar:")
        print("0."+cartas[0])
        print("1."+cartas[1])
        print("2."+cartas[2])
        op = int(input("Elija entre 0,1,2:"))
    for j in cartas:
        if j != cartas[op]:
            lista.append(j)
    return cartas[op],lista

def tirar_2(jugador,cartas):
    lista = []
    print(jugador + mostrar_cartas(cartas))
    print("Que carta desea tirar:")
    print("0."+cartas[0])
    print("1."+cartas[1])
    op = int(input("Elija:"))
    while op not in [0,1]:
        print("Que carta desea tirar:")
        print("0."+cartas[0])
        print("1."+cartas[1])
        op = int(input("Elija entre 0,1:"))
    for j in cartas:
        if j != cartas[op]:
            lista.append(j)
    return cartas[op],lista

def tirar_1(jugador,cartas):
    lista = []
    print(jugador + mostrar_cartas(cartas))
    print("Le queda una sola carta, presione 0 para tirarla:")
    print("0."+cartas[0])
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

######################################################## ENVIDO ##########################################################################

def real_envido (jug1, puntos1, jug2, puntos2, puntos_tanto, puntos_al_no):
  print(jug1,'ha cantado REAL ENVIDO')
  print('\n',jug2,', que desea hacer?')
  print('1. Falta envido')
  print('2. Quiero')
  print('3. No quiero')
  opcion = int(input('\tElija:'))
  if opcion == 1:                   
    puntos_al_no=puntos_tanto
    puntos1, puntos2 = falta_envido (jug2, puntos2, jug1, puntos1, puntos_al_no)
    
  elif opcion == 2:                    
    print('\n',jug2,' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto)
    
  elif opcion == 3:                
    print('\n',jug2,' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
    puntos1 += puntos_al_no
  
  return puntos1, puntos2

def falta_envido (jug1, puntos1, jug2, puntos2, puntos_al_no):
  puntos_tanto = contar_puntos_falta (puntos1,puntos2)
  print(jug1,'ha cantado FALTA ENVIDO!')
  print('\n',jug2,', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = int(input('\tElija:'))

  if opcion == 1:                         
    print('\n',jug2,' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto)
          
  if opcion == 2:                         
    print('\n',jug2,' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
    puntos1 += puntos_al_no
  
  return puntos1, puntos2

def contar_tanto(cartas):
    tanto_01 = 0
    tanto_02 = 0
    tanto_12 = 0
    n=0
    if cartas[1].palo == cartas[2].palo:
        tanto_12 = 20 + (int(cartas[1].jerarquia_envido) + int(cartas[2].jerarquia_envido))
        n += 1

    if cartas[0].palo == cartas[1].palo:
        tanto_01 = 20 + (int(cartas[1].jerarquia_envido) + int(cartas[0].jerarquia_envido))
        n += 1
        
    if cartas[0].palo == cartas[2].palo:
        tanto_02 = 20 + (int(cartas[0].jerarquia_envido) + int(cartas[2].jerarquia_envido))
        
    if n >= 1:
        tanto=max(tanto_01,tanto_02,tanto_12)

    if n == 0:
        tanto=(max(cartas[0].jerarquia_envido, cartas[1].jerarquia_envido, cartas[2].jerarquia_envido))
    
    return tanto

def contar_los_tantos (cartasjug1,cartasjug2):
    tanto1 = contar_tanto(cartasjug1)
    tanto2 = contar_tanto(cartasjug2)
    return tanto1, tanto2

def contar_puntos_falta (puntos1,puntos2):
  if puntos2 < puntos1:
    puntos_tanto = 30 - puntos1
  elif puntos2 > puntos1:
    puntos_tanto = 30 - puntos2
  else:
    puntos_tanto = 30 - puntos1
  return puntos_tanto

def sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto):
  tanto1, tanto2 = contar_los_tantos (jug1, jug2)
  if jug1 == mano:
    print('\n',jug1+':',tanto1)

    if tanto2>tanto1:
      print(jug2+':',tanto2,'son mejores puto de mierda')
      puntos2 += puntos_tanto
      print(jug2,'suma',puntos_tanto,'puntos')

    else:
      print(jug2+': son buenas')
      puntos1 += puntos_tanto
      print(jug1,'suma',puntos_tanto,'puntos')

  elif jug2 == mano:
    print('\n',jug2+':',tanto2)

    if tanto1>tanto2:
      print(jug1+':',tanto1,'son mejores.')
      puntos1 += puntos_tanto
      print(jug1,'suma',puntos_tanto,'puntos')

    else:
      print(jug1+': son buenas')
      puntos2 += puntos_tanto
      print(jug2,'suma',puntos_tanto,'puntos')

  return puntos1, puntos2
  


def envido (jug1, puntos1, jug2, puntos2):
  print('Que desea cantar?')
  print('1. Envido')
  print('2. Real envido')
  print('3. Falta envido')
  opcion = int(input('\tElija:'))

  if opcion == 1:             #ENVIDO (j1)
    puntos_tanto = 2
    puntos_al_no = 1
    print(jug1,'ha cantado ENVIDO')
    print('\n',jug2,', que desea hacer?')
    print('1. Envido')
    print('2. Real envido')
    print('3. Falta envido')
    print('4. Quiero')
    print('5. No quiero')
    opcion = int(input('\tElija:'))

    if opcion == 1:              #ENVIDO (j1) ENVIDO (j2)
      puntos_al_no = puntos_tanto
      puntos_tanto = 4
      print(jug2,'ha cantado ENVIDO')
      print('\n',jug1,', que desea hacer?')
      print('1. Real envido')
      print('2. Falta envido')
      print('3. Quiero')
      print('4. No quiero')
      opcion = int(input('\tElija:'))

      if opcion == 1:              #ENVIDO (j1) ENVIDO (j2) REAL ENVIDO (j1)
        puntos_al_no = puntos_tanto
        puntos_tanto = 7
        puntos1, puntos2 = real_envido (jug1, puntos1, jug2, puntos2, puntos_tanto, puntos_al_no)
        
      elif opcion == 2:                   #ENVIDO (j1) ENVIDO (j2) FALTA ENVIDO (j1)
        puntos_al_no=4
        puntos1, puntos2 = falta_envido (jug1, puntos1, jug2, puntos2, puntos_al_no)
      
      elif opcion == 3:                   # ENVIDO (j1) ENVIDO (j2) QUIERO (j1)
        print('\n',jug1,' ha dicho QUIERO')
        puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto)
      
      elif opcion == 4:                   # ENVIDO (j1) ENVIDO (j2) NO QUIERO (j1)
        print('\n',jug1,' ha dicho NO QUIERO.',jug2,'suma',puntos_al_no,'puntos')
        puntos2 += puntos_al_no
    
    elif opcion == 2:                     #ENVIDO (j1) REAL ENVIDO (j2)
      puntos_al_no = puntos_tanto
      puntos_tanto=5
      puntos1, puntos2 = real_envido (jug2, puntos2, jug1, puntos1, puntos_tanto, puntos_al_no)
      
    elif opcion == 3:                     #ENVIDO (j1) FALTA ENVIDO (j2)
      puntos_al_no=2
      puntos1, puntos2 = falta_envido (jug2, puntos2, jug1, puntos1, puntos_al_no)
    
    elif opcion == 4:                     #ENVIDO (j1) QUIERO (j2)
      print('\n',jug2,' ha dicho QUIERO')
      puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, jug2, puntos2, puntos_tanto)
    
    elif opcion == 5:                     #ENVIDO (j1) NO QUIERO (j2)
      print('\n',jug2,' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
      puntos1 += puntos_al_no
    
  elif opcion == 2:                     #REAL ENVIDO (j1) 
    puntos_al_no = 1
    puntos_tanto = 32
    puntos1, puntos2 = real_envido (jug1, puntos1, jug2, puntos2, puntos_tanto, puntos_al_no)
  
  elif opcion == 3:
    puntos_al_no=1
    puntos1, puntos2 = falta_envido (jug1, puntos1, jug2, puntos2, puntos_al_no)
  
  return puntos1, puntos2

########################################################## TRUCO ############################################################################

def CantarTruco (p1,p2): 
  retruco = False
  vale_cuatro = False
  quiero = True

  print(p1,'ha cantado TRUCO!')
  print(p2+', que desea hacer?')
  print('1. Retruco')
  print('2. Quiero')
  print('3. No quiero')
  opcion = int(input('\tElija:'))

  if opcion == 1:
    retruco = True 
    print(p2,'ha cantado RE TRUCO!')
    print(p1+', que desea hacer?')
    print('1. Vale cuatro')
    print('2. Quiero')
    print('3. No quiero')
    opcion = int(input('\tElija:'))

    if opcion == 1:
      vale_cuatro = True
      print(p1,'ha cantado QUIERO VALE CUATRO!')
      print(p2+', que desea hacer?')
      print('1. Quiero')
      print('2. No quiero')
      opcion = int(input('\tElija:'))

      if opcion == 1:
        print(p2+', ha dicho QUIERO')
        puntos_truco = 4
      
      elif opcion == 2:
        print(p2+', ha dicho NO QUIERO')
        puntos_truco = 3
        quiero = False
    
    elif opcion == 2:
      print(p1+', ha dicho QUIERO')
      puntos_truco = 3

    elif opcion == 3:
      print(p1+', ha dicho NO QUIERO')
      puntos_truco = 2
      quiero = False
  
  elif opcion == 2:
    print(p2+', ha dicho QUIERO')
    puntos_truco = 2
          
  elif opcion == 3:
    print(p2+', ha dicho NO QUIERO')
    puntos_truco = 1
    quiero = False
  
  return puntos_truco, quiero, retruco, vale_cuatro 

def CantarReTruco (p1, p2):
  print(p2,'ha cantado RE TRUCO!')
  print(p1+', que desea hacer?')
  print('1. Vale cuatro')
  print('2. Quiero')
  print('3. No quiero')
  opcion = int(input('\tElija:'))

  if opcion == 1:
    vale_cuatro = True
    print(p1,'ha cantado QUIERO VALE CUATRO!')
    print(p2+', que desea hacer?')
    print('1. Quiero')
    print('2. No quiero')
    opcion = int(input('\tElija:'))

    if opcion == 1:
      print(p2+', ha dicho QUIERO')
      puntos_truco = 4
    
    elif opcion == 2:
      print(p2+', ha dicho NO QUIERO')
      puntos_truco = 3
      quiero = False
  
  elif opcion == 2: 
    print(p1+', ha dicho QUIERO')
    puntos_truco = 3

  elif opcion == 3:
    print(p1+', ha dicho NO QUIERO')
    puntos_truco = 2
    quiero = False

  return puntos_truco, quiero, vale_cuatro

def CantarValeCuatro(p1, p2):
  print(p1,'ha cantado QUIERO VALE CUATRO!')
  print(p2+', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = int(input('\tElija:'))

  if opcion == 1:
    print(p2+', ha dicho QUIERO')
    puntos_truco = 4
  
  elif opcion == 2:
    print(p2+', ha dicho NO QUIERO')
    puntos_truco = 3
    quiero = False

  return puntos_truco, quiero

################################################################ MAIN ######################################################################## 

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
    que_mano_es+=1
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

