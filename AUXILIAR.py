#####################################################CLASES###########################################

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

class Jugador():
	def __init__(self, nombre : str):
          self.nombre = nombre







################################################################ ENVIDO #######################################################################







def real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano):
  
  print('\n'+jug1,'ha cantado REAL ENVIDO')
  print('\n',jug2,', que desea hacer?')
  print('1. Falta envido')
  print('2. Quiero')
  print('3. No quiero')
  opcion = int(input('Elija:'))

  if opcion == 1:                   
    puntos_al_no=puntos_tanto
    puntos1, puntos2 = falta_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_al_no, mano)
    
  elif opcion == 2:                    
    print('\n',jug2,' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
    
  elif opcion == 3:                
    print('\n',jug2,' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
    puntos1 += puntos_al_no
  
  return puntos1, puntos2

def falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano):
  
  puntos_tanto = contar_puntos_falta (puntos1,puntos2)

  print('\n'+jug1,'ha cantado FALTA ENVIDO!')
  print('\n',jug2,', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = int(input('Elija:'))

  if opcion == 1:                         
    print('\n',jug2,' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
          
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

def contar_los_tantos (cartasjug1, cartasjug2):
  
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

def sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano):
  
  tanto1, tanto2 = contar_los_tantos (cartasj1, cartasj2) 

  if jug1 == mano:
    print('\n',jug1+':',tanto1)

    if tanto2>tanto1:
      print(jug2+':',tanto2,'son mejores!!')
      puntos2 += puntos_tanto
      print(jug2,'suma',puntos_tanto,'puntos')

    else:
      print(jug2+': son buenas.')
      puntos1 += puntos_tanto
      print(jug1,'suma',puntos_tanto,'puntos')

  elif jug2 == mano:
    print('\n',jug2+':',tanto2)

    if tanto1>tanto2:
      print(jug1+':',tanto1,'son mejores!!')
      puntos1 += puntos_tanto
      print(jug1,'suma',puntos_tanto,'puntos')

    else:
      print(jug1+': son buenas.')
      puntos2 += puntos_tanto
      print(jug2,'suma',puntos_tanto,'puntos')

  return puntos1, puntos2
  


def envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano):
  
  print('\nQue desea cantar?')
  print('1. Envido')
  print('2. Real envido')
  print('3. Falta envido')
  opcion = int(input('Elija:'))

  if opcion == 1:             #ENVIDO (j1)
    puntos_tanto = 2
    puntos_al_no = 1
    print('\n'+jug1,'ha cantado ENVIDO')
    print('\n',jug2,', que desea hacer?')
    print('1. Envido')
    print('2. Real envido')
    print('3. Falta envido')
    print('4. Quiero')
    print('5. No quiero')
    opcion = int(input('Elija:'))

    if opcion == 1:              #ENVIDO (j1) ENVIDO (j2)
      puntos_al_no = puntos_tanto
      puntos_tanto = 4
      print('\n'+jug2,'ha cantado ENVIDO')
      print('\n',jug1,', que desea hacer?')
      print('1. Real envido')
      print('2. Falta envido')
      print('3. Quiero')
      print('4. No quiero')
      opcion = int(input('Elija:'))

      if opcion == 1:              #ENVIDO (j1) ENVIDO (j2) REAL ENVIDO (j1)
        puntos_al_no = puntos_tanto
        puntos_tanto = 7
        puntos1, puntos2 = real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano)
        
      elif opcion == 2:                   #ENVIDO (j1) ENVIDO (j2) FALTA ENVIDO (j1)
        puntos_al_no=4
        puntos1, puntos2 = falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
      
      elif opcion == 3:                   # ENVIDO (j1) ENVIDO (j2) QUIERO (j1)
        print('\n',jug1,' ha dicho QUIERO')
        puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
      
      elif opcion == 4:                   # ENVIDO (j1) ENVIDO (j2) NO QUIERO (j1)
        print('\n',jug1,' ha dicho NO QUIERO.',jug2,'suma',puntos_al_no,'puntos')
        puntos2 += puntos_al_no
    
    elif opcion == 2:                     #ENVIDO (j1) REAL ENVIDO (j2)
      puntos_al_no = puntos_tanto
      puntos_tanto=5
      puntos1, puntos2 = real_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_tanto, puntos_al_no, mano)
      
    elif opcion == 3:                     #ENVIDO (j1) FALTA ENVIDO (j2)
      puntos_al_no=2
      puntos1, puntos2 = falta_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_al_no, mano)
    
    elif opcion == 4:                     #ENVIDO (j1) QUIERO (j2)
      print('\n',jug2,' ha dicho QUIERO')
      puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
    
    elif opcion == 5:                     #ENVIDO (j1) NO QUIERO (j2)
      print('\n',jug2,' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
      puntos1 += puntos_al_no
    
  elif opcion == 2:                     #REAL ENVIDO (j1) 
    puntos_al_no = 1
    puntos_tanto = 32
    puntos1, puntos2 = real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano)
  
  elif opcion == 3:
    puntos_al_no=1
    puntos1, puntos2 = falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
  
  return puntos1, puntos2






######################################################### TRUCO #############################################################################






def CantarTruco (p1, p2): 

  quiero = True
  ganador = ''

  print('\n'+p1,'ha cantado TRUCO!')
  print('\n'+p2+', que desea hacer?')
  print('1. Retruco')
  print('2. Quiero')
  print('3. No quiero')
  opcion = int(input('Elija:'))

  if opcion == 1:
    puntos_truco, quiero, ganador = CantarReTruco (p2, p1)
  
  elif opcion == 2:
    print('\n'+p2+', ha dicho QUIERO')
    puntos_truco = 2
          
  elif opcion == 3:
    print('\n'+p2+', ha dicho NO QUIERO')
    puntos_truco = 1
    quiero = False
    ganador = p1
  
  return puntos_truco, quiero, ganador

def CantarReTruco (p1, p2):

  quiero = True
  ganador = ''

  print('\n'+p1,'ha cantado RE TRUCO!')
  print('\n'+p2+', que desea hacer?')
  print('1. Vale cuatro')
  print('2. Quiero')
  print('3. No quiero')
  opcion = int(input('Elija:'))

  if opcion == 1:
    puntos_truco, quiero, ganador = CantarValeCuatro(p2, p1)
  
  elif opcion == 2: 
    print('\n'+p2+', ha dicho QUIERO')
    puntos_truco = 3

  elif opcion == 3:
    print('\n'+p2+', ha dicho NO QUIERO')
    puntos_truco = 2
    quiero = False
    ganador = p1

  return puntos_truco, quiero, ganador

def CantarValeCuatro(p1, p2):
  
  quiero = True
  ganador = ''

  print('\n'+p1,'ha cantado QUIERO VALE CUATRO!')
  print('\n'+p2+', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = int(input('Elija:'))

  if opcion == 1:
    print('\n'+p2+', ha dicho QUIERO')
    puntos_truco = 4
  
  elif opcion == 2:
    print('\n'+p2+', ha dicho NO QUIERO')
    puntos_truco = 3
    quiero = False
    ganador = p1

  return puntos_truco, quiero, ganador




########################################################### FUNCIONES ######################################################################





def mostrar_cartas(lista):
  cartas = "sus cartas son: "
  for i in lista:
    cartas += (str(i)+', ')
  
  return cartas

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

def JugarPrimera (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_truco):
  
  termino = False
  hubo_envido = False
  carta1_p1=''
  ganador = ''

  if puntos_truco == 1:
    print('\n'+jug1+', que desea hacer?')
    print('1. Cantar envido')
    print('2. Cantar truco')
    print('3. Tirar carta')
    print('4. Irse al mazo') 
    opcion = int(input('Elija:'))

    if opcion == 1:
      puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
      hubo_envido = True
      
      print('\n'+jug1+', que desea hacer?')
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))

      if opcion == 1:
        puntos_truco, quiero, ganador = CantarTruco (jug1, jug2)
      
        if quiero == False:
          termino = True
        
        else:
          carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
          print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
      
      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
    
      elif opcion == 3:
        termino = True
        ganador = jug2

    elif opcion == 2:
      puntos_truco, quiero, ganador = CantarTruco (jug1, jug2)
    
      if quiero == False:
        termino = True
      
      else:
        carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 3:
      carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
      print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 4:
      termino = True
      ganador = jug2

  elif puntos_truco == 2:
    print('\n'+jug1+', que desea hacer?')
    print('1. Cantar envido')
    print('2. Cantar retruco')
    print('3. Tirar carta')
    print('4. Irse al mazo') 
    opcion = int(input('Elija:'))

    if opcion == 1:
      puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
      hubo_envido = True
      
      print('\n'+jug1+', que desea hacer?')
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))

      if opcion == 1:
        puntos_truco, quiero, ganador = CantarReTruco (jug1, jug2)
    
        if quiero == False:
          termino = True
        
        else:
          carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
          print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
    
      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
    
      elif opcion == 3:
        termino = True
        ganador = jug2

    elif opcion == 2:
      puntos_truco, quiero, ganador = CantarReTruco (jug1, jug2)
    
      if quiero == False:
        termino = True
      
      else:
        carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 3:
      carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
      print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 4:
      termino = True
      ganador = jug2
    
  elif puntos_truco == 3:
    print('\n'+jug1+', que desea hacer?')
    print('1. Cantar envido')
    print('2. Cantar vale cuatro')
    print('3. Tirar carta')
    print('4. Irse al mazo') 
    opcion = int(input('Elija:'))

    if opcion == 1:
      puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
      hubo_envido = True
      
      print('\n'+jug1+', que desea hacer?')
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))

      if opcion == 1:
        puntos_truco, quiero, ganador = CantarValeCuatro (jug1, jug2)
    
        if quiero == False:
          termino = True
        
        else:
          carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
          print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
    
      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
      
      elif opcion == 3:
        termino = True
        ganador = jug2

    elif opcion == 2:
      puntos_truco, quiero, ganador = CantarValeCuatro (jug1, jug2)
  
      if quiero == False:
        termino = True
      
      else:
        carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 3:
      carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
      print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 4:
      termino = True
      ganador = jug2
    
  elif puntos_truco == 4:
    print('\n'+jug1+', que desea hacer?')
    print('1. Cantar envido')
    print('2. Tirar carta')
    print('3. Irse al mazo') 
    opcion = int(input('Elija:'))

    if opcion == 1:
      puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
      hubo_envido = True
      
      print('\n'+jug1+', que desea hacer?')
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = int(input('Elija:'))

      if opcion == 1:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
      
      elif opcion == 2:
        termino = True
        ganador = jug2

    elif opcion == 2:
      carta1_p1, cartasj1 = tirar_3(p1, cartasj1)
      print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = jug2

  return puntos1, puntos2, puntos_truco, termino, hubo_envido, carta1_p1, cartasj1, ganador

def JugarPrimeraSinTanto (jug1, cartasj1, jug2, puntos_truco):
  
  quiero = True
  carta1_p1 = ''
  ganador = ''
  termino = False 

  if puntos_truco == 1:
    print('\n'+jug1+', que desea hacer?')
    print('1. Cantar truco')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('Elija:'))

    while opcion not in [1,2,3]:
      print('\n'+jug1+', que desea hacer?')
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))

    if opcion == 1:
      puntos_truco, quiero, ganador = CantarTruco (jug1, jug2)

      if quiero == False:
        termino = True
    
      else:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 2:
      carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
      print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = jug2

  elif puntos_truco == 2:
    print('\n'+jug1+', que desea hacer?')
    print('1. Cantar retruco')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('Elija:'))
    
    while opcion not in [1,2,3]:
      print('\n'+jug1+', que desea hacer?')
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))

    if opcion == 1:
      puntos_truco, quiero, ganador = CantarReTruco (jug1, jug2)

      if quiero == False:
        termino = True
    
      else:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 2:
      carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
      print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = jug2

  elif puntos_truco == 3:
    print('\n'+jug1+', que desea hacer?')
    print('1. Cantar vale cuatro')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('Elija:'))

    while opcion not in [1,2,3,]:
      print('\n'+jug1+', que desea hacer?')
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))
    
    if opcion == 1:
      puntos_truco, quiero, ganador = CantarValeCuatro (jug1, jug2)
        
      if quiero == False:
        termino = True
    
      else:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 2:
      carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
      print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = jug2
  
  elif puntos_truco == 4:
    print('\n'+jug1+', que desea hacer?')
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = int(input('Elija:'))

    while opcion not in [1,2]:
      print('\n'+jug1+', que desea hacer?')
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = int(input('Elija:'))

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
      print("\n{} ha tirado el {}".format(jug1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = jug2

  return puntos_truco, termino, carta1_p1, cartasj1, ganador

def Jugar_Segunda(p1, puntos1, p2, puntos2, cartasj1, puntos_truco):
  
  termino= False
  carta1_p1 = ""
  ganador = ''

  if puntos_truco == 1:
    print('\n'+p1+', que desea hacer?')
    print('1. Cantar truco')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('Elija:'))

    while opcion not in [1,2,3]:
      print('\n'+p1+', que desea hacer?')
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))
        
    if opcion == 1:
      
      puntos_truco, quiero, ganador = CantarTruco (p1, p2)
    
      if quiero == False:
        termino = True
      
      else:
        carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
        print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 2:
      carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
      print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = p2

  elif puntos_truco == 2:
    print('\n'+p1+', que desea hacer?')
    print('1. Cantar retruco')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('\tElija:'))

    while opcion not in [1,2,3]:
      print('\n'+p1+', que desea hacer?')
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))

    if opcion == 1:
      
      puntos_truco, quiero, ganador = CantarReTruco (p1, p2)
    
      if quiero == False:
        termino = True
      
      else:
        carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
        print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 2:
      carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
      print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = p2

  elif puntos_truco == 3:
    print('\n'+p1+', que desea hacer?')
    print('1. Cantar vale cuatro')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('\tElija:'))

    while opcion not in [1,2,3]:
      print('\n'+p1+', que desea hacer?')
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))

    if opcion == 1:     
      puntos_truco, quiero, ganador = CantarValeCuatro (p1, p2)
    
      if quiero == False:
        termino = True
      
      else:
        carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
        print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 2:
      carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
      print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = p2

  elif puntos_truco == 4:
    carta1_p1,cartasj1 = tirar_2(p1,cartasj1)
    print("\n{} ha tirado el {}".format(p1,carta1_p1))
     
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador 

def Jugar_Tercera(p1, puntos1, p2, puntos2, cartasj1, puntos_truco):
  
  termino= False
  carta1_p1 = ""
  ganador = ''

  if puntos_truco == 1:
    print('\n'+p1+', que desea hacer?')
    print('1. Cantar truco')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('Elija:'))

    while opcion not in [1,2,3]:
      print('\n'+p1+', que desea hacer?')
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('Elija:'))
    
    if opcion == 1:
      puntos_truco, quiero, ganador = CantarTruco (p1, p2)
    
      if quiero == False:
        termino = True
      
      else:
        carta1_p1,cartasj1 = tirar_1(p1,cartasj1)
        print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 2:
      carta1_p1,cartasj1 = tirar_1(p1,cartasj1)
      print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = p2

  elif puntos_truco == 2:
    print('\n'+p1+', que desea hacer?')
    print('1. Cantar retruco')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('\tElija:'))

    while opcion not in [1,2,3]:
      print('\n'+p1+', que desea hacer?')
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))

    if opcion == 1:
      
      puntos_truco, quiero, ganador = CantarReTruco (p1, p2)
    
      if quiero == False:
        termino = True
      
      else:
        carta1_p1, cartasj1 = tirar_1(p1,cartasj1)
        print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 2:
      carta1_p1, cartasj1 = tirar_1(p1,cartasj1)
      print("\n{} ha tirado el {}".format(p1,carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = p2

  elif puntos_truco == 3:
    print('\n'+p1+', que desea hacer?')
    print('1. Cantar vale cuatro')
    print('2. Tirar carta')
    print('3. Irse al mazo')
    opcion = int(input('\tElija:'))

    while opcion not in [0,1,2,3]:
      print('\n'+p1+', que desea hacer?')
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = int(input('\tElija:'))

      if opcion == 1:
        
        puntos_truco, quiero, ganador = CantarValeCuatro (p1, p2)
      
        if quiero == False:
          termino = True
        
        else:
          carta1_p1,cartasj1 = tirar_1(p1,cartasj1)
          print("\n{} ha tirado el {}".format(p1,carta1_p1))

      elif opcion == 2:
        carta1_p1,cartasj1 = tirar_1(p1,cartasj1)
        print("\n{} ha tirado el {}".format(p1,carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

  elif puntos_truco == 4:
    carta1_p1,cartasj1 = tirar_1(p1,cartasj1)
    print("\n{} ha tirado el {}".format(p1,carta1_p1))
     
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador 






############################################################## MAIN ###########################################################################

registro_partidas = open("Registro partidas.txt", "a") 

nombre1 = input("Ingrese el nombre de un jugador")
nombre2 = input("Ingrese el nombre del otro jugador")

jugador1 = Jugador(nombre1)
jugador2 = Jugador(nombre2)

p1 = jugador1.nombre
puntos1 = 0
p2 = jugador2.nombre 
puntos2 = 0
ronda = 1

escribir = "Se ha iniciado una nueva partida entre: " + p1 + " y " + p2

registro_partidas.write(escribir)

while puntos1 < 30 and puntos2 < 30:
  
  mazo=Mazo()       #Se crea el mazo

  cartas_en_juego = mazo.repartir()      #Se reparte el mazo

  mano, puntos_mano, pie, puntos_pie = quien_es_mano (ronda, p1, puntos1, p2, puntos2)        #Se determina que jugador es mano

  cartasmano = [cartas_en_juego[0],cartas_en_juego[2],cartas_en_juego[4]]         #Se dan las cartas al mano y al pie
  cartaspie = [cartas_en_juego[1],cartas_en_juego[3],cartas_en_juego[5]]

  print('Comienza la ronda '+str(ronda)+'!')

  print('\n'+mano, 'es MANO. Estas son sus cartas:')
  print(mostrar_cartas(cartasmano))
  print('\n')
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

    #Primera mano

    puntos_mano, puntos_pie, puntos_truco, termino, hubo_envido, carta1_mano, cartasmano2, ganador  = JugarPrimera (mano, puntos_mano, cartasmano, pie, puntos_pie, cartaspie, puntos_truco)
    
    if termino == True:
         break
    
    if hubo_envido == True:
      puntos_truco, termino, carta1_pie, cartaspie, ganador  = JugarPrimeraSinTanto (pie, cartaspie, mano, puntos_truco)
  
      if termino == True: #HAY QUE PRINTEAR CUANTOS PUNTOS SUMA Y QUIEN GANO LA MANO EN TODOS LOS BREAKS Y VER QUIEN GANO LOS PUNTOS
        break

    elif hubo_envido == False:
      puntos_pie, puntos_mano, puntos_truco, termino, hubo_envido, carta1_pie, cartaspie, ganador  = JugarPrimera (pie, puntos_pie, cartaspie, mano, puntos_mano, cartasmano, puntos_truco)

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
      
      puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pies, ganador = Jugar_Segunda(pie, puntos_pie, mano, puntos_mano,cartaspie, puntos_truco)

      if termino == True: 
        break

      puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador = Jugar_Segunda(mano, puntos_mano,pie,puntos_pie,cartasmano, puntos_truco)
      
      if termino == True: 
        break

    elif ganador1 == mano: #la mano gano primera arranca la 2 el
      
      puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador = Jugar_Segunda(mano, puntos_mano,pie,puntos_pie,cartasmano, puntos_truco)
      
      if termino == True: 
        break

      puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pies, ganador = Jugar_Segunda(pie, puntos_pie, mano, puntos_mano,cartaspie, puntos_truco)
      
      if termino == True: 
        break

    elif  parda1 == True: #Se juega la parda
      
      puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador = Jugar_Segunda(mano, puntos_mano,pie,puntos_pie,cartasmano, puntos_truco)
      
      if termino == True: 
        break
      
      puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pies, ganador = Jugar_Segunda(pie, puntos_pie, mano, puntos_mano,cartaspie,puntos_truco )
      
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
    
      puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pies, ganador = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano,cartaspie, puntos_truco)

      if termino == True: 
        break

      puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador = Jugar_Tercera (mano, puntos_mano,pie,puntos_pie,cartasmano, puntos_truco)
      
      if termino == True: 
        break

    elif ganador2 == mano: #mano gano 2 arranca en 3
      puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador = Jugar_Tercera (mano, puntos_mano,pie,puntos_pie,cartasmano, puntos_truco)
      
      if termino == True: 
        break

      puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pies, ganador = Jugar_Tercera(pie, puntos_pie, mano, puntos_mano,cartaspie, puntos_truco)
      
      if termino == True: 
        break
      
    elif  parda2 == True and parda1 == True: #Se juega la parda
      puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador = Jugar_Tercera(mano, puntos_mano,pie,puntos_pie,cartasmano, puntos_truco)
      
      if termino == True: 
        break
      
      puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pies, ganador = Jugar_Tercera(pie, puntos_pie, mano, puntos_mano,cartaspie,puntos_truco )
      
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
    registro_partidas.write("\nHa ganado: ", mano, " se le suman ", puntos_truco, " puntos") 
    
  elif ganador == pie:
    puntos_pie += puntos_truco
    print("\nHa ganado: ", pie, " se le suman ", puntos_truco, " puntos")
    registro_partidas.write("\nHa ganado: ", pie, " se le suman ", puntos_truco, " puntos") 

  if p1 == mano:
    puntos1 = puntos_mano
    puntos2 = puntos_pie
  elif p2 == mano:
    puntos2 = puntos_mano
    puntos1 = puntos_pie
  
  print('\nPuntos de '+ p1 + ": " + str(puntos1))
  print('\nPuntos de' + p2 + ": " + str(puntos2))
  print('\n------------------------------------------------------------------------------\n\n')
  registro_partidas.write('\nPuntos de '+ p1 + ": " + str(puntos1))
  registro_partidas.write('\nPuntos de ' + p2 + ": " + str(puntos2))
  registro_partidas.write('\n------------------------------------------------------------------------------\n\n')

  ronda +=1


if puntos1 >= 30 and puntos2 >= 30:
        
  if puntos1 > puntos2:
    print('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
    registro_partidas.write('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
        
  elif puntos2 > puntos1:
    print('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
    registro_partidas.write('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')

  elif puntos2 == puntos1:
    print('\nHA HABIDO UN EMPATE.')
    registro_partidas.write('\nHA HABIDO UN EMPATE.')

elif puntos2 >= 30:
  print('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
  registro_partidas.write('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')

elif puntos1 >= 30:
  print('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
  registro_partidas.write('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')



  registro_partidas.close() 